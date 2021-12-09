#!/usr/bin/env python3

def getO2Rating(arr = []):
  col, one, zero = 0, 0, 0

  while len(arr) > 1 and col < 12:
    for x in arr:
      if(x[col] == '1'):
        one += 1
      else:
        zero += 1

    if(one > zero):
      for x in list(arr):
        if x[col] == '0':
          arr.remove(x)
    elif(one < zero):
      for x in list(arr):
        if x[col] == '1':
          arr.remove(x)
    else:
      for x in list(arr):
        if x[col] == '0':
          arr.remove(x)
    col += 1
    one, zero = 0, 0

  return arr[0]

def getCO2Rating(arr = []):
  col, one, zero = 0, 0, 0

  while len(arr) > 1 and col < 12:
    for x in arr:
      if(x[col] == '1'):
        one += 1
      else:
        zero += 1

    if(one > zero):
      for x in list(arr):
        if x[col] == '1':
          arr.remove(x)
    elif(one < zero):
      for x in list(arr):
        if x[col] == '0':
          arr.remove(x)
    else:
      for x in list(arr):
        if x[col] == '1':
          arr.remove(x)
    col += 1
    one, zero = 0, 0

  return arr[0]

def main():
  o2 = []
  co2 = []

  with open("./Day3/Part2/input.txt", 'r') as f:
    o2 = f.read().split()

  for x in o2:
    co2.append(x)

  o2Rating = getO2Rating(o2)
  co2Rating = getCO2Rating(co2)

  answer = (int(o2Rating,2) * int(co2Rating,2))

  print("The answer to Day 3 Part 2 is \033[32;1m{}\033[0m".format(answer))

if __name__ == "__main__":
  main()