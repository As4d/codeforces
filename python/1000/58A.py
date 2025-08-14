s = input()
i = 0
hello = "hello"
while hello != "" and i < len(s):
    if s[i] == hello[0]:
        hello = hello[1:]
    i += 1

if hello == "":
    print("YES")
else:
    print("NO")