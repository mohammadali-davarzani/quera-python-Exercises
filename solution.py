def csv_reader(path):
    lines = list()
    with open(path) as file:
        for row in file:
            lines.append(row.split())
    times = 0
    for i in lines:
        if (len(i) > 0) and (i[0][0] != "#") :
            times += 1
    print(times)
    
        


path = input()
csv_reader(path)
