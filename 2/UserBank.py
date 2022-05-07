import random


class UserBank():
    def __init__(self):
        self.__name = ""
        self.__lastName = ""
        self.__id = ""
        self.country = ""
        self.__nroCard = random.random() + self.__id
        self.__currentBalance = 0

    @property
    def name(self):
        return self.__name

    @property
    def lastName(self, lastName):
        return self.__lastName

    @property
    def id(self, id):
        return self.__id

    @property
    def country(self, country):
        return self.__country

    @property
    def currentBalance(self):
        return self.__currentBalance

        # .....................................

    @name.setter
    def name(self, name):
        self.__name = name

    @lastName.setter
    def lastName(self, lastName):
        self.__lastName = lastName

    @id.setter
    def id(self, id):
        self.__id = id

    @country.setter
    def country(self, country):
        self.__country = country

    @currentBalance.setter
    def currentBalance(self, currentBalance):
        self.__currentBalance = currentBalance

    def diccionary(self, ):
        return {"name": self.__name, "lastName": self.__lastName, "country": self.__country, "nroCard": self.__nroCard, "currentBalance": self.__currentBalance}


# ........................Operationes...........................

    def moneyOut(self, quantity):
        if(quantity <= self.__currentBalance):
            self.__currentBalance = self.__currentBalance - quantity
