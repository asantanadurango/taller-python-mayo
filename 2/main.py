from UserBank import UserBank

print("................")
print("=== Registrar usuario Bancolombia ===")
print("................")

registros = []

nombre = input("digita tu nombre  ")
apellido = input("digita tu apellido  ")
cedula = input("digita tu id  ")
while(cedula.isdigit() == False or int(cedula) < 0):
    print("Ingrese un id valido (numeros enteros positivos)")
    cedula = input()
cedula = int(cedula)
pais = input("digita pais  ")

usuario = UserBank()
usuario.name = nombre
usuario.lastName = apellido
usuario.userId = cedula
usuario.country = pais
registros.append(usuario)

print("")
print("=== ¿Qué deseas hacer? ===")
print("................")
print("=== 0. Salir ===")
print("=== 1. Ingresar como administrador ===")
print("=== 2. Ingresar como usuario ===")
option = input()
if(option.isdigit()):
    option = int(option)
else:
    option = 4
while(option != 0):
    print("")

    if(option == 1):
        print("=== ¿Qué deseas hacer? ===")
        print("................")
        print("=== 0. Salir ===")
        print("=== 1. Ingresar nuevo usuario ===")
        print("=== 2. Ver lista de usuarios ===")
        optionRol = input()
        if(optionRol.isdigit()):
            optionRol = int(optionRol)
        else:
            optionRol = 4

        if(optionRol == 0):
            option = 4

        while(optionRol != 0):
            if(optionRol == 1):
                nombre = input("digita tu nombre  ")
                apellido = input("digita tu apellido  ")
                while(cedula.isdigit() == False or int(cedula) < 0):
                    print("Ingrese un id valido (numeros enteros positivos)")
                    cedula = input()
                cedula = int(cedula)
                pais = input("digita pais  ")

                usuario = UserBank()
                usuario.name = nombre
                usuario.lastName = apellido
                usuario.userId = cedula
                usuario.country = pais
                registros.append(usuario)

            if(optionRol==2):
                paraMostrar = []
                for obj in registros:
                    paraMostrar.append(obj.diccionary())
                print(f'{paraMostrar}')
            else:
                print("opción invalida")
            print("")
            print("=== ¿Qué deseas hacer? ===")
            print("................")
            print("=== 0. Salir ===")
            print("=== 1. Ingresar nuevo usuario ===")
            print("=== 2. Ver lista de usuarios ===")
            optionRol = input()
            if(optionRol.isdigit()):
                optionRol = int(optionRol)
            else:
                optionRol = 4

            if(optionRol == 0):
                option = 4

    elif(option == 2):
        print("Por favor digite su id")
        inpID = input()
        while(inpID.isdigit() == False or int(inpID) < 0):
            print("Ingrese un id valido (numeros enteros positivos)")
            inpID = input()
        inpID = int(inpID)

        user = UserBank()
        for idx in range(len(registros)):
            if(registros[idx].userId == inpID):
                user.name = registros[idx].name
                user.lastName = registros[idx].lastName
                user.userId = registros[idx].userId
                user.country = registros[idx].country
                user.currentBalance = registros[idx].currentBalance
                user.nroCard = registros[idx].nroCard
 
        if(not user.userId):
            print("No se encontro este usuario")
            option = 4
        else:
            print(f'hola {user.name}')
            print("=== ¿Qué deseas hacer? ===")
            print("................")
            print("=== 0. Salir ===")
            print("=== 1. Consultar Saldo ===")
            print("=== 2. Consignar dinero ===")
            print("=== 3. Retirar dinero ===")
            optionRol = input()
            if(optionRol.isdigit()):
                optionRol = int(optionRol)
            else:
                optionRol = 4

            if(optionRol == 0):
                option = 4

            while(optionRol != 0):
                print("")
                if(optionRol == 1):
                    print("Saldo actual")
                    print(f'{user.currentBalance} $')

                elif(optionRol==2):
                    print("Ingresar cantidad a consignar")
                    monto = input()

                    while(monto.isdigit() == False or inpID < 0):
                        print("Ingrese un monto valido (numeros enteros positivos)")
                        monto = input()
                    monto = int(monto)
                    user.moneyUp(monto)
                    print(f'nuevo saldo {user.currentBalance}')

                elif(optionRol == 3):
                    print("Ingresar la cantidad que desea retirar")
                    monto = input()
                    while(monto.isdigit() == False or inpID < 0):
                        print("Ingrese un monto valido (numeros enteros positivos)")
                        monto = input()
                    monto = int(monto)

                    if(monto > user.currentBalance):
                        print("No cuenta con saldo suficiente para hacer esta operacion")
                        print(f'saldo actual:  {user.currentBalance}')
                        print(f'saldo que desea retirar: {monto}')
                        print(f'Balance {(user.currentBalance - monto)}')
                    else:
                        user.moneyOut(monto)
                        print("Transaccion exitosa: ")
                        print(f'Balance a favor {(user.currentBalance)}')

                else:
                    ("Opción no valida")

                for idx, value in enumerate(registros):
                    if(value.userId == inpID):
                        registros[idx] = user

                print("")
                print("=== ¿Qué deseas hacer? ===")
                print("................")
                print("=== 0. Salir ===")
                print("=== 1. Consultar Saldo ===")
                print("=== 2. Consignar dinero ===")
                print("=== 3. Retirar dinero ===")
                optionRol = input()
                if(optionRol.isdigit()):
                    optionRol = int(optionRol)
                else:
                    optionRol = 4
                if(optionRol == 0):
                    option = 4
    else:
        print("Dato no valido")
    print("=== ¿Qué deseas hacer? ===")
    print("................")
    print("=== 0. Salir ===")
    print("=== 1. Ingresar como administrador ===")
    print("=== 2. Ingresar como usuario ===")
    option = input()
    if(option.isdigit()):
        option = int(option)
    else:
        option = 4

print("Fin de la ejecución")