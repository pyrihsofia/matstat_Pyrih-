s = input()

if len(s) <= 3:
    print(s)
else:
    parts = []
    while len(s) > 3:
        parts.append(s[-3:])
        s = s[:-3]
    parts.append(s)
    parts.reverse()
    print(" ".join(parts))


