import math

i = input().split(" ")
n, m, a = int(i[0]), int(i[1]), int(i[2])

print(math.ceil(n/a) * math.ceil(m/a))

