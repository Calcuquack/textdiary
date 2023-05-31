from colorama import Fore, Back, Style
with open(input("File Name: ")) as f:
  diary = f.read().split("\n")
date = input("Type in the date or nesting of the entry: ").split("/")
def reverseparenthesis(character):
  if character == "(":
    return ")"
  if character == "[":
    return "]"  
def checkdepth(line):
  streak = 0
  symbol = ""
  count = 0
  for i in line:
    count = count + 1
    if(count == 1 and (i == "[" or i == "(")):
      symbol = i
      streak = 1
    elif (i == symbol):
      streak = streak + 1
    else: 
      break
  if(streak>0):
    if(line[-1*streak:] == streak*reverseparenthesis(symbol)):
      if(symbol == "["):
        return streak*2-1
      else:
        return streak*2
    else:
      return -1
  else:
    return 0
def get(line):
  streak = 0
  symbol = ""
  count = 0
  for i in line:
    count = count + 1
    if(count == 1 and (i == "[" or i == "(")):
      symbol = i
      streak = 1
    elif (i == symbol):
      streak = streak + 1
    else: 
      break
  if(streak>0):
    if(line[-1*streak:] == streak*reverseparenthesis(symbol)):
      return line[streak:-1*streak]
    else:
      return None
  else:
    return None    
depth = 0    
entry = ""    
for i in diary:
  if(checkdepth(i) <= depth and checkdepth(i)>0):
    depth = 0
    break
  if(depth == len(date)):
    entry = entry + i + "\n"
  if(checkdepth(i)-1 == depth):
    if(depth < len(date)):
      if(get(i).lower() == date[depth].lower()):
        depth = depth + 1 
print(Fore.RED + entry + Style.RESET_ALL)
