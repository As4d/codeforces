n = input()
print(n.upper() if len([_ for _ in n if _.isupper()]) > len([_ for _ in n if _.islower()]) else n.lower())
