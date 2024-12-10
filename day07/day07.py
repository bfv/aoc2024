
equations = []
with open(file="day07/input.txt", mode="r") as file:
  for line in file.read().splitlines():
    equations.append([int(x) for x in line.replace(":", "").split()])

def check(res: int, numbers: list, operations: list) -> bool: 

  if len(numbers) == 1:
    return res == numbers[0]
  
  if numbers[0] > res:
    return False
  
  for op in operations:
    match op:
      case "+":
        op_res = numbers[0] + numbers[1]
      case "*":
        op_res = numbers[0] * numbers[1]
      case "||":
        op_res = numbers[0] * pow(10, len(str(numbers[1]))) + numbers[1]
        
    new_numbers = [op_res]
    if len(numbers) > 2:
      new_numbers += numbers[2:]    
      
    if check(res, new_numbers, operations):
      return True
        
  return False  
  
a, b = 0, 0
for eq in equations:
  if check(eq[0], eq[1:], ["+", "*"]):
    a += eq[0]
  if check(eq[0], eq[1:], ["*", "+", "||"]):
    b += eq[0]
 
print(f"iter: {iter}")  
print(f"day07, a: {a}, b: {b}")
