players = input()

target = players[0]
count = 1
flag = False
for player in players[1:]:
    if player == target:
        count += 1
    else:
        target = player
        count = 1
    if count == 7:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")
        