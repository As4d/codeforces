n = input()
s = [int(_) for _ in input().split(" ")]

# possible taxis (10)
# 4, 
# 3x1, 3, 
# 2x2, 2x1x1, 2x1, 2, 
# 1x1x1x1, 1x1x1, 1x1, 1

groups = {1:0, 2:0, 3:0, 4:0}
for g in s:
    groups[g] += 1

c = 0

c += groups[4] 

c += groups[3]
groups[1] -= groups[3]
if groups[1] < 0:
    groups[1] = 0

c += groups[2] // 2 + (1 if groups[2] % 2 > 0 else 0)
groups[1] -= (groups[2] % 2) * 2
if groups[1] < 0:
    groups[1] = 0

c += groups[1] // 4 + (1 if groups[1] % 4 > 0 else 0)

print(c)