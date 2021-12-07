#!/usr/bin/env python3

def main():
  inputList = []
  gamma = ''
  epsilon = ''
  col, one, zero = 0, 0, 0

  with open("./Day3/Part1/input.txt", 'r') as f:
    inputList = f.read().split()

  while col < 12:
    for x in inputList:
      if (x[col] == "1"):
        one += 1
      else:
        zero += 1
    if one > zero:
      gamma += '1'
    else:
      gamma += '0'
    one, zero = 0, 0
    col += 1

  for x in gamma:
    if x == '1':
      epsilon += '0'
    else:
      epsilon += '1'

  gamma = int(gamma, 2)
  epsilon = int(epsilon, 2)

  answer = (gamma * epsilon)

  print("The answer to Day 3 Part 1 is \033[32;1m{}\033[0m".format(answer))

if __name__ == "__main__":
  main()