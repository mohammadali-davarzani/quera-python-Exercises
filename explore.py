import os

def explore (type, path):
    output = dict()
    type = type.lower()
    walk = os.walk(path)
    for root, dirs, files in walk:
        for file in files:
            if file.endswith(".%s" % type):
                if file.split('.')[-1].lower() == type:
                    
                    if root not in output:
                        output[root] = 1
                    elif root in output:
                        output[root] += 1
                
    print(output)
explore("mkv", "./")