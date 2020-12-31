number = int(input())

films_name = list()
for i in range(0, number):
    film_name_input = input().split()
    films_name.append(film_name_input)

test = list()
output = list()
for i in range(0, len(films_name)):
    for j in range(0, len(films_name[i])):
        test.append(films_name[i][j].capitalize())
    
    
for x in range(0, len(films_name)):
    output.append(test[0:len(films_name[x])])
    del test[0:len(films_name[x])]

for i in range(0, len(output)):
    print(*output[i])