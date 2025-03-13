## \file motoron_protocol.py
##
## This file defines the arbitrary constants needed to communicate with a
## Motoron.  We do not recommend importing this package directly because
## all of the constants defined in it are available through the `motoron`
## package.
##
## \cond

CMD_GET_FIRMWARE_VERSION = 0x87
CMD_SET_PROTOCOL_OPTIONS = 0x8B
CMD_READ_EEPROM = 0x93
CMD_WRITE_EEPROM = 0x95
CMD_REINITIALIZE = 0x96
CMD_RESET = 0x99
CMD_GET_VARIABLES = 0x9A
CMD_SET_VARIABLE = 0x9C
CMD_COAST_NOW = 0xA5
CMD_CLEAR_MOTOR_FAULT = 0xA6
CMD_CLEAR_LATCHED_STATUS_FLAGS = 0xA9
CMD_SET_LATCHED_STATUS_FLAGS = 0xAC
CMD_SET_BRAKING = 0xB1
CMD_SET_BRAKING_NOW = 0xB2
CMD_SET_SPEED = 0xD1
CMD_SET_SPEED_NOW = 0xD2
CMD_SET_BUFFERED_SPEED = 0xD4
CMD_SET_ALL_SPEEDS = 0xE1
CMD_SET_ALL_SPEEDS_NOW = 0xE2
CMD_SET_ALL_BUFFERED_SPEEDS = 0xE4
CMD_SET_ALL_SPEEDS_USING_BUFFERS = 0xF0
CMD_SET_ALL_SPEEDS_NOW_USING_BUFFERS = 0xF3
CMD_RESET_COMMAND_TIMEOUT = 0xF5
CMD_MULTI_DEVICE_ERROR_CHECK = 0xF9
CMD_MULTI_DEVICE_WRITE = 0xFA

SETTING_FACTORY_RESET_CODE = 0
SETTING_DEVICE_NUMBER = 1
SETTING_ALTERNATIVE_DEVICE_NUMBER = 3
SETTING_COMMUNICATION_OPTIONS = 5
SETTING_BAUD_DIVIDER = 6
SETTING_RESPONSE_DELAY = 8

VAR_PROTOCOL_OPTIONS = 0
VAR_STATUS_FLAGS = 1
VAR_VIN_VOLTAGE = 3
VAR_COMMAND_TIMEOUT = 5
VAR_ERROR_RESPONSE = 7
VAR_ERROR_MASK = 8
VAR_JUMPER_STATE = 10
VAR_UART_FAULTS = 11

MVAR_PWM_MODE = 1
MVAR_TARGET_SPEED = 2
MVAR_TARGET_BRAKE_AMOUNT = 4
MVAR_CURRENT_SPEED = 6
MVAR_BUFFERED_SPEED = 8
MVAR_MAX_ACCEL_FORWARD = 10
MVAR_MAX_ACCEL_REVERSE = 12
MVAR_MAX_DECEL_FORWARD = 14
MVAR_MAX_DECEL_REVERSE = 16
MVAR_STARTING_SPEED_FORWARD = 18
MVAR_STARTING_SPEED_REVERSE = 20
MVAR_DIRECTION_CHANGE_DELAY_FORWARD = 22
MVAR_DIRECTION_CHANGE_DELAY_REVERSE = 23
MVAR_MAX_DECEL_TMP = 24
MVAR_CURRENT_LIMIT = 26
MVAR_CURRENT_SENSE_RAW = 28
MVAR_CURRENT_SENSE_SPEED = 30
MVAR_CURRENT_SENSE_PROCESSED = 32
MVAR_CURRENT_SENSE_OFFSET = 34
MVAR_CURRENT_SENSE_MINIMUM_DIVISOR = 35

PROTOCOL_OPTION_CRC_FOR_COMMANDS = 0
PROTOCOL_OPTION_CRC_FOR_RESPONSES = 1
PROTOCOL_OPTION_I2C_GENERAL_CALL = 2

COMMUNICATION_OPTION_7BIT_RESPONSES = 0
COMMUNICATION_OPTION_14BIT_DEVICE_NUMBER = 1
COMMUNICATION_OPTION_ERR_IS_DE = 2

STATUS_FLAG_PROTOCOL_ERROR = 0
STATUS_FLAG_CRC_ERROR = 1
STATUS_FLAG_COMMAND_TIMEOUT_LATCHED = 2
STATUS_FLAG_MOTOR_FAULT_LATCHED = 3
STATUS_FLAG_NO_POWER_LATCHED = 4
STATUS_FLAG_UART_ERROR = 5
STATUS_FLAG_RESET = 9
STATUS_FLAG_COMMAND_TIMEOUT = 10
STATUS_FLAG_MOTOR_FAULTING = 11
STATUS_FLAG_NO_POWER = 12
STATUS_FLAG_ERROR_ACTIVE = 13
STATUS_FLAG_MOTOR_OUTPUT_ENABLED = 14
STATUS_FLAG_MOTOR_DRIVING = 15

UART_FAULT_FRAMING = 0
UART_FAULT_NOISE = 1
UART_FAULT_HARDWARE_OVERRUN = 2
UART_FAULT_SOFTWARE_OVERRUN = 3

ERROR_RESPONSE_COAST = 0
ERROR_RESPONSE_BRAKE = 1
ERROR_RESPONSE_COAST_NOW = 2
ERROR_RESPONSE_BRAKE_NOW = 3

PWM_MODE_DEFAULT = 0
PWM_MODE_1_KHZ = 1
PWM_MODE_2_KHZ = 2
PWM_MODE_4_KHZ = 3
PWM_MODE_5_KHZ = 4
PWM_MODE_10_KHZ = 5
PWM_MODE_20_KHZ = 6
PWM_MODE_40_KHZ = 7
PWM_MODE_80_KHZ = 8

JMP1_INSTALLED = 0
JMP1_NOT_INSTALLED = 1

CLEAR_MOTOR_FAULT_UNCONDITIONAL = 0

ERROR_CHECK_CONTINUE = 0x3C
ERROR_CHECK_DONE = 0x00

MAX_SPEED = 800
MAX_ACCEL = 6400
MAX_DIRECTION_CHANGE_DELAY = 250

LATCHED_STATUS_FLAGS = 0x03FF
MAX_ERROR_MASK = 0x07FF

MAX_COMMAND_TIMEOUT = 16250

MIN_BAUD_RATE = 245
MAX_BAUD_RATE = 1000000

CRC_TABLE = [
  0x00, 0x41, 0x13, 0x52, 0x26, 0x67, 0x35, 0x74,
  0x4c, 0x0d, 0x5f, 0x1e, 0x6a, 0x2b, 0x79, 0x38,
  0x09, 0x48, 0x1a, 0x5b, 0x2f, 0x6e, 0x3c, 0x7d,
  0x45, 0x04, 0x56, 0x17, 0x63, 0x22, 0x70, 0x31,
  0x12, 0x53, 0x01, 0x40, 0x34, 0x75, 0x27, 0x66,
  0x5e, 0x1f, 0x4d, 0x0c, 0x78, 0x39, 0x6b, 0x2a,
  0x1b, 0x5a, 0x08, 0x49, 0x3d, 0x7c, 0x2e, 0x6f,
  0x57, 0x16, 0x44, 0x05, 0x71, 0x30, 0x62, 0x23,
  0x24, 0x65, 0x37, 0x76, 0x02, 0x43, 0x11, 0x50,
  0x68, 0x29, 0x7b, 0x3a, 0x4e, 0x0f, 0x5d, 0x1c,
  0x2d, 0x6c, 0x3e, 0x7f, 0x0b, 0x4a, 0x18, 0x59,
  0x61, 0x20, 0x72, 0x33, 0x47, 0x06, 0x54, 0x15,
  0x36, 0x77, 0x25, 0x64, 0x10, 0x51, 0x03, 0x42,
  0x7a, 0x3b, 0x69, 0x28, 0x5c, 0x1d, 0x4f, 0x0e,
  0x3f, 0x7e, 0x2c, 0x6d, 0x19, 0x58, 0x0a, 0x4b,
  0x73, 0x32, 0x60, 0x21, 0x55, 0x14, 0x46, 0x07,
  0x48, 0x09, 0x5b, 0x1a, 0x6e, 0x2f, 0x7d, 0x3c,
  0x04, 0x45, 0x17, 0x56, 0x22, 0x63, 0x31, 0x70,
  0x41, 0x00, 0x52, 0x13, 0x67, 0x26, 0x74, 0x35,
  0x0d, 0x4c, 0x1e, 0x5f, 0x2b, 0x6a, 0x38, 0x79,
  0x5a, 0x1b, 0x49, 0x08, 0x7c, 0x3d, 0x6f, 0x2e,
  0x16, 0x57, 0x05, 0x44, 0x30, 0x71, 0x23, 0x62,
  0x53, 0x12, 0x40, 0x01, 0x75, 0x34, 0x66, 0x27,
  0x1f, 0x5e, 0x0c, 0x4d, 0x39, 0x78, 0x2a, 0x6b,
  0x6c, 0x2d, 0x7f, 0x3e, 0x4a, 0x0b, 0x59, 0x18,
  0x20, 0x61, 0x33, 0x72, 0x06, 0x47, 0x15, 0x54,
  0x65, 0x24, 0x76, 0x37, 0x43, 0x02, 0x50, 0x11,
  0x29, 0x68, 0x3a, 0x7b, 0x0f, 0x4e, 0x1c, 0x5d,
  0x7e, 0x3f, 0x6d, 0x2c, 0x58, 0x19, 0x4b, 0x0a,
  0x32, 0x73, 0x21, 0x60, 0x14, 0x55, 0x07, 0x46,
  0x77, 0x36, 0x64, 0x25, 0x51, 0x10, 0x42, 0x03,
  0x3b, 0x7a, 0x28, 0x69, 0x1d, 0x5c, 0x0e, 0x4f,
]

## \endcond

def calculate_crc(buffer):
  """
  This method calculates the 7-bit CRC needed for a Motoron
  command or response.  Most users will not need to use this, since most
  methods in this library automatically append a CRC byte or check
  received CRC bytes when appropriate.
  """
  crc = 0
  for byte in buffer:
    crc = CRC_TABLE[crc ^ byte]
  return crc

