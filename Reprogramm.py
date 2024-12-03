import time
import codecs
import re
import math
import serial
import threading
import numpy as np
'''def pretty_print(msg):
    fmt_str = "-----------------------"
    print(f"\n{fmt_str}{msg}{fmt_str}\n")'''

_byte_cnt=0
class HexOp():
    def __init__(self, filename):
        self.file = filename
        self._byte_cnt = 0
        self._bytesCntInString = 32
        self._CRC32_POLY = 0xEDB88320
        self._flashOffset = 0x08018000
        self.msg_count = 0
        self.percent_increment = 0

    def readHex(self):
        with open(self.file, 'rb') as f:
            _hexdata = codecs.decode(f.read().hex(), 'hex').decode("utf-8")  # to string
        self.hexarr = re.split(r'[\r&\n&:]', _hexdata)
        self.hexarr[:] = [hexstr[8:(8 + int(hexstr[0:2], 16) * 2)] for hexstr in self.hexarr if hexstr != '' and hexstr[6:8] == '00']  # delete first 4 bytes
        print(self.hexarr)

    def getNextByte(self):
        global _byte_cnt
        bytePtrInStr = (_byte_cnt - int(_byte_cnt / self._bytesCntInString) * self._bytesCntInString)
        hexstr = self.hexarr[int(_byte_cnt / self._bytesCntInString)][bytePtrInStr:bytePtrInStr + 2]
        _byte_cnt += 2
        val = int.from_bytes(bytes.fromhex(hexstr), "big")
        return val  # hexstr.encode().hex()

    def getHexZise(self):
        #global _byte_cnt
        #_byte_cnt=0
        hexsize=int((len(self.hexarr) - 1) * 16 + len(self.hexarr[-1]) / 2)
        self.msg_count=int(round(hexsize/7))
        self.percent_increment=int(round(self.msg_count/95))
        return hexsize

    def CalculateHexCRC32(self, startAddr, endAddr):
        global _byte_cnt
        temp_crc = (0xFFFFFFFF)
        # temp_crc = 0
        startAddr -= (self._flashOffset)
        endAddr -= (self._flashOffset)
        _byte_cnt = 0
        print(endAddr)
        f = open('CRC_log_script.txt', 'w+')
        while startAddr < endAddr:
            if startAddr == 0x8000:
                startAddr = 0x8000
            temp_crc = temp_crc ^ self.getNextByte()
            for _ in range(0, 8):
                mask = -(temp_crc & 1)
                temp_crc = (temp_crc >> 1) ^ (self._CRC32_POLY & mask)
            f.write(f"{hex(temp_crc)}\n")
            startAddr += 1
        f.close()
        return ~temp_crc
    def clear(self):
        self.hexarr.clear()
        self._byte_cnt=0



class UART_Transmitter():
    def __init__(self, COM_PORT, progressbar, hexhandler):
        self.appHex=hexhandler
        self.UART = serial.Serial(COM_PORT,115200)
        self.ProgressbarValue=0
        self.Progress_bar=progressbar
        self.msg_send = int(0)
        self.mutex = threading.Lock()
        self.lastframe_flag = False
        self.Sizebuf = [0, 0, 0]
        resp = 0

    def safe_receive(self) -> int:
        for i in range(5):
            #self.resp = self.UART.read(0.150)
            start_time = time.time()
            while time.time() - start_time < 0.50:
                if self.UART.in_waiting > 0:
                    self.resp = self.UART.read(self.UART.in_waiting)
                else:
                    self.resp=bytearray([0])
            if (self.resp and self.resp[0] != 0):
                print(f"Resp: {self.resp}")
                return i
        return 5

    def read(self, size):
        self.UART.read(size)
    def receive_status_message(self):
        REQUESTING_DOWNLOAD = bytes([0x12,0x21,0x12])
        DOWNLOAD_REQUEST_ACCEPTED = bytes([0x21, 0x12, 0x21])
        ERASING_FLASH = bytes([0x0a, 0xa0, 0x0a])
        FLASH_ERASE_SUCCESS = bytes([0xA0, 0x0A, 0xA0])
        TRANSMITTING_PROGRAM = bytes([0xA5, 0x0A5, 0xA5])
        TERMINATING_TRANSFER = bytes([0x5A, 0x5A, 0x5A])
        REQUEST_CRC_VERIFICATION = bytes([0xAB, 0xAB, 0xAB])
        CRC_VERIFICATION_SUCCESS = bytes([0xBA, 0xBA, 0xBA])
        CRC_VERIFICATION_FAIL = bytes([0xBB,0xBB,0xBB])
        REPROGRAMMING_SUCCESS = bytes([0xBF,0xFB,0xBF])
        REPROGRAMMING_FAIL = bytes([0xFB, 0xBF, 0xFB])
        RST = bytes([0xFC, 0xCF, 0xFC])
        status_msg= self.UART.read(3)
        if(status_msg==ERASING_FLASH):
            return "STARTING FLASH ERASE"
        elif(status_msg==FLASH_ERASE_SUCCESS):
            return "FLASH ERASE SUCCESS"
        elif (status_msg == REQUESTING_DOWNLOAD):
            return "REQUESTING DOWNLOAD"
        elif (status_msg == DOWNLOAD_REQUEST_ACCEPTED):
            return "DOWNLOAD REQUEST ACCEPTED"
        elif (status_msg == TRANSMITTING_PROGRAM):
            return "TRANSMITTING PROGRAM"
        elif (status_msg == TERMINATING_TRANSFER):
            return "TERMINATING TRANSFER"
        elif (status_msg == REQUEST_CRC_VERIFICATION):
            return "REQUEST CRC VERIFICATION"
        elif (status_msg == CRC_VERIFICATION_SUCCESS):
            return "CRC VERIFICATION SUCCESS"
        elif (status_msg == CRC_VERIFICATION_FAIL):
            return "CRC VERIFICATION FAIL"
        elif (status_msg == REPROGRAMMING_SUCCESS):
            return "REPROGRAMMING SUCCESS"
        elif (status_msg == REPROGRAMMING_FAIL):
            return "REPROGRAMMING FAIL"
        elif (status_msg == RST):
            return "RESET"

    def UART_send_with_resp(self, request):
        while True:
            while True:
                self.UART.write(request)
                print(f"Req:    {request}")
                time.sleep(0.150)
                if (self.safe_receive() != 5):
                    break
            # print(f"Resp: {resp}")
            if self.resp[1] == 0x7F:
                print("Error in previous message")
            if self.resp[3] != 0x78:
                break
            elif self.resp[1] == request[1] + 0x40 or self.resp[0] == 0x30 or request[0] & 0x20 != 0:
                break


        return self.resp

    def UART_send_no_resp(self, req):
        self.UART.write(req)
        time.sleep(0.150)
        print(f"Req:    {req}")
        return

    def UART_send_fisrt_program(self, req,size=1):
        while True:
            self.UART.write(req)
            print(f"Req:    {req}")
            time.sleep(0.15)
            resp = self.UART.read(size)  # Wait FCF
            print(f"Resp: {resp}")
           # if (resp[0] == 0x30):
                #break
        return

    def sendFlashPage(self, page_size):
        self.resp=bytearray([0,0])
        self.lastframe_warner=bytearray([0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0])
        self.last_frame_of_page=bytearray([0xEE,0xEE,0xEE,0xEE,0xEE,0xEE,0xEE,0xEE])
        transferDataRefFirst[0] = 0x10 | ((page_size & 0xF00) >> 8)
        transferDataRefFirst[1] = (page_size & 0xFF) + 2
        transferDataRefFirst[2] = 0x36
        transferDataRefFirst[3] = 0x00 if ((transferDataRefFirst[3] + 1) > 0xFF) else (
                    transferDataRefFirst[3] + 1)
        transferDataRefFirst[4] = self.appHex.getNextByte()
        transferDataRefFirst[5] = self.appHex.getNextByte()
        transferDataRefFirst[6] = self.appHex.getNextByte()
        transferDataRefFirst[7] = self.appHex.getNextByte()
        transferDataRefConsec[0] = 0x20
        #self.UART_send_fisrt_program(transferDataRefFirst)
        self.UART.write(transferDataRefFirst)
        self.msg_send+=1
        #if(self.msg_send % self.appHex.percent_increment == 0):
            #self.ProgressbarValue+=1

        time.sleep(0.05)
        for _ in range(math.floor((page_size - 4) / 7)):
            transferDataRefConsec[0] = 0x20 if ((transferDataRefConsec[0] + 1) > 0x2F) else (
                        transferDataRefConsec[0] + 1)
            for i in range(1, 8):
                transferDataRefConsec[i] = self.appHex.getNextByte()
            #self.UART_send_no_resp(transferDataRefConsec)
            self.UART.write(transferDataRefConsec)
            self.msg_send += 1
            if (self.msg_send % self.appHex.percent_increment == 0):
                self.mutex.acquire()
                self.ProgressbarValue =self.ProgressbarValue+1
                self.mutex.release()
            time.sleep(0.05)
        # Last frame
        if (page_size - 4) % 7 != 0:
            transferDataRefConsec[0] = 0x20 if ((transferDataRefConsec[0] + 1) > 0x2F) else (
                        transferDataRefConsec[0] + 1)
            for i in range(1, (page_size - 4) % 7 + 1):
                transferDataRefConsec[i] = self.appHex.getNextByte()
            #transferDataRefConsec.dlc = (page_size - 4) % 7 + 1
            #self.UART_send_with_resp(transferDataRefConsec)
            self.lastframe_warner[7]=(page_size - 4) % 7
            if(self.lastframe_flag==True):
                self.UART.write(self.lastframe_warner)
            time.sleep(0.2)
            self.UART.write(self.last_frame_of_page)
            time.sleep(0.2)
            self.UART.write(transferDataRefConsec)
            time.sleep(0.05)
        #while self.resp[1] != 0x76:
            #self.safe_receive()

    def determineCRC(self, crc):
        CRCbuf=bytearray([0,0,0,0])
       # pretty_print("REQUEST CRC CALCULATION")
        CRCbuf[0] = (crc & 0xFF000000) >> 24
        CRCbuf[1] = (crc & 0x00FF0000) >> 16
        CRCbuf[2] = (crc & 0x0000FF00) >> 8
        CRCbuf[3] = (crc & 0x000000FF)
        self.UART.write(CRCbuf)
        self.UART.write(CRCbuf)
        for i in range(0,3):
            print(hex(int(CRCbuf[i])))
        '''self.UART_send_no_resp(UDScheckStartCRC2)
        self.UART_send_with_resp(UDScheckStartCRC3)
        time.sleep(10)
        while True:
            pretty_print("CHECK CRC CALCULATION RESULT")
            res = self.UART_send_with_resp(UDScheckCRCRes)
            if (res[1] == 0x71):
                return res'''

    '''def enterSecMode(self):
        pretty_print("SECURITY ACCESS")
        seed = self.UART_send_with_resp(reqSeed)
        if (seed[3] != 0 or seed[4] != 0 or seed[5] != 0 or seed[6] != 0):
            res = self.UART_send_with_resp(sendKey)'''

    def requestDownload(self):
            self.Sizebuf=bytearray(self.Sizebuf)
            self.UART.write(self.Sizebuf)
            time.sleep(0.5)
            self.UART.write(requestDownload1)
            time.sleep(0.5)
            self.UART.write(requestDownload2)
            time.sleep(0.1)
            '''self.UART_send_with_resp(requestDownload1)
            resp = self.UART_send_with_resp(requestDownload2)
            if resp[3] == 0x22:  # Transfer is already active, do reset
                pretty_print("RESET")
                self.UART_send_with_resp(doReset)
            else:
                return'''

    def transmitProgramm(self):
        # send data
        global lastframe_flag
        #pretty_print("TRANSFER DATA")
        self.updater()
        for j in range(math.floor(self.appHex.getHexZise() / 0x800)):
            self.sendFlashPage(0x800)
        self.lastframe_flag=True
        self.sendFlashPage(self.appHex.getHexZise() % 0x800)
    def update_progress(self):
        while(self.ProgressbarValue<95):
            self.mutex.acquire()
#            self.Progress_bar.setValue(3+self.ProgressbarValue)
            self.mutex.release()
        return
    def updater(self):
        updater=threading.Thread(target=self.update_progress)
        updater.start()

    def stopUART(self):
        #pretty_print("SUCCESSFUL REPROGRAMM")
        self.UART.close()


# --------------------------------------------CAN-MESSAGES------------------------------------------#
enterProgMode=bytearray([0x02, 0x10, 0x02],)
doReset=bytearray([0x02, 0x11, 0x01])
reqSeed=bytearray([0x03, 0x27, 0x01, 0x00])
sendKey=bytearray([0x06, 0x27, 0x02, 0x3F, 0x4D, 0xBB, 0x01],)
eraseFlash1=bytearray([0x10, 0x0A, 0x31, 0x01, 0xFF, 0x00, 0x01, 0x80])
eraseFlash2=bytearray([0x21, 0x00, 0x2F, 0xFF, 0xFF])
requestFlashEraseRes=bytearray([0x04, 0x31, 0x03, 0xFF, 0x00])
requestDownload1=bytearray([0x10, 0x09, 0x34, 0x00, 0x33, 0x01, 0x80, 0x00])
requestDownload2=bytearray([0x21, 0x01, 0x90, 0x00])
transferDataRefFirst=bytearray([0x18, 0x02, 0x36, 0x00, 0x11, 0x22, 0x33, 0x44])
transferDataRefConsec=bytearray([0x20, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55])
lastConsec=bytearray([0x29, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55])
checkDownloadRes=bytearray([0x29, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55])
requestTranferExit=bytearray([0x01, 0x37])
UDScheckStartCRC1=bytearray([0x10, 0x0E, 0x31, 0x01, 0xFF, 0x01, 0x01, 0x80])
UDScheckStartCRC2=bytearray([0x21, 0x00, 0x2F, 0xFF, 0xFF, 0x0, 0x0, 0x0])
UDScheckStartCRC3=bytearray([0x22, 0x00])
UDScheckCRCRes=bytearray([0x04, 0x31, 0x03, 0xFF, 0x01])

# -----------------------------------------PROGRAMM---------------------------------#
'''if __name__ == "Reprogramm":
    appHex = HexOp('hex_to_write.hex')
    appHex.readHex()
    hexsize = appHex.getHexZise()
    print(hexsize)'''
'''
requestDownload2[1] = (hexsize & 0xFF0000) >> 16
requestDownload2[2] = (hexsize & 0x00FF00) >> 8
requestDownload2[3] = (hexsize & 0x0000FF)
UDScheckStartCRC2[2] = ((hexsize + 0x18000) & 0xFF0000) >> 16
UDScheckStartCRC2[3] = ((hexsize + 0x18000) & 0x00FF00) >> 8
UDScheckStartCRC2[4] = ((hexsize + 0x18000) & 0x0000FF)
UARTDriver = UART_Transmitter()

pretty_print("ENTERING PROGRAMMING MODE")
UARTDriver.send_with_resp(enterProgMode)
UARTDriver.enterSecMode()

while True:
    UARTDriver.eraseFlash()
    UARTDriver.requestDownload()
    UARTDriver.transmitProgramm()

    # Calculate and chack CRC32
    crc = appHex.CalculateHexCRC32(0x08018000, 0x08018000 + hexsize)
    if (UARTDriver.determineCRC(crc)[5] == 0x00):
        break

pretty_print("RESET")
UARTDriver.send_with_resp(doReset)
UARTDriver.stopCan()'''

