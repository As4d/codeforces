n = int(input())

t = 0
for _ in range(n):
  if sum([int(_) for _ in input().split(" ")]) > 1: t += 1

print(t)