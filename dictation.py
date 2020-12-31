output = list()
for i in range(1, 6):
    entry = input()
    if ("MOLANA" in entry) or ("HAFEZ" in entry):
        output.append(i)
    
if (len(output) == 0):
    print("NOT FOUND!")

else:
    print(*output)