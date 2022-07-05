from time import sleep
from os import system as s
#Modules

def Dialogue(options, inputReturn):
  if (type(options) is list):
    pass
  else:
    print("GOKUDO ERROR 00: Dialogue not list.")
    quit()

  optionsLen = len(options)
  if optionsLen > 26:
    print("GOKUDO ERROR 01: Too many options.")
    quit()
  else:
    pass

  abcs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  oLet = []
  for i in range(0, optionsLen):
    oLet += abcs[i]

  print("\nChoose 1:")
  for i in range(0, optionsLen):
    print(oLet[i] + ": " + options[i])
  inp = input()
  if inp in abcs:
    pass
  else:
    print("GOKUDO ERROR 02: INVALID CHARACTER")
    quit()

  isAccounted = False
  for i in range(0, optionsLen):
    if inp == oLet[i]:
      inputReturn = i
      return inputReturn
      isAccounted = True
  if isAccounted != True:
    print("GOKUDO ERROR 03: INVALID CHARACTER (NOT IN ANSWER)")
    quit()
    



def Write(text):
  s("clear")
  print(text)
  