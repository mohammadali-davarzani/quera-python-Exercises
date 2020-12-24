n = int(input())

names = dict()
for i in range(n):
    name = input().split()
    if name[0] in names:
        names[name[0]] += 1
    else:
        names[name[0]] = 1


#--------------------------------------------------------------------