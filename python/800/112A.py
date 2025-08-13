a = [ord(_) for _ in input().lower()]
b = [ord(_) for _ in input().lower()]

o = 0

for i in range(len(a)):
    if a[i] > b[i]:
        o = 1
        break
    elif a[i] < b[i]:
        o = -1
        break

print(o)