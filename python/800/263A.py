matrix = [input().split(" ") for _ in range(5)]

for x in range(5):
  for y in range(5):
    if matrix[x][y] == "1":
      print(abs(2 - x) + abs(2 - y))