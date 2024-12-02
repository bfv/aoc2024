
lines = open(file="day01/input.txt", mode="r").read().split("\n")

lefts, rights = [], []
for line in lines:
  left, right = map(int, line.split())
  lefts.append(left); rights.append(right)

lefts.sort(), rights.sort()

distance = 0
for i in range(len(lefts)):
  distance += abs(lefts[i] - rights[i])
  
print(f"day 01a: {distance}")

similarity = 0  
for i in range(len(lefts)):
  similarity += lefts[i] * rights.count(lefts[i])
  
print(f"day 01b: {similarity}")
