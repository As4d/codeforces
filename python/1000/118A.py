s = input().lower()
n = ""

v = ["a", "e", "i", "o", "u", "y"]
for c in s:
    if c not in v:
        n += "." + c

print(n)