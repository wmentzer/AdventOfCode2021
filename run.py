#!/usr/bin/env python3
import subprocess

daySelector = str(input("Please enter the day you would line to run: "))

print("\nRunning main.py for Day {}...\n".format(daySelector))

filepath1 = str("Day{}/Part1/main.py".format(daySelector))
filepath2 = str("Day{}/Part2/main.py".format(daySelector))

subprocess.call(filepath1, shell=True)

print("\nDay{} Part 1 subprocess completed successfully...\nStarting Day{} Part 2...\n".format(daySelector, daySelector))

subprocess.call(filepath2, shell=True)