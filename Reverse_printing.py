numbers = list()
try:
    run = True
    while run:
        line = int(input())
        if (line != 0):
            numbers.append(line)
        else:
            run = False
except:
    pass

numbers.reverse()
for i in numbers:
    print(i)