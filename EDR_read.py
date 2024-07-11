#import can
import array as arr
#import tabulate
import re
import math

#EDR_buffer = arr.array('h', [0xfc,0xff,0xad,0xff,0xb0,0xff,0xbb,0xff,0xab,0xff,0xa2,0xff,0x75,0xff,0x38,0xff,0x36,0xff,0x2c,0xff,0x2d,0xff,0x65,0xff,0xb0,0xff,0xdf,0xff,0xf1,0xff,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x2c,0xff,0x10,0x27,0x0,0x0,0x0,0x3,0x4,0x5,0x6,0x7,0x8,0x9,0xa,0x1,0x1,0x1,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x7a,0xd,0x7a,0xd,0x0,0xdf,0xff,0xc,0x0,0x13,0x0,0xe,0x0,0x28,0x0,0x2f,0x0,0xfd,0xff,0x6,0x0,0xc,0x0,0x39,0x0,0x39,0x0,0x23,0x0,0xb,0x0,0x0,0x0,0xfd,0xff,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x39,0x0,0x10,0x27,0x25,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x7a,0xd,0x7a,0xd,0x7a,0xd,0x7a,0xd,0x7a,0xd,0x7a,0xd,0x0,0x0,0x0,0x0,0xb5,0xb5,0xb5,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xff,0x11,0x3f,0x0,0x3f,0x0,0x22,0xff,0xff,0xff,0xb,0x0,0x2,0x0,0x4,0x0,0x2,0x0,0x11,0x0,0x17,0x0,0x2,0x0,0x4,0x0,0x5,0x0,0x25,0x0,0x25,0x0,0xe,0x0,0x1,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x25,0x0,0x10,0x27,0xf0,0x3c,0x30,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0])
#EDR_buffer = arr.array('h', [])
EDR_postcrash_decoded = dict()
#EDR_postcrash_decoded = list()
EDR_precrash_arr_decoded = dict()
EDR_decoded = dict()
EDR_unsupported_decoded = dict()
#------------------Crash data----------------------#
LongdV_buf = list()
LateraldV_buf = list()
#--------------Precrash data---------------------#
Vehicle_Speed = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Brake_OnOff = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Engine_Revolutions_Per_Minute = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
ABS_activity = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Stability_control = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Steering_Angle = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Yaw_Rate = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Traction_Control_Status = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Cruise_Control_System = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Longitudinal_acceleration_pre_crash = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Lateral_acceleration_pre_crash = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Time = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
datalist=list([0 for i in range(0,40)])
print(datalist)
wnum = 0


'''def can_send(request):
    try:
        bus.send(request)
        print(f"Message sent on {bus.channel_info}")
    except can.CanError:
        print("Message NOT sent")
    return'''

#datalen - 1 or 2 bytes
def get_precrash_data_arr(word_num, datalen, EDR_name,EDR_buffer):
    precrash_buff = []

    if datalen == 1:
        for i in range(word_num, word_num + 11, 1):
            precrash_buff.append(EDR_buffer[i])
        EDR_precrash_arr_decoded.update([(EDR_name, precrash_buff)])
        word_num += 11
    elif datalen == 2:
        for i in range(word_num, word_num + 22, 2):
            precrash_buff.append((EDR_buffer[i+1]<<8) + EDR_buffer[i])
        EDR_precrash_arr_decoded.update([(EDR_name, precrash_buff)])
        word_num += 22 
    print(word_num)

    return word_num

def get_unsupported_data(word_num, arraylen, EDR_name):
    word_num += arraylen
    EDR_precrash_arr_decoded.update([(EDR_name, "Not supported")])
    return word_num

def get_single_data(word_num, datalen, EDR_name,EDR_buffer):
    if datalen == 1:
        EDR_decoded.update([(EDR_name, EDR_buffer[word_num])])
    elif datalen == 2:
        EDR_decoded.update([(EDR_name, (EDR_buffer[word_num+1] << 8) + EDR_buffer[word_num])])

    word_num += datalen
    print(word_num)
    return word_num

def get_dV(word_num, EDR_name,EDR_buffer):
    EDR_dv_buf = []
    for i in range(word_num, word_num + 50, 2):
        EDR_dv_buf.append(((EDR_buffer[i+1] << 8) + EDR_buffer[i]))
    word_num += 50
    EDR_postcrash_decoded.update([(EDR_name, EDR_dv_buf)])
    print(word_num)
    return word_num

def get_val_from_2s_compl(val, len):
    #val = int(val, 16)
    if(val&(1 << (len - 1)) != 0):
        val = val - (1 << len)
    return val

def to_yaw_rate(val):
    return (val-750)/10
    
def to_float_100_step(dV):
    return get_val_from_2s_compl(dV, 16)/100

def to_steer_offst(steer_code):
    return round((steer_code*0.01)-250,2)

def to_dV(dV):
    if dV == 0:
        return 0
    else:
        return round((dV/100 - 165.00),2)

def to_pos_float_100_step(val):
    return val/100

def to_uint_1_step(dV):
    return get_val_from_2s_compl(dV, 16)

def to_ttf(time):
    if time == 0:
        return 0
    else:
        return round(time/2, 1)
        #return round(time/100 - 482, 1)

def to_brake_state(UDS_val):
    match UDS_val:
        case 0:
            return "Disabled"
        case 1:
            return "Enabled"
        case _:
            return ""
    

def to_eng_rpm(UDS_val):
    return int(UDS_val)

def to_EDR_state(UDS_val):
    match UDS_val:
        case 0:
            return "Not activated"
        case 1:
            return "Activated"
        case 2:
            return "Fault"  
        case 3:
            return "User-defined"
        case _:
            return ""
def to_Stability_control(UDS_val):
    match UDS_val:
        case 0:
            return "Faulted"
        case 1:
            return "On"
        case 2:
            return "0ff"
        case 3:
            return "Engaged"
        case _:
            return ""
def to_ABS_activity(UDS_val):
    match UDS_val:
        case 0:
            return "Faulted"
        case 1:
            return "Non Engaged"
        case 2:
            return "Engaged"
        case _:
            return ""
        
def to_Cruise_control(UDS_val):
    match UDS_val:
        case 0:
            return "Actively controlling"
        case 1:
            return "Faulted"
        case 2:
            return "Off"
        case 3:
            return "On, but not controlling"
        case _:
            return ""
def to_Traction_control_status(UDS_val):
    match UDS_val:
        case 0:
            return "Faulted"
        case 1:
            return "On"
        case 2:
            return "Off"
        case 3:
            return "Engaged"

        
def to_precrash_acc(UDS_val):
    return (UDS_val - 15)*0.1
        
def to_SBS(UDS_val):
    match UDS_val:
        case 1:
            return "Bucled"
        case 0:
            return "Unbucled"
        case _:
            return ""
        
def to_lamp_state(UDS_val):
    match UDS_val:
        case 1:
            return "No warning"
        case 0:
            return "Warning"
        
def to_EDR_rec_st(UDS_val):
    match UDS_val:
        #case 0:
        #    return "Not recorded"
        #case 1:
        #    return "Recorded"
        case _:
            return "Recorded"  
        
def to_ingibit_st(UDS_val):
    match UDS_val:
        case 0:
            return "PAB enabled"
        case 1:
            return "PAB disabled"    

def to_TPMS_st(UDS_val):
    match UDS_val:
        case 0:
            return "Off"
        case 1:
            return "On"         

#------------------------Configurating CAN-bus-----------------------
'''bus=can.Bus(#interface='socketcan', 
            interface='socketcan', 
            channel='can0', 
            receive_own_messages=False, 
            bitrate=500000)
bus.set_filters([{"can_id": 0x772, "can_mask": 0x7FF, "extended": False}])

request = can.Message(arbitration_id=0x752,
                      data=[0x03, 0x22, 0xFA, 0x16],
                      is_extended_id=False)

consequtive = can.Message(arbitration_id=0x752,
                          data=[0x30, 0x00, 0x00, 0x00],
                          is_extended_id=False)

#--------------------Transmit CAN data stored to EDR-----------------
brake_r1_tx = can.Message(arbitration_id=0x5D7,
                      data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xF4], #5 km/h
                      is_extended_id=False)
bus.send_periodic(brake_r1_tx, 0.100)


swa_rnr_1 = can.Message(arbitration_id=0x0C6,
                          dlc = 8,
                          data=[0x0, 0x0, 0x0, 0x01, 0x09, 0x00, 0x01, 0x09], #Steer angle = 26,5 + 26,5 = 53
                          is_extended_id=False)
bus.send_periodic(swa_rnr_1, 0.010)

time_r_1 = can.Message(arbitration_id=0x53B,
                          dlc = 6,
                          data=[0x12, 0x04, 0x78, 0x18, 0x0A, 0x0C], #18.04.2024 12:10:30
                          is_extended_id=False)
bus.send_periodic(time_r_1, 3.0)

torque_at = can.Message(arbitration_id=0x17E,
                          dlc = 8,
                          data=[0x0, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], #gear pos = drive
                          is_extended_id=False)
bus.send_periodic(torque_at, 0.010)

torque_ecm = can.Message(arbitration_id=0x186,
                          dlc = 7,
                          data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x19], #engine rpm = 99.125
                          is_extended_id=False)
bus.send_periodic(torque_ecm, 0.010)

mii_ecm    = can.Message(arbitration_id=0x66A,
                          dlc = 8,
                          data=[0x0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20], #cruise control = SL active
                          is_extended_id=False)
bus.send_periodic(mii_ecm, 0.100)

brake_rnr4    = can.Message(arbitration_id=0x12E,
                          dlc = 8,
                          data=[0x0, 0x00, 0x00, 0x05, 0xD4, 0x00, 0x00, 0x00], #yaw rate = -60,2
                          is_extended_id=False)
bus.send_periodic(brake_rnr4, 0.010)

brake_rnr1    = can.Message(arbitration_id=0x242,
                          dlc = 8,
                          data=[0x0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], #no malfunction
                          is_extended_id=False)
bus.send_periodic(brake_rnr1, 0.020)

time.sleep(15)

#----------------------Get data from CAN-----------------------------
rec_msg = None
while rec_msg == None:
    can_send(request) 
    rec_msg = bus.recv(5)



for elem in rec_msg.data:
    print(hex(elem))
EDR_buffer.extend([rec_msg.data[5], rec_msg.data[6], rec_msg.data[7]])

while rec_msg:
    can_send(consequtive) 
    rec_msg = bus.recv(5)
    if rec_msg.dlc != 8:
        break
    EDR_buffer.extend([rec_msg.data[1], rec_msg.data[2], rec_msg.data[3], rec_msg.data[4], rec_msg.data[5], rec_msg.data[6], rec_msg.data[7]])

#add last frame
EDR_buffer.extend([rec_msg.data[1], rec_msg.data[2], rec_msg.data[3], rec_msg.data[4], rec_msg.data[5]])     
for elem in EDR_buffer:
    print(hex(elem))'''

'''EDR_buffer.extend([0x6D, 0x40, 0x2C,
0x40, 0xD8, 0x3F, 0xD5, 0x3F, 0x2B, 0x40,
0x72, 0x40, 0x75, 0x40, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x75, 0x40,
0x58, 0x1B, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0x01, 0x01, 0x01, 0x01,
0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
0x88, 0x00, 0xFE, 0xFE, 0x00, 0x00, 0x40,
0x1F, 0x40, 0x1F, 0xFE, 0xFE, 0xA5, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0x00, 0x00,
0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0xFF,
0xFF, 0xFF, 0xFF, 0xF4, 0xCD, 0x00, 0x20,
0xA5, 0xA5, 0xA5, 0xA5, 0xA5, 0xA5, 0xA5,
0xA5, 0xA5, 0xA5, 0xA5, 0xA5, 0xA5, 0xA5,
0xA5, 0xA5, 0xFD, 0xFF, 0xFF, 0xFF, 0x00,
0x00, 0x00, 0x00, 0x28, 0x00, 0x00, 0x20,
0xAC, 0x58, 0x00, 0x20, 0xAC, 0x58, 0x00,
0x20, 0xB3, 0x07, 0x0B, 0x00, 0xF9, 0x75,
0x00, 0x08, 0xF8, 0x75, 0x00, 0x08, 0x00,
0x00, 0x00, 0x61, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x20, 0xC6, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0x00, 0x00,
0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0xFF,
0xFF, 0xFF, 0xFF, 0xF4, 0xCD, 0x00, 0x20,
0xA5, 0xA5, 0xA5, 0xA5, 0xA5, 0xA5, 0xA5,
0xA5, 0xA5, 0xA5, 0xA5, 0xA5, 0xA5, 0xA5,
0xA5, 0xA5, 0xFD, 0xFF, 0xFF, 0xFF, 0x00,
0x00, 0x00, 0x00, 0x28, 0x00, 0x00, 0x20,
0xAC, 0x58, 0x00, 0x20, 0xAC, 0x58, 0x00,
0x20, 0xB3, 0x07, 0x0B, 0x00, 0xF9, 0x75,
0x00, 0x08, 0xF8, 0x75, 0x00, 0x08, 0x00,
0x00, 0x00, 0x61, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x20, 0xC6, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0x00, 0x00,
0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0xFF,
0xFF, 0xFF, 0xFF, 0xF4, 0xCD, 0x00, 0x20,
0xA5, 0xA5, 0xA5, 0xA5, 0xA5, 0xA5, 0xA5,
0xA5, 0xA5, 0xA5, 0xA5, 0xA5, 0xA5, 0xA5,
0xA5, 0xA5, 0xFD, 0xFF, 0xFF, 0xFF, 0x00,
0x00, 0x00, 0x00, 0x28, 0x00, 0x00, 0x20,
0xAC, 0x58, 0x00, 0x20, 0xAC, 0x58, 0x00,
0x20, 0xB3, 0x07, 0x0B, 0x00, 0xF9, 0x75,
0x00, 0x08, 0xF8, 0x75, 0x00, 0x08, 0x00,
0x00, 0x00, 0x61, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x20, 0xC6, 0x79,
0x40, 0x7A, 0x40, 0x7B, 0x40, 0x77, 0x40,
0x74, 0x40, 0x74, 0x40, 0x73, 0x40, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x7B, 0x40, 0xB8, 0x0B, 0x77, 0x40, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0xFE, 0xFF, 0xA5, 0xA5, 0xFE, 0xFF, 0xA5,
0xA5, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40,
0x1F, 0x40, 0x1F, 0xFE, 0xFE, 0xFE, 0xFE,
0x01, 0x00, 0x01, 0xFE, 0x0F, 0x0F, 0x0F,
0x0F, 0x0F, 0x13, 0x0F, 0x0F, 0x0F, 0x0F,
0x0F, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0C,
0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02,
0x02, 0x02, 0x02, 0x02, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFE, 0xFE, 0xFE, 0xFE])'''

#f = open('20g/EDR_front_crash_new_model.trc', 'r')
#content = f.readlines()
'''print()
print(re.split(r" +", content[2][42:50]))
EDR_buffer.extend([int(x, 16) for x in re.split(r" +", content[2][42:50])])
for i in range(118):
    print(i)
    arr = re.split(r" +", content[3+i][30:50])
    print(re.split(r" +", content[3+i][30:50]))
    try:
        arr.remove('')
    except:
        print("'' not in list")
    EDR_buffer.extend([int(x, 16) for x in arr])

print(EDR_buffer)
f.close()'''

def Parse_EDR(EDR_buffer):
    #----------------------------MESSAGE HANDLING--------------------------
    wnum = get_dV(0, "Longitudinal Delta-V Value", EDR_buffer)
    wnum = get_single_data(wnum, 2, "Max Longitudinal Delta-V Value", EDR_buffer)
    wnum = get_single_data(wnum, 2, "Max Longitudinal Delta-V Record Time", EDR_buffer)

    wnum = get_precrash_data_arr(wnum, 1, "Vehicle Speed", EDR_buffer)
    wnum = get_unsupported_data(wnum, 11, "Engine throttle, %")
    wnum = get_precrash_data_arr(wnum, 1, "Brake On/Off", EDR_buffer)
    wnum = get_single_data(wnum, 2, "Ignition cycle, crash", EDR_buffer)
    wnum = get_single_data(wnum, 2, "Ignition cycle, download", EDR_buffer)

    wnum = get_single_data(wnum, 1, "Driver SBS",EDR_buffer)
    wnum = get_single_data(wnum, 1, "Airbag warning lamp status", EDR_buffer)
    wnum = get_single_data(wnum, 2, "Deployment Time of Driver Frontal Airbag", EDR_buffer)
    wnum = get_single_data(wnum, 2, "Deployment Time of First RawPassenger Frontal Airbag", EDR_buffer)
    wnum = get_unsupported_data(wnum, 1, "Multi-event crash, number of events")
    wnum = get_unsupported_data(wnum, 1, "Time from event 1 to 2")
    wnum = get_single_data(wnum, 1, "Complete file recorded", EDR_buffer)

    wnum = get_unsupported_data(wnum, 126, "Lateral acceleration (post-crash)")
    wnum = get_unsupported_data(wnum, 126, "Longitudinal acceleration (post-crash)")
    wnum = get_unsupported_data(wnum, 126, "Normal acceleration (post-crash)")


    wnum = get_dV(wnum, "Lateral Delta-V Value",EDR_buffer)
    wnum = get_single_data(wnum, 2, "Max Lateral Delta-V Value", EDR_buffer)
    wnum = get_single_data(wnum, 2, "Max Lateral Delta-V Record Time", EDR_buffer)
    wnum = get_single_data(wnum, 2, "Time for maximum delta-V, resultant", EDR_buffer)

    wnum = get_precrash_data_arr(wnum, 2, "Engine Revolutions Per Minute", EDR_buffer)
    wnum = get_unsupported_data(wnum, 4, "Vehicle roll angle")
    wnum = get_unsupported_data(wnum, 4, "Vehicle roll rate")
    wnum = get_precrash_data_arr(wnum, 1, "ABS activity", EDR_buffer)
    wnum = get_precrash_data_arr(wnum, 1, "Stability control", EDR_buffer)
    wnum = get_precrash_data_arr(wnum, 2, "Steering Angle", EDR_buffer)

    wnum = get_single_data(wnum, 1, "Safety belt status, front passenger", EDR_buffer)
    wnum = get_single_data(wnum, 1, "Passenger air bag suppression status, front", EDR_buffer)

    wnum = get_single_data(wnum, 2, "Side air bag deployment, time to deploy, driver", EDR_buffer)
    wnum = get_single_data(wnum, 2, "Side air bag deployment, time to deploy, front passenger", EDR_buffer)
    wnum = get_single_data(wnum, 2, "Side curtain/tube air bag deployment, time to deploy, driver side", EDR_buffer)
    wnum = get_single_data(wnum, 2, "Side curtain/tube air bag deployment, time to deploy, passenger side", EDR_buffer)
    wnum = get_single_data(wnum, 2, "Pretensioner deployment, time to fire, driver", EDR_buffer)
    wnum = get_single_data(wnum, 2, "Pretensioner deployment, time to fire, front passenger", EDR_buffer)

    wnum = get_unsupported_data(wnum, 1, "Seat track position switch, driver")
    wnum = get_unsupported_data(wnum, 1, "Seat track position switch, front passenger")
    wnum = get_unsupported_data(wnum, 1, "Occupant size classification, driver")
    wnum = get_unsupported_data(wnum, 1, "Occupant size classification, front passenger")

    wnum = get_single_data(wnum, 1, "Safety belt status, rear right passenger", EDR_buffer)
    wnum = get_single_data(wnum, 1, "Safety belt status, rear centre passenger", EDR_buffer)
    wnum = get_single_data(wnum, 1, "Safety belt status, rear left passenger", EDR_buffer)
    wnum = get_unsupported_data(wnum, 1, "Tyre Pressure Monitoring System (TPMS) Warning Lamp Status")

    wnum = get_precrash_data_arr(wnum, 1, "Longitudinal acceleration (pre-crash)", EDR_buffer)
    wnum = get_precrash_data_arr(wnum, 1, "Lateral acceleration (pre-crash)", EDR_buffer)

    wnum = get_precrash_data_arr(wnum, 2, "Yaw Rate", EDR_buffer)
    wnum = get_precrash_data_arr(wnum, 1, "Traction Control Status", EDR_buffer)
    wnum = get_unsupported_data(wnum, 11, "Advanced emergency braking system status AEB")
    wnum = get_precrash_data_arr(wnum, 1, "Cruise Control System", EDR_buffer)


    #new
    # wnum = get_single_data(wnum, 1, "Accelerator Pedal Position, Percentage of Full Range")
    # wnum = get_single_data(wnum, 1, "Brake Pedal Position")

    # wnum = get_single_data(wnum, 2, "The PowerOn Cycle in Event")
    # wnum = get_single_data(wnum, 2, "The PowerOn Cycle when Reading")
    # wnum = get_single_data(wnum, 1, "VIN Code")
    # wnum = get_single_data(wnum, 1, "ECU Hardware Number of EDR Data Record")
    # wnum = get_single_data(wnum, 1, "ECU Serial Number of EDR Data Record")
    # wnum = get_single_data(wnum, 1, "ECU Software Number of EDR Data Record")

    # wnum = get_dV(wnum, "Squared Delta-V Value")
    # wnum = get_single_data(wnum, 2, "Maximum Squared Sum Delta-V Record Value")
    # wnum = get_single_data(wnum, 2, "Maximum Squared Sum Delta-V Record Time")
    # wnum = get_single_data(wnum, 2, "Collision Event End")

    # wnum = get_single_data(wnum, 1, "Year")
    # wnum = get_single_data(wnum, 1, "Month")
    # wnum = get_single_data(wnum, 1, "Date")
    # wnum = get_single_data(wnum, 1, "Hour")
    # wnum = get_single_data(wnum, 1, "Minutes")
    # wnum = get_single_data(wnum, 1, "Seconds")
    # wnum = get_single_data(wnum, 1, "Gear Postion")
    # wnum = get_single_data(wnum, 1, "Steering Signal Switch Status")
    # wnum = get_single_data(wnum, 1, "Synchronize Time before Event")

    #---------------------Filling display string--------------------
    #display_str = f'''
    #--------------------------CRASH DATA--------------------------
    #Time, ms:   Long dV, km/h:  Lateral dV, km/h:
    #'''
    for i in range(10, 260, 10):
        #display_str += f" {i}            {round(to_dV(EDR_postcrash_decoded['Longitudinal Delta-V Value'][int(i/10) - 1]),2)}"
        #display_str += f"                  {round(to_dV(EDR_postcrash_decoded['Lateral Delta-V Value'][int(i/10) - 1]),2)}\n"
        LongdV_buf.insert(int(i/10) - 1,(round(to_dV(EDR_postcrash_decoded['Longitudinal Delta-V Value'][int(i/10) - 1]),2)))
        LateraldV_buf.insert(int(i/10) - 1,(round(to_dV(EDR_postcrash_decoded['Lateral Delta-V Value'][int(i/10) - 1]),2)))
    datalist.insert( 0,(f"-----------------------------CRASH DATA--------------------------"))
    datalist.insert(1,( f"Max Longitudinal Delta-V Value: {to_dV(EDR_decoded['Max Longitudinal Delta-V Value'])}\n"))
    datalist.insert( 2,( f"Max Longitudinal Delta-V Record Time: {to_pos_float_100_step(EDR_decoded['Max Longitudinal Delta-V Record Time'])}\n"))
    datalist.insert( 3,( f"Max Lateral Delta-V Value: {to_dV(EDR_decoded['Max Lateral Delta-V Value'])}\n"))
    datalist.insert( 4,( f"Max Lateral Delta-V Record Time: {to_pos_float_100_step(EDR_decoded['Max Lateral Delta-V Record Time'])}\n"))
    datalist.insert( 5,( f"Time for maximum delta-V, resultant: {to_pos_float_100_step(EDR_decoded['Time for maximum delta-V, resultant'])}\n"))




    #display_str += f'''
    #-----------------------------PRECRASH DATA ARRAY--------------------------
    #Time, s:    Vehicle Speed     Brake On/Off    Engine RPM     ABS activity    Stability control   Steering Angle  Yaw Rate   Traction Control Status   Cruise Control System  Long acc, g   Lateral acc, g
    #'''
    for i in range(11):
        Time.append(f"{(i/2)-5.0}")
        Vehicle_Speed.insert(i, (f"{EDR_precrash_arr_decoded['Vehicle Speed'][i]}"))
        Brake_OnOff.insert(i,(f"{to_brake_state(EDR_precrash_arr_decoded['Brake On/Off'][i])}"))
        Engine_Revolutions_Per_Minute.insert(i,(f"{to_eng_rpm(EDR_precrash_arr_decoded['Engine Revolutions Per Minute'][i])}"))
        ABS_activity.insert(i, (f"{to_ABS_activity(EDR_precrash_arr_decoded['ABS activity'][i])}"))
        Stability_control.insert(i,( f"{to_Stability_control(EDR_precrash_arr_decoded['Stability control'][i])}"))
        Steering_Angle.insert(i,( f"{to_steer_offst(EDR_precrash_arr_decoded['Steering Angle'][i])}"))
        Yaw_Rate.insert(i,( f"{to_yaw_rate(EDR_precrash_arr_decoded['Yaw Rate'][i])}"))
        Traction_Control_Status.insert(i,( f"{to_Traction_control_status(EDR_precrash_arr_decoded['Traction Control Status'][i])}"))
        #display_str += f"           {to_EDR_ext_state(EDR_precrash_arr_decoded['Automatic Emergency Braking System Status'][i])}"
        Cruise_Control_System.insert(i,( f"{to_Cruise_control(EDR_precrash_arr_decoded['Cruise Control System'][i])}"))
        Longitudinal_acceleration_pre_crash.insert(i,( f"{to_precrash_acc(EDR_precrash_arr_decoded['Longitudinal acceleration (pre-crash)'][i])}"))
        Lateral_acceleration_pre_crash.insert(i,( f"{to_precrash_acc(EDR_precrash_arr_decoded['Lateral acceleration (pre-crash)'][i])}\n\n"))

    datalist.insert(6,( f"-----------------------------SINGLE DATA--------------------------"))
    datalist.insert(7,( f"Ignition cycle, crash: {EDR_decoded['Ignition cycle, crash']}\n"))
    datalist.insert(8,( f"Ignition cycle, download: {EDR_decoded['Ignition cycle, download']}\n"))
    datalist.insert(9,( f"Driver Seat Belt Status: {to_SBS(EDR_decoded['Driver SBS'])}\n"))
    datalist.insert(10,( f"Airbag warning lamp: {to_lamp_state(EDR_decoded['Airbag warning lamp status'])}\n"))
    datalist.insert(11,( f"Deployment Time of Driver Frontal Airbag: {to_ttf(EDR_decoded['Deployment Time of Driver Frontal Airbag'])}\n"))
    datalist.insert(12,( f"Deployment Time of First RawPassenger Frontal Airbag: {to_ttf(EDR_decoded['Deployment Time of First RawPassenger Frontal Airbag'])}\n"))
    datalist.insert(13,( f"Event Data Record Complete Status: {to_EDR_rec_st(EDR_decoded['Complete file recorded'])}\n"))
    datalist.insert(14,( f"Safety belt status, front passenger: {to_SBS(EDR_decoded['Safety belt status, front passenger'])}\n"))
    datalist.insert(15,( f"Passenger air bag suppression status, front: {to_ingibit_st(EDR_decoded['Passenger air bag suppression status, front'])}\n"))
    datalist.insert(16,( f"Side air bag deployment, time to deploy, driver: {to_ttf(EDR_decoded['Side air bag deployment, time to deploy, driver'])}\n"))
    datalist.insert(17,( f"Side air bag deployment, time to deploy, front passenger: {to_ttf(EDR_decoded['Side air bag deployment, time to deploy, front passenger'])}\n"))
    datalist.insert(18,( f"Side curtain/tube air bag deployment, time to deploy, driver side: {to_ttf(EDR_decoded['Side curtain/tube air bag deployment, time to deploy, driver side'])}\n"))
    datalist.insert(19,( f"Side curtain/tube air bag deployment, time to deploy, passenger side: {to_ttf(EDR_decoded['Side curtain/tube air bag deployment, time to deploy, passenger side'])}\n"))
    datalist.insert(20,( f"Pretensioner deployment, time to fire, driver: {to_ttf(EDR_decoded['Pretensioner deployment, time to fire, driver'])}\n"))
    datalist.insert(21,( f"Pretensioner deployment, time to fire, front passenger: {to_ttf(EDR_decoded['Pretensioner deployment, time to fire, front passenger'])}\n"))
    datalist.insert(22,( f"Safety belt status, rear right passenger: {to_SBS(EDR_decoded['Safety belt status, rear right passenger'])}\n"))
    datalist.insert(23,( f"Safety belt status, rear centre passenger: {to_SBS(EDR_decoded['Safety belt status, rear centre passenger'])}\n"))
    datalist.insert(24,( f"Safety belt status, rear left passenger: {to_SBS(EDR_decoded['Safety belt status, rear left passenger'])}\n"))
    #display_str += f"Tyre Pressure Monitoring System (TPMS) Warning Lamp Status: {to_TPMS_st(EDR_decoded['Safety belt status, rear left passenger'])}\n"

    #display_str += f"Accelerator Pedal Position, Percentage of Full Range: {EDR_decoded['Safety belt status, rear left passenger']}\n"
    #display_str += f"Brake Pedal Position: {EDR_decoded['Safety belt status, rear left passenger']}\n"


    datalist.insert(25,( f"-----------------------------UNSUPPORTED DATA--------------------------"))
    datalist.insert(26,( f"Engine throttle, %\n"))
    datalist.insert(27,( f"Multi-event crash, number of events\n"))
    datalist.insert(28,( f"Time from event 1 to 2\n"))
    datalist.insert(29,(f"Lateral acceleration (post-crash)\n"))
    datalist.insert(30,( f"Longitudinal acceleration (post-crash)\n"))
    datalist.insert(31,( f"Normal acceleration (post-crash)\n"))
    datalist.insert(32,(f"Vehicle roll angle\n"))
    datalist.insert(33,( f"Vehicle roll rate\n"))
    datalist.insert(34,( f"Seat track position switch, driver\n"))
    datalist.insert(35,( f"Seat track position switch, front passenger\n"))
    datalist.insert(36,( f"Occupant size classification, driver\n"))
    datalist.insert(37,( f"Occupant size classification, front passenger\n"))
    datalist.insert(38,( f"Tyre Pressure Monitoring System (TPMS) Warning Lamp Status\n"))
    datalist.insert(39,( f"Advanced emergency braking system status AEB\n"))
    EDR_buffer=bytearray(EDR_buffer)
    EDR_buffer.clear()


    return ([LongdV_buf,LateraldV_buf,Time,Vehicle_Speed,Brake_OnOff,Engine_Revolutions_Per_Minute,ABS_activity,Stability_control,Steering_Angle,Yaw_Rate,Traction_Control_Status,Cruise_Control_System,Longitudinal_acceleration_pre_crash,Lateral_acceleration_pre_crash,datalist])
LongdV_buf.clear()
LateraldV_buf.clear()
Time.clear()
Vehicle_Speed.clear()
Brake_OnOff.clear()
Engine_Revolutions_Per_Minute.clear()
ABS_activity.clear()
Stability_control.clear()
Steering_Angle.clear()
Yaw_Rate.clear()
Traction_Control_Status.clear()
Cruise_Control_System.clear()
Longitudinal_acceleration_pre_crash.clear()
Lateral_acceleration_pre_crash.clear()
datalist.clear()
EDR_postcrash_decoded.clear()
EDR_precrash_arr_decoded.clear()
EDR_decoded.clear()






