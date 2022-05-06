
class Athlete():
	def __init__(self, name, age, country, team, time):
		self.__name = name
		self.__age = age
		self.__country =country
		self.__team = team
		self.__time= time

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

		
person = Athlete("nombre", "edad", 20, "pais", 20)
person.name("otro nombre")
print(person.name())







	# def addAthlete(self, name, age, country, team, time):
	# 	self.__name = name
	# 	self.__age = age
	# 	self.__country =country
	# 	self.__team = team
	# 	self.__time= time

	# def initialitation(self):
	# 	if(len(self.__allData) == 0):
	# 		self.__id = self.__id + 1

	# def addToList(self):


   
	
	 	

# person = Athlete("hola")
# person.saludar()

# class Humano(): #Creamos la clase Humano
#    def __init__(self, edad, nombre, ocupacion): #Definimos el parametro edad , nombre y ocupacion
#       self.edad = edad # Definimos que el atributo edad, sera la edad asignada
#       self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asig
#       self.ocupacion = ocupacion #DEFINIMOS EL ATRIBUTO DE INSTANCIA OCUPACION
        
#         #Creación de un nuevo método
#    def presentar(self):
#         presentacion = ("Hola soy {}, mi edad es {} y mi ocupación es {}") #Mensaje
#         print(presentacion.format(self.nombre, self.edad, self.ocupacion)) #Usamos FORMAT
# Persona1 = Humano(31, "Pedro", "Desocupado")