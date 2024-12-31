from collections import Counter

aloc = []
char_arrays = []

def main():
  global aloc, char_arrays
  lines = []
  with open(file="day04/input.txt", mode="r") as file:
    char_arrays = [list(line) for line in file.read().splitlines()]

  a, b = 0, 0
  
  aloc = []  
  a = count_occurrences(char_arrays, "XMAS")
  
  aloc = []
  count_occurrences(char_arrays, "MAS")
  
  occurrences = Counter(aloc)
  occurrences = {k: v for k, v in occurrences.items() if v > 1}
  b = len(occurrences)
  
  #print_board(char_arrays, occurrences)
  
  print(f"day04, a: {a}, b: {b}")

def print_board(char_arrays, aloc):
  for i in range(len(char_arrays)):
    for j in range(len(char_arrays[0])):
      if (i, j) in aloc:
          print(f"\033[92m{char_arrays[i][j]}\033[0m", end="")
      else:
        print(char_arrays[i][j], end="")
    print()

def count_occurrences(char_arrays, target):
  
  if target == "XMAS":
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
  else:
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    
  def check_direction(x, y, dx, dy):
    global aloc
    for i in range(len(target)):
      if not (0 <= x + i * dx < len(char_arrays) and 0 <= y + i * dy < len(char_arrays[0])):
        return False
      if char_arrays[x + i * dx][y + i * dy] != target[i]:
        return False
    #print(f"{(x+dx, y+dy)}")
    if target == "MAS":
      aloc.append((x+dx, y+dy))
    return True

  count = 0
  for i in range(len(char_arrays)):
    for j in range(len(char_arrays[0])):
      for dx, dy in directions:
        if check_direction(i, j, dx, dy):
          count += 1
  return count

if __name__ == '__main__':
  main()
