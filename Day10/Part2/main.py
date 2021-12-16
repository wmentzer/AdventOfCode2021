#!/usr/bin/env python3

def checkScore(param = []):
  complScore = 0

  for i in range(len(param)):
    complScore *= 5
    
    if(param[i] == ')'):
      complScore += 1
    elif(param[i] == ']'):
      complScore += 2
    elif(param[i] == '}'):
      complScore += 3
    elif(param[i] == '>'):
      complScore += 4

  return complScore

def main():
  inputList = []
  stack = []
  compl = []
  scores = []

  with open('./Day10/Part2/input.txt') as f:
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
        stack = []
        break
    
    if(len(stack) != 0): 
      while (len(stack) != 0):
        if(stack[-1] == '{'):
          compl.append('}')
        elif(stack[-1] == '['):
          compl.append(']')
        elif(stack[-1] == '<'):
          compl.append('>')
        elif(stack[-1] == '('):
          compl.append(')')
        stack.pop()

      scores.append(checkScore(compl))
    stack = []
    compl = []

  scores.sort()

  print("The answer is: \033[32m{}\033[0m".format(scores[len(scores)//2]))

if __name__ == '__main__':
  main()