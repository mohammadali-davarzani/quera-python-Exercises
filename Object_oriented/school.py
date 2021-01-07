from Object_oriented.work_place import WorkPlace, Consts
import math

class School(WorkPlace):

    def __init__ (self, name):
        
        self.name = name

        super(School, self).__init__(name)

        self.expertise = "school"

    def calc_capacity(self):

        self.capacity = int(math.floor(math.sqrt(self.level)))

    def calc_costs(self):

        Consts.BASE_PALCE_COST = Consts.BASE_PLACE_COST
        
        self.cost = Consts.BASE_PALCE_COST * int(math.floor(math.sqrt(self.level)))
        
        return self.cost
