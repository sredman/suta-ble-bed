#!/usr/bin/env python3
#
# Filename: suta_ble_consts.py
#
# Author: Simon Redman <simon@ergotech.com>
# File Created: 03.03.2023
# Description: Constants required for BLE communication with the SUTA beds
#

from enum import IntEnum
import platform

# Normally, one would identify a BLE devuce by its UUID
# As far as I can tell (I know nothing about BLE),
# the bed does not advertise a UUID.
# Use the name instead.
BED_LOCAL_NAME = "QRRM104150"

class BedCharacteristic(IntEnum):
    SERVICE = 0x1801,

class BedCommands(IntEnum):
    '''
    These were reverse engineered and documented in
    '''
    LIGHT = 0x6e01003cab
    ZERO_GRAVITY = 0x6e010045b4
    FLAT = 0x6e010031a0
    HEAD_UP = 0x6e01002493
    HEAD_DOWN = 0x6e01002594
    FEED_UP = 0x6e01002695
    FEET_DOWN = 0x6e01002796

IS_LINUX = platform.system() == "Linux"
