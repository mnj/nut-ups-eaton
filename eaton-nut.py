#!/usr/bin/python3

import sys
import subprocess

# ups1 is the name of the ups in NUT
ups_name = "ups1"

def get_ups_status_variables():
    p = subprocess.Popen(f"upsc {ups_name}".split(), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    upsc_lines = p.stdout.readlines()

    variables = {}

    for line in upsc_lines:
        line = line.rstrip('\n')
        name, value = line.split(': ')
        variables[name] = value

    return variables

def get_values():
    upsc_variables = get_ups_status_variables()

    for key in sorted(upsc_variables):
        print(upsc_variables[key])

def get_names():
    upsc_variables = get_ups_status_variables()

    for key in sorted(upsc_variables):
        print(key)

def main():
    if "names" in sys.argv:
        get_names()
    elif "values" in sys.argv:
        get_values()

if __name__ == "__main__":
    main()
