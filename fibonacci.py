nterms = int(input())

n1, n2 = 0, 1
count = 0

fibonacci_numbers = list()

if 100 < nterms < 1:
   pass

else:
   
   while n1 <= nterms:
       fibonacci_numbers.append(n1)
       nth = n1 + n2
       
       n1 = n2
       n2 = nth
       count += 1
    
output = list()
for i in range(1, nterms+1):
    if i in fibonacci_numbers:
        output.append("+")
    else:
        output.append("-")

print("".join(output))