#!/usr/bin/env python3

def main():
  print("**********    DAY 1 PART 2    **********\n")
  lines = []
  count = 0

  with open("./Day1/Part2/input.txt", 'r') as f:
    lines = f.read().splitlines()

  back3, back2, back1 = lines[0], lines[1], lines[2]

  for x in range(len(lines)):
    if x <= 2:
      continue
    if (int(back3) + int(back2) + int(back1)) < (int(back2) + int(back1) + int(lines[x])):
      count += 1
    back3, back2, back1 = back2, back1, lines[x]

  print("The distance increased a total of \033[32;1m{}\033[0m times".format(count))

  print("\n**********    FINISHED    **********")


if __name__ == "__main__":
  main()