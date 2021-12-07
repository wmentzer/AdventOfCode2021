#!/usr/bin/env python3

def main():
  inputList = []
  x, y = 0, 0

  with open("./Day2/Part1/input.txt", 'r') as f:
    inputList = f.read().splitlines()
    
  for x in inputList:
    dir, num = x.split()

    if (dir == "forward"):
      x += num
    elif (dir == "up"):
      y += num
    elif (dir == "down"):
      y -= num

  print(x * y)



if __name__ == "__main__":
  main()