n = int(input(""))

def is_lucky(n):
    s = set([int(_) for _ in str(n)])
    return s == {4} or s == {7} or s == {4, 7}

flag = False

if is_lucky(n):
    flag = True

lucky_divisor = 4
while lucky_divisor < n and not flag:
    if n % lucky_divisor == 0:
        flag = True
    else:
        lucky_divisor += 1
        while not is_lucky(lucky_divisor):
            lucky_divisor += 1

if flag:
    print("YES")
else:
    print("NO")

