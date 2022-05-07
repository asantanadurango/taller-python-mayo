import random


class UserBank():
    def __init__(self):
        self.__name = ""
        self.__lastName = ""
        self.__userId = 0
        self.__country = ""
        self.__currentBalance = 0
        self.__nroCard = "card#"

    @property
    def name(self):
        return self.__name

    @property
    def lastName(self):
        return self.__lastName

    @property
    def userId(self):
        return self.__userId

    @property
    def country(self):
        return self.__country

    @property
    def currentBalance(self):
        return self.__currentBalance

    @property
    def nroCard(self):
        return self.__nroCard

        # .....................................

    @name.setter
    def name(self, name):
        self.__name = name

    @lastName.setter
    def lastName(self, lastName):
        self.__lastName = lastName

    @userId.setter
    def userId(self, userId):
        self.__userId = userId

    @country.setter
    def country(self, country):
        self.__country = country

    @currentBalance.setter
    def currentBalance(self, currentBalance):
        self.__currentBalance = currentBalance

    @nroCard.setter
    def nroCard(self, nroCard):
        self.__nroCard = nroCard

    def diccionary(self, ):
        return {"name": self.__name, "lastName": self.__lastName, "userId": self.__userId, "country": self.__country, "currentBalance": self.__currentBalance, "nroCard": self.__nroCard}


# ........................Operationes...........................

    def moneyOut(self, quantity):
            self.__currentBalance = self.__currentBalance - quantity

    def moneyUp(self, quantity):
            self.__currentBalance = self.__currentBalance + quantity
