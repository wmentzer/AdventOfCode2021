#!/usr/bin/env python3
import subprocess
import os

daySelector = str(input("\033[34;1m[+]\033[0m Please enter the day you would line to run: "))

print("\n\033[34;1m[+]\033[0m Starting subprocesses for Day {}...".format(daySelector))

filepath1 = str("Day{}/Part1/main.py".format(daySelector))
filepath2 = str("Day{}/Part2/main.py".format(daySelector))

if os.path.exists(filepath1):
  print("\033[34;1m[+]\033[0m Running Day {} Part 1 subprocess...\n".format(daySelector))

  st = os.stat(filepath1)
  os.chmod(filepath1, st.st_mode | 0o0111)
  subprocess.call(filepath1, shell=True)
else:
  print("\n\033[34;1m[+]\033[0m Could not start Day {} subprocess... \033[31;1mFile doesn't exist!\033[0m".format(daySelector))
  print("\033[34;1m[+]\033[0m Exiting...")

if os.path.exists(filepath2):
  print("\n\033[34;1m[+]\033[0m Day{} Part 1 subprocess completed successfully...\n\033[34;1m[+]\033[0m Starting Day{} Part 2...\n".format(daySelector, daySelector))

  st = os.stat(filepath2)
  os.chmod(filepath2, st.st_mode | 0o0111)
  subprocess.call(filepath2, shell=True)

  print("\n\033[34;1m[+]\033[0m Day {} subprocess complete...\n\033[34;1m[+]\033[0m Exiting...".format(daySelector))