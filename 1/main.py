from AthleteClass import Athlete

print("................")
print("=== añadir jugadores ===")
print("................")

option = 1
registros = []

while(option != 0):
    print("")
    if(option == 1):
        nombre = input("digita nombre  ")
        edad = int(input("digita edad  "))
        pais = input("digita pais  ")
        equipo = input("digita equipo  ")
        tiempo = int(input("digita tiempo (en minutos)  "))

        if(edad > 0 and tiempo > 0):
            jugador = Athlete()
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
        ganadores = []
        for obj in registros:
            if(obj["time"] <= menorTiempo):
                menorTiempo = obj["time"]
                ganadores.append(obj)

        if(len(ganadores)>1):
            print(f'L@s ganadores son: ')
            print(f'{ganadores}')
        else:
            print(f'El ganador(a) es: ')
            print(f'{ganadores[0]}')

    else:
        print("opción invalida")

    print("")
    print("=== 0. Salir ===")
    print("=== 1. Agregar nuevo jugador(a) ===")
    print("=== 2. Ver tod@s l@s jugador@s ===")
    print("=== 3. Ver ganador(a) ===")
    option = input("¿Qué deseas hacer? ")
    
    if(option.isdigit()):
        option = int(option)
    else:
        option = 4
    
