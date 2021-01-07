from math import sqrt
class Person():

    instances = [] 

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.level = 1
        self.job = ""
        self.work_place = None
        Person.instances.append(self)

    def do_level(self, income):
        self.income = income 
        output = income * sqrt((self.level * self.work_place.level))
        return output
    
    def calc_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self):
        income = self.calc_income()
        cost = self.calc_life_cost()
        output = self.do_level(income) - cost
        return output
    
    @staticmethod
    def calc_all():
        output = list()
        for instance in Person.instances:
            output.append(instance.calc())
        return sum(output)

    def get_job(self):
        return self.job
    
    def upgrade(self):
        self.level += 1

