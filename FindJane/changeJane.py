#!/usr/bin/env python3

import sys
import subprocess

list = sys.argv[1]

with open(list) as file:
    for line in file.readlines():
        line = line.strip()
        new = line.replace("jane", "jdoe")
        subprocess.run(['mv', line, new])
