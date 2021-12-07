#!/usr/bin/env python3

def main():
  o2 = []
  co2 = o2
  col, one, zero = 0, 0, 0

  with open("./Day3/Part2/input.txt", 'r') as f:
    o2 = f.read().split()

  while len(o2) > 1:
    print(col, o2)
    for x in o2:
      if(o2[col] == '1'):
        one += 1
      else:
        zero += 1
    
    if(one > zero):
      for x in o2:
        if x[col] == '0':
          o2.remove(x)
    else:
      for x in o2:
        if x[col] == '1':
          o2.remove(x)
    col += 1
    one, zero = 0, 0

  while len(co2) > 1:
    for x in co2:
      if(co2[col] == '1'):
        one += 1
      else:
        zero += 1
    
    if(one > zero):
      for x in co2:
        if x[col] == '0':
          co2.remove(x)
    else:
      for x in o2:
        if x[col] == '1':
          co2.remove(x)
    col += 1
    one, zero = 0, 0

  print(co2, o2)

if __name__ == "__main__":
  main()