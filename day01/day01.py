
lines = open(file="day01/input.txt", mode="r").read().split("\n")

left, right = [], []
for line in lines:
  nmbrs = line.split("  ")
  left.append(int(nmbrs[0]))
  right.append(int(nmbrs[1]))

left.sort(), right.sort()

distance = 0
for i in range(len(left)):
  distance += abs(left[i] - right[i])
  
print(f"day 01a: {distance}")

similarity = 0  
for i in range(len(left)):
  similarity += left[i] * right.count(left[i])
  
print(f"day 01b: {similarity}")
