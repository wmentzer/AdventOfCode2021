#!/usr/bin/env python3

def main():
  inputList = []
  pos = [0,0]
  aim = 0

  with open("./Day2/Part1/input.txt", 'r') as f:
    inputList = f.read().splitlines()
    
  for x in inputList:
    dir, num = x.split()

    if (dir == "forward"):
      pos[0] += int(num)
      pos[1] += int(num) * aim
    elif (dir == "up"):
      aim -= int(num)
    elif (dir == "down"):
      aim += int(num)

  answer = pos[0] * pos[1]

  print("The answer to Day 2 Part 1 is \033[32;1m{}\033[0m".format(answer))

if __name__ == "__main__":
  main()