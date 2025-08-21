t = int(input())
results = []

for test in range(t):
    n = int(input())
    xs = []
    for power in range(1,19):
        if n % (10 ** power + 1) == 0:
            xs += [n // (10 ** power + 1)]
    results += [[len(xs), sorted(xs)]]

for output in results:
    print(output[0])
    if(len(output[1]) > 0):
        print(" ".join([str(_) for _ in output[1]]))