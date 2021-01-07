from Object_oriented.work_place import WorkPlace, Consts
import math


class Mine(WorkPlace):

    def __init__ (self, name):
        
        self.name = name

        super(Mine, self).__init__(name)

        self.expertise = "mine"

    def calc_capacity(self):

        self.capacity = int(math.pow(self.level, 2))

    def calc_costs(self):

        Consts.BASE_PLACE_COST = Consts.BASE_PLACE_COST
        
        Consts.LEVEL_MUL = Consts.LEVEL_MUL
        
        self.cost = Consts.BASE_PALCE_COST + Consts.LEVEL_MUL * self.level
        
        return self.cost
