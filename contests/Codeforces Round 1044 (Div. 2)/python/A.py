t = int(input())
results = []

for test in range(t):
    n = int(input())
    a = input().split(" ")
    results += ["YES" if len(set(a)) < n else "NO"]
    
for _ in results:
    print(_)