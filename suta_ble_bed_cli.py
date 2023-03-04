#!/usr/bin/env python3
#
# Filename: suta_ble_bed_cli.py
#
# Author: Simon Redman <simon@ergotech.com>
# File Created: 03.03.2023
# Description: Scuffed CLI to control your bed. Mostly for testing.
#

import asyncio
import argparse
from argparse import Namespace

import scanner as suta_scanner

async def worker(args: Namespace):
    devices = await suta_scanner.discover(args.MAC)

    for device in devices:
        pass

    print(devices)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="SUTA BLE Control",
        description="Control your Bluetooth-enabled SUTA (and other) bed.")

    parser.add_argument(
        "--MAC",
        required=False,
        help="MAC Address of your bed. May be ommitted, in which case we will attempt auto-discovery.")
    
    parser.add_argument(
        "-c", "--command",
        choices=["feet-up", "feet-down", "head-up", "head-down"],
        help="Action to perform")
    
    args = parser.parse_args()
    
    asyncio.run(worker(args))
    