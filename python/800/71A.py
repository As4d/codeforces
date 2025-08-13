n = int(input())

for _ in range(n):
  w = input()
  l = len(w)
  if l > 10:
    print(w[0] + str(len(w[1:-1])) + w[-1])
  else:
    print(w)