t = int(input())
results = []

for test in range(t):
    n = int(input())
    a = str(input())
    m = int(input())
    b = str(input())
    c = str(input())
    
    for i in range(m):
        if c[i] == "D":
            a += b[i]
        else:
            a = b[i] + a
    
    results += [a]
    
for output in results:
    print(output)