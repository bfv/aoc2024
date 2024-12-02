
lines = open(file="day02/input.txt", mode="r").read().split("\n")

reports = []
for line in lines:
  reports.append([int(x) for x in line.split()])

def is_safe(report) -> 0 | 1:  # 0 = unsafe, 1 = safe
  direction = 0
  for i in range(len(report) - 1):
    delta = report[i] - report[i + 1]
    if abs(delta) > 3 or delta == 0 or direction * delta < 0:    
      return 0
    direction = delta    
  return 1

safe_count_a, safe_count_b = 0, 0  
for report in reports:
  safe_count_a += is_safe(report)
  for i in range(len(report)):
    if is_safe(report[:i] + report[i+1:]):
      safe_count_b += 1
      break

print(f"day 02, a: {safe_count_a}, b: {safe_count_b}")  
