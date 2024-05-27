#import can
import array as arr
#import tabulate

EDR_buffer = arr.array('h', [0xfc,0xff,0xad,0xff,0xb0,0xff,0xbb,0xff,0xab,0xff,0xa2,0xff,0x75,0xff,0x38,0xff,0x36,0xff,0x2c,0xff,0x2d,0xff,0x65,0xff,0xb0,0xff,0xdf,0xff,0xf1,0xff,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x2c,0xff,0x10,0x27,0x0,0x0,0x0,0x3,0x4,0x5,0x6,0x7,0x8,0x9,0xa,0x1,0x1,0x1,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x7a,0xd,0x7a,0xd,0x0,0xdf,0xff,0xc,0x0,0x13,0x0,0xe,0x0,0x28,0x0,0x2f,0x0,0xfd,0xff,0x6,0x0,0xc,0x0,0x39,0x0,0x39,0x0,0x23,0x0,0xb,0x0,0x0,0x0,0xfd,0xff,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x39,0x0,0x10,0x27,0x25,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x7a,0xd,0x7a,0xd,0x7a,0xd,0x7a,0xd,0x7a,0xd,0x7a,0xd,0x0,0x0,0x0,0x0,0xb5,0xb5,0xb5,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xff,0x11,0x3f,0x0,0x3f,0x0,0x22,0xff,0xff,0xff,0xb,0x0,0x2,0x0,0x4,0x0,0x2,0x0,0x11,0x0,0x17,0x0,0x2,0x0,0x4,0x0,0x5,0x0,0x25,0x0,0x25,0x0,0xe,0x0,0x1,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x25,0x0,0x10,0x27,0xf0,0x3c,0x30,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0])
#EDR_buffer = arr.array('h', [])
EDR_postcrash_decoded = dict()
EDR_precrash_arr_decoded = dict()
EDR_decoded = dict()
wnum = 0


'''def can_send(request):
    try:
        bus.send(request)
        print(f"Message sent on {bus.channel_info}")
    except can.CanError:
        print("Message NOT sent")
    return'''

#datalen - 1 or 2 bytes
def get_precrash_data_arr(word_num, datalen, EDR_name):
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

def get_single_data(word_num, datalen, EDR_name):
    if datalen == 1:
        EDR_decoded.update([(EDR_name, EDR_buffer[word_num])])
    elif datalen == 2:
        EDR_decoded.update([(EDR_name, (EDR_buffer[word_num+1] << 8) + EDR_buffer[word_num])])

    word_num += datalen
    print(word_num)
    return word_num

def get_dV(word_num, EDR_name):
    EDR_dv_buf = []
    for i in range(word_num, word_num + 60, 2):
        EDR_dv_buf.append((EDR_buffer[i+1] << 8) + EDR_buffer[i])
    word_num += 60
    EDR_postcrash_decoded.update([(EDR_name, EDR_dv_buf)])
    print(word_num)
    return word_num

def get_val_from_2s_compl(val, len):
    #val = int(val, 16)
    if(val&(1 << (len - 1)) != 0):
        val = val - (1 << len)
    return val
    
def to_float_100_step(dV):
    return get_val_from_2s_compl(dV, 16)/100

def to_pos_float_100_step(val):
    return val/100

def to_uint_1_step(dV):
    return get_val_from_2s_compl(dV, 16)

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
        
def to_EDR_ext_state(UDS_val):
    match UDS_val:
        case 0:
            return "Not activated"
        case 1:
            return "Actively controlling"
        case 2:
            return "Commanded Off"
        case 3:
            return "Commanded On but not controlling"
        case 4:
            return "Fault"
        case 5:
            return "User-defined"
        case _:
            return ""
        
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
        case 0:
            return "No warning"
        case 1:
            return "Warning"
        
def to_EDR_rec_st(UDS_val):
    match UDS_val:
        case 0:
            return "Not recorded"
        case 1:
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
                      data=[0x03, 0x22, 0xFA, 0x11],
                      is_extended_id=False)

consequtive = can.Message(arbitration_id=0x752,
                          data=[0x30, 0x00, 0x00, 0x00],
                          is_extended_id=False)

#----------------------Get data from CAN-----------------------------'''
'''rec_msg = None
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
def Parse_EDR():
    #----------------------------MESSAGE HANDLING--------------------------
    wnum = get_dV(0, "Longitudinal Delta-V Value")
    wnum = get_single_data(wnum, 2, "Max Longitudinal Delta-V Value")
    wnum = get_single_data(wnum, 2, "Max Longitudinal Delta-V Record Time")

    wnum = get_precrash_data_arr(wnum, 1, "Vehicle Speed")
    wnum = get_precrash_data_arr(wnum, 1, "Brake On/Off")

    wnum = get_single_data(wnum, 1, "Driver SBS")
    wnum = get_single_data(wnum, 1, "Airbag warning lamp status")
    wnum = get_single_data(wnum, 2, "Deployment Time(Level1) of Driver Frontal Airbag")
    wnum = get_single_data(wnum, 2, "Deployment Time(Level1) of First RawPassenger Frontal Airbag")
    wnum = get_single_data(wnum, 1, "Event Data Record Complete Status")

    wnum = get_dV(wnum, "Lateral Delta-V Value")
    wnum = get_single_data(wnum, 2, "Max Lateral Delta-V Value")
    wnum = get_single_data(wnum, 2, "Max Lateral Delta-V Record Time")
    wnum = get_single_data(wnum, 2, "Time for maximum delta-V, resultant")

    wnum = get_precrash_data_arr(wnum, 2, "Engine Revolutions Per Minute")
    wnum = get_precrash_data_arr(wnum, 1, "ABS activity")
    wnum = get_precrash_data_arr(wnum, 1, "Stability control")
    wnum = get_precrash_data_arr(wnum, 2, "Steering Angle")

    wnum = get_single_data(wnum, 1, "Safety belt status, front passenger")
    wnum = get_single_data(wnum, 1, "Passenger air bag suppression status, front")

    wnum = get_single_data(wnum, 2, "Side air bag deployment, time to deploy, driver")
    wnum = get_single_data(wnum, 2, "Side air bag deployment, time to deploy, front passenger")
    wnum = get_single_data(wnum, 2, "Side curtain/tube air bag deployment, time to deploy, driver side")
    wnum = get_single_data(wnum, 2, "Side curtain/tube air bag deployment, time to deploy, passenger side")
    wnum = get_single_data(wnum, 2, "Pretensioner deployment, time to fire, driver")
    wnum = get_single_data(wnum, 2, "Pretensioner deployment, time to fire, front passenger")

    wnum = get_single_data(wnum, 1, "Safety belt status, rear right passenger")
    wnum = get_single_data(wnum, 1, "Safety belt status, rear centre passenger")
    wnum = get_single_data(wnum, 1, "Safety belt status, rear left passenger")
    wnum = get_single_data(wnum, 1, "Tyre Pressure Monitoring System (TPMS) Warning Lamp Status")

    wnum = get_precrash_data_arr(wnum, 1, "Yaw Rate")
    wnum = get_precrash_data_arr(wnum, 1, "Traction Control Status")
    wnum = get_precrash_data_arr(wnum, 1, "Automatic Emergency Braking System Status")
    wnum = get_precrash_data_arr(wnum, 1, "Cruise Control System")


        #new
    wnum = get_single_data(wnum, 1, "Accelerator Pedal Position, Percentage of Full Range")
    wnum = get_single_data(wnum, 1, "Brake Pedal Position")

    wnum = get_single_data(wnum, 2, "The PowerOn Cycle in Event")
    wnum = get_single_data(wnum, 2, "The PowerOn Cycle when Reading")
    wnum = get_single_data(wnum, 1, "VIN Code")
    wnum = get_single_data(wnum, 1, "ECU Hardware Number of EDR Data Record")
    wnum = get_single_data(wnum, 1, "ECU Serial Number of EDR Data Record")
    wnum = get_single_data(wnum, 1, "ECU Software Number of EDR Data Record")

    wnum = get_dV(wnum, "Squared Delta-V Value")
    wnum = get_single_data(wnum, 2, "Maximum Squared Sum Delta-V Record Value")
    wnum = get_single_data(wnum, 2, "Maximum Squared Sum Delta-V Record Time")
    wnum = get_single_data(wnum, 2, "Collision Event End")

    wnum = get_single_data(wnum, 1, "Year")
    wnum = get_single_data(wnum, 1, "Month")
    wnum = get_single_data(wnum, 1, "Date")
    wnum = get_single_data(wnum, 1, "Hour")
    wnum = get_single_data(wnum, 1, "Minutes")
    wnum = get_single_data(wnum, 1, "Seconds")
    wnum = get_single_data(wnum, 1, "Gear Postion")
    wnum = get_single_data(wnum, 1, "Steering Signal Switch Status")
    wnum = get_single_data(wnum, 1, "Synchronize Time before Event")

    #---------------------Filling display string--------------------
    display_str = f'''
    --------------------------CRASH DATA--------------------------
    Time, ms:   Long dV, km/h:  Lateral dV, km/h:  Squared dV, km/h
    '''
    for i in range(10, 310, 10):
       display_str += f"{i}          {to_float_100_step(EDR_postcrash_decoded['Longitudinal Delta-V Value'][int(i/10) - 1])}"
       display_str += f"          {to_float_100_step(EDR_postcrash_decoded['Lateral Delta-V Value'][int(i/10) - 1])}"
       display_str += f"          {to_float_100_step(EDR_postcrash_decoded['Squared Delta-V Value'][int(i/10) - 1])}\n"

    display_str += f"Max Longitudinal Delta-V Value: {to_float_100_step(EDR_decoded['Max Longitudinal Delta-V Value'])}\n"
    display_str += f"Max Longitudinal Delta-V Record Time: {to_pos_float_100_step(EDR_decoded['Max Longitudinal Delta-V Record Time'])}\n"
    display_str += f"Max Lateral Delta-V Value: {to_float_100_step(EDR_decoded['Max Lateral Delta-V Value'])}\n"
    display_str += f"Max Lateral Delta-V Record Time: {to_pos_float_100_step(EDR_decoded['Max Lateral Delta-V Record Time'])}\n"
    display_str += f"Maximum Squared Sum Delta-V Record Value: {to_float_100_step(EDR_decoded['Maximum Squared Sum Delta-V Record Value'])}\n"
    display_str += f"Maximum Squared Sum Delta-V Record Time: {to_pos_float_100_step(EDR_decoded['Maximum Squared Sum Delta-V Record Time'])}\n"
    display_str += f"Time for maximum delta-V, resultant: {to_pos_float_100_step(EDR_decoded['Time for maximum delta-V, resultant'])}\n"
    display_str += f"Collision Event End: {to_pos_float_100_step(EDR_decoded['Collision Event End'])}\n"



    display_str += f'''
    -----------------------------PRECRASH DATA ARRAY--------------------------
    Time, s:         Vehicle Speed       Brake On/Off     Engine RPM    ABS activity    Stability control   Steering Angle
    '''
    for i in range(11):
        display_str += f"{(i/2)-5.0}                 {EDR_precrash_arr_decoded['Vehicle Speed'][i]}"
        display_str += f"               {to_brake_state(EDR_precrash_arr_decoded['Brake On/Off'][i])}"
        display_str += f"               {to_eng_rpm(EDR_precrash_arr_decoded['Engine Revolutions Per Minute'][i])}"
        display_str += f"              {to_EDR_state(EDR_precrash_arr_decoded['ABS activity'][i])}"
        display_str += f"       {to_EDR_state(EDR_precrash_arr_decoded['Stability control'][i])}"
        display_str += f"           {to_float_100_step(EDR_precrash_arr_decoded['Steering Angle'][i])}"
        display_str += f"           {to_uint_1_step(EDR_precrash_arr_decoded['Yaw Rate'][i])}"
        display_str += f"           {to_EDR_ext_state(EDR_precrash_arr_decoded['Traction Control Status'][i])}"
        display_str += f"           {to_EDR_ext_state(EDR_precrash_arr_decoded['Automatic Emergency Braking System Status'][i])}"
        display_str += f"           {to_EDR_ext_state(EDR_precrash_arr_decoded['Cruise Control System'][i])}\n\n"

    display_str += f'''
    -----------------------------SINGLE DATA--------------------------
    '''
    display_str += f"Driver Seat Belt Status: {to_SBS(EDR_decoded['Driver SBS'])}\n"
    display_str += f"Airbag warning lamp: {to_lamp_state(EDR_decoded['Airbag warning lamp status'])}\n"
    display_str += f"Deployment Time(Level1) of Driver Frontal Airbag: {to_pos_float_100_step(EDR_decoded['Deployment Time(Level1) of Driver Frontal Airbag'])}\n"
    display_str += f"Deployment Time(Level1) of First RawPassenger Frontal Airbag: {to_pos_float_100_step(EDR_decoded['Deployment Time(Level1) of First RawPassenger Frontal Airbag'])}\n"
    display_str += f"Event Data Record Complete Status: {to_EDR_rec_st(EDR_decoded['Event Data Record Complete Status'])}\n"
    display_str += f"Safety belt status, front passenger: {to_SBS(EDR_decoded['Safety belt status, front passenger'])}\n"
    display_str += f"Passenger air bag suppression status, front: {to_ingibit_st(EDR_decoded['Passenger air bag suppression status, front'])}\n"
    display_str += f"Side air bag deployment, time to deploy, driver: {to_pos_float_100_step(EDR_decoded['Side air bag deployment, time to deploy, driver'])}\n"
    display_str += f"Side air bag deployment, time to deploy, front passenger: {to_pos_float_100_step(EDR_decoded['Side air bag deployment, time to deploy, front passenger'])}\n"
    display_str += f"Side curtain/tube air bag deployment, time to deploy, driver side: {to_pos_float_100_step(EDR_decoded['Side curtain/tube air bag deployment, time to deploy, driver side'])}\n"
    display_str += f"Side curtain/tube air bag deployment, time to deploy, passenger side: {to_pos_float_100_step(EDR_decoded['Side curtain/tube air bag deployment, time to deploy, passenger side'])}\n"
    display_str += f"Pretensioner deployment, time to fire, driver: {to_pos_float_100_step(EDR_decoded['Pretensioner deployment, time to fire, driver'])}\n"
    display_str += f"Pretensioner deployment, time to fire, front passenger: {to_pos_float_100_step(EDR_decoded['Pretensioner deployment, time to fire, front passenger'])}\n"
    display_str += f"Safety belt status, rear right passenger: {to_SBS(EDR_decoded['Safety belt status, rear right passenger'])}\n"
    display_str += f"Safety belt status, rear centre passenger: {to_SBS(EDR_decoded['Safety belt status, rear centre passenger'])}\n"
    display_str += f"Safety belt status, rear left passenger: {to_SBS(EDR_decoded['Safety belt status, rear left passenger'])}\n"
    display_str += f"Tyre Pressure Monitoring System (TPMS) Warning Lamp Status: {to_TPMS_st(EDR_decoded['Safety belt status, rear left passenger'])}\n"

    #display_str += f"Accelerator Pedal Position, Percentage of Full Range: {EDR_decoded['Safety belt status, rear left passenger']}\n"
    #display_str += f"Brake Pedal Position: {EDR_decoded['Safety belt status, rear left passenger']}\n"
    display_str += f"The PowerOn Cycle in Event: {to_uint_1_step(EDR_decoded['The PowerOn Cycle in Event'])}\n"
    display_str += f"The PowerOn Cycle when Reading: {to_uint_1_step(EDR_decoded['The PowerOn Cycle when Reading'])}\n"

    display_str += f"Year: {EDR_decoded['Year']}\n"
    display_str += f"Month: {to_uint_1_step(EDR_decoded['Month'])}\n"
    display_str += f"Date: {to_uint_1_step(EDR_decoded['Date'])}\n"
    display_str += f"Hour: {to_uint_1_step(EDR_decoded['Hour'])}\n"
    display_str += f"Minutes: {to_uint_1_step(EDR_decoded['Minutes'])}\n"
    display_str += f"Seconds: {to_uint_1_step(EDR_decoded['Seconds'])}\n"



    print(display_str)
    return display_str
#print(EDR_postcrash_decoded)
#print(EDR_precrash_arr_decoded)
#print(EDR_decoded)

#bus.shutdown()





