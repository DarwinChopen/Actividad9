while True:
    print("Menu")
    print("1.Registrar clientes")
    print("2. Listado Clientes")
    print("3. Salir")
    try:
        opcion=int(input("Ingrese una Opcion: "))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            print("Registo de datos")
        case 2:
            print("Listado de datos")
        case 3:
            print("Saliendo...")
            break
        case _:
            print("Opcion Invalida")


