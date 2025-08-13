n = int(input())
x = 0
for _ in range(n):
  x = eval("x" + sorted(input())[0] + "1")
print(x)