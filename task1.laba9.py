n= input()
n= n.zfill(4)

if n[0] == n[3] and n[1] == n[2]:
    print(1)
else:
    print(0)