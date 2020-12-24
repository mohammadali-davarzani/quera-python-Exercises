n, m = input().split()
n = int(n)
m = int(m)
times = int(input())
map = []
for x in range(n):
    map.append([])
    for y in range(m):
         map[x].append(0)

for i in range(times):
    row , column = input().split()
    row = int(row)
    column = int(column)
    map[row-1][column-1] = "*"
    


for i in map:
    print(*i)

#----------------------------------------------------------------------