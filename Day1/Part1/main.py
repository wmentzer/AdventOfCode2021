#!/usr/bin/env python3

def main():
  print("**********    DAY 1 PART 1    **********\n")
  lines = []

  prev = None
  count = 0

  with open("./Day1/Part1/input.txt", 'r') as f:
    lines = f.read().splitlines()

  prev = lines[0]

  for x in lines:
    if int(x) > int(prev):
      count += 1
      prev = x
    else:
      prev = x

  print("The distance increased a total of {} times".format(count))

  print("\n**********    FINISHED    **********")


if __name__ == "__main__":
  main()