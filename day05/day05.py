

with open(file="day05/input.txt", mode="r") as file:
  still_ordering = True
  ordering, updates, evaluated_updates = [], [], []
  for line in file.read().splitlines():
    if line == "":
      still_ordering = False
      continue
    if still_ordering:
      #print(f"ordering: {line}")
      ordering.append(tuple(map(int, line.split("|"))))
    else:
      updates.append(list(map(int, line.split(","))))  
      pass

def find(val: int) -> list:
  #print(f"Finding {val} in ordering {ordering}")
  found = []
  for i in range(0, len(ordering)):
    if ordering[i][0] == val:
      found.append(ordering[i])
  return found

  def is_tuple_in_ordering(t: tuple) -> bool:
    return t in ordering
  
ordering.sort(key=lambda x: x[0])

print(f"ordering: {ordering}")
print(f"75: {find(75)}")

def check_rule(update: list) -> bool:
  # rule 1
  order_ok = True
  for i in range(len(update) - 1):
    for j in range(i + 1, len(update)):
      if (update[j], update[i]) in ordering:
        print(f"wrong order: {update[j]} after {update[i]}")
        return False
        break
  return True

def calc_a_for_update(update: list) -> int:
  return update[len(update) // 2]

a, b = 0, 0
for update in updates:
  order_ok = check_rule(update)
  if order_ok:
    print(f"a for {update}: {calc_a_for_update(update)}")
    a += calc_a_for_update(update)
  else:
    pass
  
print(f"day05, a: {a}, b: {b}")


# def check_rule2(update: list) -> bool:
#   sorted_update = sorted(update, key=lambda x: x)
#   print(f"update: {update} --> sorted_update: {sorted_update}")
#   if sorted_update in evaluated_updates:
#     print(f"Already evaluated {sorted_update}")
#     return False
#   evaluated_updates.append(sorted_update)
#   return True
