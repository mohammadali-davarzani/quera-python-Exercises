from person import Person, Consts
import math 

class Teacher(Person):

    def __init__ (self, name, age):

        self.name = name

        self.age = age

        super(Teacher, self).__init__(name, age)

        self.job = "teacher"

    
    def get_price(self):

        Consts.BASE_PRICE[self.job] = Consts.BASE_PRICE[self.job]

        Consts.MIN_AGE = Consts.MIN_AGE

        Consts.AGE_MUL = Consts.AGE_MUL

        self.price = int(Consts.BASE_PRICE[self.job] - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL)

        return self.price

    def calc_life_cost(self):

        Consts.BASE_COST[self.job] = Consts.BASE_COST[self.job]
        
        Consts.MIN_AGE = Consts.MIN_AGE

        Consts.AGE_MUL = Consts.AGE_MUL

        self.cost = int(Consts.BASE_COST[self.job] + (self.age - Consts.MIN_AGE) * Consts.AGE_MUL)

        return self.cost
        
    def calc_income(self):

        Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] = Consts.BASE_INCOME[self.job][self.work_place.get_expertise()]

        Consts.MIN_AGE = Consts.MIN_AGE

        Consts.AGE_MUL = Consts.AGE_MUL

        self.income = int(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL)

        return self.income
