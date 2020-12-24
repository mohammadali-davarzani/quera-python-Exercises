from datetime import datetime

date = datetime.strptime(input(), '%Y-%m-%d')

sajad_born = datetime.strptime("1999-01-14", '%Y-%m-%d')

output = (date - sajad_born).days

if (output < 0):
    print("Not yet born")

else:
    print(output)