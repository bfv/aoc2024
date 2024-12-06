
lines = ''
with open(file="day03/__input.txt", mode="r") as file:
  lines = ''.join(file.read().splitlines())
  #lines = file.read().splitlines()
print(lines)
#exit()

digits = list(range(10)).append(',')  
a, b = 0, 0
current_is_do = True

def get_numbers(str):
  print(f'  {str}')
  str = str.replace("mul(", "").replace(")", "")
  numbers = str.split(',')

  try:
    res = [int(n) for n in numbers]
  except:
    res = None

  return res

def checkRemainder(line, idx):
  end = line.find(")", idx)
  mul = f"{line[idx:end+1]}"
  numbers = get_numbers(mul)
  res = 0
  if numbers != None:
    dont_idx = line.rfind("don't()", 0, idx)
    do_idx = line.rfind("do()", 0, idx)
    
    if (do_idx == -1 and dont_idx == -1 and current_is_do == True) or (dont_idx < idx and do_idx < idx and dont_idx < do_idx):
      res = numbers[0] * numbers[1]
      current_is_do = True
    else:
      current_is_do = False
      
  return res

    
for line in lines:
  # a
  parts = line.split('mul(')
  for part in parts:    
    numbers = get_numbers(part.split(')')[0])
    print(numbers)
    if numbers != None:
      a += numbers[0] * numbers[1]
  
  # b: a approach does not work, 
  # idx = 0
  # done =- False
  # while not done:
  #   idx = line.find("mul(", idx)
  #   if idx == -1:
  #     break
  #   b += checkRemainder(line, idx)
  #   idx += 1

print(f"day 03, a: {a}, b: {b}")  
