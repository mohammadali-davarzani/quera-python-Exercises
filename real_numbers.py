import re
try:
    while True:
        line = input()
        regex = re.findall(r'^\s*[+-]?(\d+(.\d+)?)([eE][+-]?\d+)?\s*$', line)
        if len(regex) > 0:
            print("LEGAL")
        else:
            print("ILLEGAL")
except:
    pass