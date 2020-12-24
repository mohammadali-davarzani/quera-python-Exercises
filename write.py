text = input()

text_list = list()
for i in text :
    if (len(text_list) != 0) and (i == "="):
        text_list.pop()
    elif (i != "="):
        text_list.append(i)

for i in text_list:
    print(i, end='')