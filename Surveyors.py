class Reverse:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):

        output = self.data[::-1]
        return output

        if(len(output) == len(self.data)):
            raise StopIteration
        
        

ls = [10, 20, 30]
for i in Reverse(ls):
    print(i)
print(ls)