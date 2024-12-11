
stones = []
with open(file="day11/input.txt", mode="r") as file:
  stones = [int(x) for x in file.read().split()]

def blink(stone, level, max_blink) -> list:
  if level == max_blink:
    return 1
  
  stone_count = 0
  if stone == 0:
    stone_count += blink(1, level+1, max_blink)
  elif len(str(stone)) % 2 == 0:
    left = int(str(stone)[:len(str(stone))//2])
    right = int(str(stone)[len(str(stone))//2:])
    stone_count += blink(left, level+1, max_blink)
    stone_count += blink(right, level+1, max_blink)
  else:
    stone_count += blink(stone * 2024, level+1, max_blink)  
  
  return stone_count


def iterate_stones(stones, max_blink) -> int:
  res = 0
  for i in range(len(stones)):
    res += blink(stones[i], 0, max_blink)
  return res

a = iterate_stones(stones, 25)
b = iterate_stones(stones, 75)

print(f"day11, a: {a}, b: {b}")
