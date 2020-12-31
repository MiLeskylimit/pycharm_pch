# mly

yyghx = []
yygsp = []

with open('yyghx.txt') as f:
    for a in f.readlines():
        a = a.strip('\n')
        a = a.strip('"')
        yyghx.append(a)
with open("yygsp.txt") as h:
    for b in h.readlines():
        b = b.strip('\n')
        b = b.strip('"')
        yygsp.append(b)

for c in yygsp:
    if c in yyghx:
        print(c)
    else:
        pass

print("-------------------------------------------")
for c in yyghx:
    if c in yygsp:
        print(c)
    else:
        pass





