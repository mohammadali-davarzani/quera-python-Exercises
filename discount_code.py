n, t = input().split()

output = list()
for i in range(int(n)):
    code = input()
    word = list()
    count = 0
    for j in code:
        if (j in t) and (j not in word):
            word.append(j)
    for y in word:
        if y in t:
            count += 1

    if count >= len(t):
        output.append("Yes")
    elif count < len(t):
        output.append("No")

for x in output:
    print(x)
    