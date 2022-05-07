
class Athlete():
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__country = ""
        self.__team = ""
        self.__time = 0

    @property
    def name(self):
        return self.__name

    @property
    def age(self, age):
        return self.__age

    @property
    def country(self, country):
        return self.__country

    @property
    def team(self, team):
        return self.__team

    @property
    def time(self, time):
        return self.__time

        # .....................................

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    @country.setter
    def country(self, country):
        self.__country = country

    @team.setter
    def team(self, team):
        self.__team = team

    @time.setter
    def time(self, time):
        self.__time = time

    def diccionary(self):
        return {"name": self.__name, "age": self.__age, "country": self.__country, "team": self.__team, "time": self.__time}
