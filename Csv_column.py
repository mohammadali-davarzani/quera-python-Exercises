import csv
def process (path):
    numbers = list()
    with open(path) as csv_file:
        for row in csv_file.readlines():
            numbers.append(row.rstrip().split(','))
    
    for i in range(0, len(numbers)): 
        for j in range(0, len(numbers[i])):
            numbers[i][j] = int(numbers[i][j])

    output = list()
    sum_of_numbers = list()
    for i in range(0, len(numbers)):
        sum_of_numbers.append([sum(numbers[i])])

    for i in range(0, len(numbers)):
        output.append([*numbers[i], *sum_of_numbers[i]])

    with open('ans.csv', 'w') as f: 
        
        write = csv.writer(f) 
        
        write.writerows(output) 


path = input()
process(path)
