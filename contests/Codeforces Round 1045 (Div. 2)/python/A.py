t = int(input())
results = []

for test in range(t):
    n,a,b = (int(_) for _ in input().split(" "))
    results += ["YES" if (b % 2 == n % 2)  and  (a <= b or a % 2 == n % 2) else "NO"]

for _ in results:
    print(_)