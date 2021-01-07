from person import Person, Consts
import math 

class Worker(Person):

    def __init__ (self, name, age):

        self.name = name

        self.age = age

        super(Worker, self).__init__(name, age)

        self.job = "worker"
    
    def get_price(self):

        Consts.BASE_PRICE[self.job] = Consts.BASE_PRICE[self.job]

        Consts.MIN_AGE = Consts.MIN_AGE

        Consts.AGE_MUL = Consts.AGE_MUL

        self.price = int(math.floor(Consts.BASE_PRICE[self.job] * Consts.MIN_AGE / self.age))

        return self.price
    
    def calc_life_cost(self):

        Consts.BASE_COST[self.job] = Consts.BASE_COST[self.job]
        
        Consts.MIN_AGE = Consts.MIN_AGE

        Consts.AGE_MUL = Consts.AGE_MUL

        self.cost = int(math.floor(Consts.BASE_COST[self.job] * self.age / Consts.MIN_AGE))

        return self.cost

    def calc_income(self):

        Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] = Consts.BASE_INCOME[self.job][self.work_place.get_expertise()]

        Consts.MIN_AGE = Consts.MIN_AGE

        Consts.AGE_MUL = Consts.AGE_MUL

        self.income = int(math.floor(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] * Consts.MIN_AGE / self.age))

        return self.income





