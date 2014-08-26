#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

"""
Colorful output
"""

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"

def head(msg):
    print(HEADER + msg + ENDC)

def info(msg):
    print(msg)

def infog(msg):
    print(OKGREEN + msg + ENDC)

def infob(msg):
    print(OKBLUE + msg + ENDC)

def warn(msg):
    print(WARNING + msg + ENDC)

def err(msg):
    print(FAIL + msg + ENDC)

"""
Welcome message
"""

head("Welcome to the Wahlque Complete, a citizen science experiement")

"""
Check python version
"""

info("checking python version...")

req_version = (3,4)
cur_version = sys.version_info

if cur_version < req_version:
    err("Your Python interpreter is too old. Please consider upgrading.")
    sys.exit(0)

"""
Check virtual enviroment
"""


