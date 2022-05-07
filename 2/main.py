from UserBank import UserBank

print("................")
print("=== añadir jugadores ===")
print("................")
option = 1
registros = []

# obj = {"name": "pepe", "age": 23}
# print(f'{obj["age"]}')
# print(f'{registros}')

while(option != 0):
    print("")
    if(option == 1):
        nombre = input("digita nombre  ")
        edad = int(input("digita edad  "))
        pais = input("digita pais  ")
        equipo = input("digita equipo  ")
        tiempo = int(input("digita tiempo (en minutos)  "))

        if(edad > 0 and tiempo > 0):
            jugador = UserBank()
            jugador.name = nombre
            jugador.age = edad
            jugador.country = pais
            jugador.team = equipo
            jugador.time = tiempo
            registros.append(jugador.diccionary())
        else:
            print("Ingrese un valor valido mayor a cero")
            option = 4

    elif(option == 2):
        print(registros)
    elif(option == 3):
        menorTiempo = registros[0]["time"]
        ganador = registros[0]
        for obj in registros:
            if(obj["time"] < menorTiempo):
                menorTiempo = obj["time"]
                ganador = obj
        print(f'{ganador}')

    else:
        print("opción invalida")

    print("")
    print("=== 0. Salir ===")
    print("=== 1. Agregar nuevo jugador(a) ===")
    print("=== 2. Ver tod@s l@s jugador@s ===")
    print("=== 3. Ver ganador(a) ===")
    option = int(input("¿Qué deseas hacer? "))
