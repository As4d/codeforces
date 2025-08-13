k,A = int(input().split(" ")[1]), input().split(" ")
print(len([_ for _ in A[:len(A[:k]) + len([_ for _ in A[k:] if _ == A[k - 1]])] if int(_) > 0]))