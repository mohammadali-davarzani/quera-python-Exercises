from Object_oriented.work_place import WorkPlace, Consts
import math

class Company(WorkPlace):

    def __init__ (self, name):
        
        self.name = name

        super(Company, self).__init__(name)

        self.expertise = "company"

    def calc_capacity(self):

        self.capacity = self.level

    def calc_costs(self):

        Consts.BASE_PALCE_COST = Consts.BASE_PLACE_COST

        self.cost = Consts.BASE_PALCE_COST * self.level

        return self.cost