import STO_tests_V2_nanopb_pb2 as Messages
import serial
portNumber = "COM6"  # Replace with the appropriate COM port name
baudrate = 115200  # Replace with the desired baud rate
UART = serial.Serial(portNumber, baudrate=baudrate,timeout=10)
def Test1_run():
  RXbuf = bytearray(256)
  Resultbuf = bytearray()
  Command = Messages.TestData()
  Result = Messages.TestData()
  Command.method=0
  Command.testNumber=1
  Command=Command.SerializeToString()
  #print(Command)
  UART.write(Command)
  while (RXbuf[0] == 0):
    bytes_read = UART.readinto(RXbuf)
  for i in range(0, bytes_read):
    Resultbuf.append(RXbuf[i])
  Result.ParseFromString(bytes(Resultbuf))
  print(Result)
def Test2_run():
  RXbuf = bytearray(256)
  Resultbuf = bytearray()
  Command = Messages.TestData()
  Result = Messages.TestData()
  Command.method=0
  Command.testNumber=2
  Command=Command.SerializeToString()
  #print(Command)
  UART.write(Command)
  while (RXbuf[0] == 0):
    bytes_read = UART.readinto(RXbuf)
  for i in range(0, bytes_read):
    Resultbuf.append(RXbuf[i])
  Result.ParseFromString(bytes(Resultbuf))
  print(Result)
def Test3_run(accDataNumber):
  RXbuf = bytearray(256)
  Resultbuf = bytearray()
  Command = Messages.TestData()
  Result = Messages.TestData()
  Command.method=0
  Command.testNumber=3
  Command=Command.SerializeToString()
  Command.accDataNumber=accDataNumber
  #print(Command)
  UART.write(Command)
  while (RXbuf[0] == 0):
    bytes_read = UART.readinto(RXbuf)
  for i in range(0, bytes_read):
    Resultbuf.append(RXbuf[i])
  Result.ParseFromString(bytes(Resultbuf))
  print(Result)
def Test4_run(Seatbelt_position):
  RXbuf=bytearray(256)
  Resultbuf=bytearray()
  Command = Messages.TestData()
  Result  = Messages.TestData()
  Command.method=0
  Command.testNumber=4
  Command.Seatbelt_position=Seatbelt_position
  Command.VehicleStateExtended=1
  Command=Command.SerializeToString()
  #print(Command)
  UART.write(Command)
  while (RXbuf[0]==0):
      bytes_read=UART.readinto(RXbuf)
  for i in range(0,bytes_read):
    Resultbuf.append(RXbuf[i])
  Result.ParseFromString(bytes(Resultbuf))
  print(Result)



