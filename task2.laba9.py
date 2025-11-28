n = input()
d = input()

pos = n.rfind(d)

if pos == -1:
    print(0)
else:
     print(len(n) - pos)
