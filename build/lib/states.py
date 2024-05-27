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
    crash_detected=0b00000001
class CrashDetectionOutOfOrder(enum.IntEnum):
    no_Crash_Detection_Out_Of_Order=0b00000000
    Crash_Detection_Out_Of_Order=0b00000010
class DriverSafetyBeltState(enum.IntEnum):
    shift=2
    SB_not_monitored = 0b00000000
    SB_unfastened = 0b00000100
    SB_fastened = 0b00001000
    Unavalible = 0b00001100#
class FrontPassengerSafetyBeltState(enum.IntEnum):
    shift=4
    SB_not_monitored = 0b00000000
    SB_unfastened = 0b00010000
    SB_fastened = 0b00100000
    Unavalible = 0b00110000#
class SecondRowCenterSafetyBeltState(enum.IntEnum):
    shift=5
    SB_not_monitored=0b00000000
    SB_unfastened=0b00100000
    SB_fastened=0b01000000
    Unavalible=0b01100000
class SecondRowLeftSafetyBeltState(enum.IntEnum):
    shift=6
    SB_not_monitored=0b00000000
    SB_unfastened_B2=0b00000000
    SB_unfastened_B3=0b10000000
    SB_fastened_B2  =0b10000000
    SB_fastened_B3=0b00000000
    Unavalible_B2=0b10000000
    Unavalible_B3=0b00000001
class SecondRowRightSafetyBeltState(enum.IntEnum):
    shift=1
    SB_not_monitored=0b00000000
    SB_unfastened=0b00000010
    SB_fastened=0b00000100
    Unavalible=0b00000110
class DriverSafetyBeltReminder(enum.IntEnum):
    No_Warning=0b00000000
    Warning_level_1=0b00000001
    Warning_level_2=0b00000010
    Not_used=0b00000011
class FrontPassengerSafetyBeltReminder(enum.IntEnum):
    shift=2
    No_Warning=0b00000000
    Warning_level_1=0b00000100
    Warning_level_2=0b00001000
    Not_used=0b00001100
class SecondRowRightSafetyBeltWarning(enum.IntEnum):
    shift=2
    No_Warning=0b00000000
    Warning_level_1=0b00000100
    Warning_level_2=0b00001000
    Not_used=0b00001100
class SecondRowCenterSafetyBeltWarning(enum.IntEnum):
    shift=6
    No_Warning=0b00000000
    Warning_level_1=0b01000000
    Warning_level_2=0b10000000
    Not_used=0b11000000
class SecondRowLeftSafetyBeltWarning(enum.IntEnum):
    No_Warning=0b00000000
    Warning_level_1=0b00000001
    Warning_level_2=0b00000010
    Not_used=0b00000011

class ValidAIRBAGInformation(enum.IntEnum):
    no_valid_AIRBAG_Information=0b00000000
    Valid_AIRBAG_Information=0b00010000

