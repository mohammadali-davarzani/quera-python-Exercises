class WorkPlaceIsFull(Exception):

    def __str__(self):
        return "work place is full!"

class Consts:

    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}
    LEVEL_MUL = 5
    BASE_PLACE_COST = 25


class WorkPlace:
    
    instances = [] 
    
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.expertise = ""
        self.employees = []
        self.capacity = 1
        WorkPlace.instances.append(self)
        
    def get_price(self):
        return Consts.BASE_PRICE[self.expertise]
    
    def upgrade(self):
        self.level += 1
        self.calc_capacity()
        
    def do_hire(self, person):
        if len(self.employees) >= self.capacity:
            raise WorkPlaceIsFull()
            
        else:
           self.employees.append(person) 
           person.work_place = self
            
    @staticmethod
    def calc_all():
        output = list()
        for instance in WorkPlace.instances:
            output.append(instance.calc())
        return sum(output)
        
    def get_expertise(self):
        return self.expertise
        
    def calc(self):
        return -self.calc_costs()
    
    def calc_capacity(self):
        pass

    def calc_costs(self):
        pass