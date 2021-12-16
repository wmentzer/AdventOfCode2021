#!/usr/bin/env python3

def checkScore(param):
  if (param == ')'):
    return 3
  elif (param == ']'):
    return 57
  elif (param == '}'):
    return 1197
  elif (param == '>'):
    return 25137
  else:
    return 0

def main():
  inputList = []
  stack = []
  syntaxScore = 0

  with open('./Day10/Part1/input.txt') as f:
    inputList = f.read().splitlines()

  for x in inputList:
    for i in range(len(x)):
      if (x[i] == '{' or x[i] == '[' or x[i] == '<' or x[i] == '('):
        stack.append(x[i])
        continue
  
      if (x[i] == '}' and stack[-1] == '{'):
        stack.pop()
      elif (x[i] == ']' and stack[-1] == '['):
        stack.pop()
      elif (x[i] == '>' and stack[-1] == '<'):
        stack.pop()
      elif (x[i] == ')' and stack[-1] == '('):
        stack.pop()
      else:
        syntaxScore += checkScore(str(x[i]))
        break
    stack = []

  print("The answer is: \033[32m{}\033[0m".format(syntaxScore))

        


if __name__ == '__main__':
  main()