#!/usr/bin/python3

import subprocess

# ups1 is the name of the ups in NUT
ups_name = "ups1"

p = subprocess.Popen(f"upsc {ups_name}".split(), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
lines = p.stdout.readlines()
print(lines)
