number = int(input())

letters = list()

for i in range(number):

    name = input()
    t = ""

    for ch in name:
        if (ch not in t):
            t += ch

    letters.append(t)

output = ""
for i in letters:
    if (len(i) >= len(output)):
        output = i
print(len(output))
    

