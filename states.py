import enum
class AIRBAGCrash(enum.IntEnum):
    Launch_Medium_Crash_Actions=0x45ba
    Launch_Heavy_Crash_Actions =0x54ab
    bit0_medium=0x45
    bit1_medium=0xba
    bit0_heavy=0x54
    bit1_heavy=0xab
class CrashDetected(enum.IntEnum):
    no_crash_detected=0b00000000
    crash_detected=0b10000000
class CrashDetectionOutOfOrder(enum.IntEnum):
    no_Crash_Detection_Out_Of_Order=0b00000000
    Crash_Detection_Out_Of_Order=0b01000000
class DriverSafetyBeltState(enum.IntEnum):
    shift=4
    SB_not_monitored = 0b00000000
    SB_unfastened = 0b00010000
    SB_fastened = 0b00100000
    Unavalible = 0b00110000#
class FrontPassengerSafetyBeltState(enum.IntEnum):
    shift=2
    SB_not_monitored = 0b00000000
    SB_unfastened = 0b00000100
    SB_fastened = 0b00001000
    Unavalible = 0b00001100#
class SecondRowCenterSafetyBeltState(enum.IntEnum):
    shift=1
    SB_not_monitored=0b00000000
    SB_unfastened=0b00000010
    SB_fastened=0b00000100
    Unavalible=0b00000110
class SecondRowLeftSafetyBeltState(enum.IntEnum):
    shift=7
    SB_not_monitored=0b00000000
    SB_unfastened_MSB=0b00000000
    SB_unfastened_LSB=0b10000000
    SB_fastened_MSB  =0b00000001
    SB_fastened_LSB=0b00000000
    Unavalible_MSB=0b10000001
    Unavalible_LSB=0b10000000
class SecondRowRightSafetyBeltState(enum.IntEnum):
    shift=5
    SB_not_monitored=0b00000000
    SB_unfastened=0b00100000
    SB_fastened=0b01000000
    Unavalible=0b01100000
class DriverSafetyBeltReminder(enum.IntEnum):
    shift=6
    No_Warning=0b00000000
    Warning_level_1=0b01000000
    Warning_level_2=0b10000000
    Not_used=0b11000000
class FrontPassengerSafetyBeltReminder(enum.IntEnum):
    shift=4
    No_Warning=0b00000000
    Warning_level_1=0b00010000
    Warning_level_2=0b00100000
    Not_used=0b00110000
class SecondRowRightSafetyBeltWarning(enum.IntEnum):
    shift=4
    No_Warning=0b00000000
    Warning_level_1=0b00010000
    Warning_level_2=0b00100000
    Not_used=0b00110000
class SecondRowCenterSafetyBeltWarning(enum.IntEnum):
    No_Warning=0b00000000
    Warning_level_1=0b00000001
    Warning_level_2=0b00000010
    Not_used=0b00000011
class SecondRowLeftSafetyBeltWarning(enum.IntEnum):
    shift=6
    No_Warning=0b00000000
    Warning_level_1=0b01000000
    Warning_level_2=0b10000000
    Not_used=0b11000000

class ValidAIRBAGInformation(enum.IntEnum):
    no_valid_AIRBAG_Information=0b00000000
    Valid_AIRBAG_Information=0b00001000
class DTC(enum.IntEnum):

    Vehicle_option_fault=0x900100
    VIN_absence=0x901800
    Internal_mode_fault=0x901204
    WatchDog_Continues_Fault=0x905647
    Crash_stored_in_memory=0x901400
    Crash_recorded_in_frontal_airbag_only=0x905000
    Crash_recorded_in_Driver_side_airbag_only=0x905100
    Crash_recorded_in_Passenger_side_airbag_only=0x905200
    Crash_recorded_in_Belt_pretensioner_only=0x905300
    Crash_recorded_in_Rear=0x905400
    Vbatt_too_high=0x909817
    Vbatt_too_low=0x909816

    Front_airbag_driver_resistance_too_high=0x90211B
    Front_airbag_driver_resistance_too_low=0x90211A
    Front_airbag_driver_short_to_GND=0x902114
    Front_airbag_driver_short_to_Vbatt=0x902112

    Front_airbag_passenger_resistance_too_high = 0x90311B
    Front_airbag_passenger_resistance_too_low = 0x90311A
    Front_airbag_passenger_short_to_GND = 0x903114
    Front_airbag_passenger_short_to_Vbatt = 0x903112

    Pretensioner_Driver_resistance_too_high = 0x902A1B
    Pretensioner_Driver_resistance_too_low = 0x902A1A
    Pretensioner_Driver_short_to_GND = 0x902A14
    Pretensioner_Driver_short_to_Vbatt = 0x902A12

    Pretensioner_Passenger_resistance_too_high = 0x903A1B
    Pretensioner_Passenger_resistance_too_low = 0x903A1A
    Pretensioner_Passenger_short_to_GND = 0x903A14
    Pretensioner_Passenger_short_to_Vbatt = 0x903A12

    Side_airbag_driver_resistance_too_high = 0x90411B
    Side_airbag_driver_resistance_too_low = 0x90411A
    Side_airbag_driver_short_to_GND = 0x904114
    Side_airbag_driver_short_to_Vbatt = 0x904112

    Side_airbag_passenger_resistance_too_high = 0x90451B
    Side_airbag_passenger_resistance_too_low = 0x90451A
    Side_airbag_passenger_short_to_GND = 0x904514
    Side_airbag_passenger_short_to_Vbatt = 0x904512

    Curtain_airbag_driver_resistance_too_high = 0x90911B
    Curtain_airbag_driver_resistance_too_low = 0x90911A
    Curtain_airbag_driver_short_to_GND = 0x909114
    Curtain_airbag_driver_short_to_Vbatt = 0x909112

    Curtain_airbag_passenger_resistance_too_high = 0x90921B
    Curtain_airbag_passenger_resistance_too_low = 0x90921A
    Curtain_airbag_passenger_short_to_GND = 0x909214
    Curtain_airbag_passenger_short_to_Vbatt = 0x909212

    Driver_side_impact_sensor_wrong_characreristics = 0x907100
    Driver_side_impact_sensor_short_to_GND = 0x907111
    Driver_side_impact_sensor_short_to_battery = 0x907114
    Driver_side_impact_sensor_communication_error = 0x907187

    Passenger_side_impact_sensor_wrong_characreristics = 0x908100
    Passenger_side_impact_sensor_short_to_GND = 0x908111
    Passenger_side_impact_sensor_short_to_battery = 0x908114
    Passenger_side_impact_sensor_communication_error = 0x908187

    Driver_door_pressure_sensor_wrong_characreristics = 0x909100
    Driver_door_pressure_sensor_short_to_GND = 0x909111
    Driver_door_pressure_sensor_short_to_battery = 0x909114
    Driver_door_pressure_sensor_communication_error = 0x909187

    Passenger_door_pressure_sensor_wrong_characreristics = 0x90A100
    Passenger_door_pressure_sensor_short_to_GND = 0x90A111
    Passenger_door_pressure_sensor_short_to_battery = 0x90A114
    Passenger_door_pressure_sensor_communication_error = 0x90A187

    Passenger_Airbag_Cutoff_switch_short_to_GND=0x910314
    Passenger_Airbag_Cutoff_switch_short_to_Vbatt=0x910312

    Passenger_presence_sensor_short_to_GND=0x910514
    Passenger_presence_sensor_short_to_Vbatt=0x910512

    CAN_Bus_off=0xC07388
    Lost_communication_with_ABS_ESC=0xC12187
    Lost_communication_with_uBCM=0xC14087
    Lost_communication_with_Cluster=0xC15587




