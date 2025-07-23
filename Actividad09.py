
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
            clientes={}
            cantidad=int(input("Ingrese la cantidad de clientes que sesea ingresar"))
            for i in range(cantidad):
                print(f"Cliente #: {i+1}")
                codigoCliente=input("Ingrrese el codigo del cliente")
                clientes[codigoCliente]={}
                clientes[codigoCliente]["Nombre"]=input("Ingrese el nombre del cliente")
                clientes[codigoCliente]["Destinos"]={}
                cantidadDestinos=int(input("Cuantos destinos desea Ingresaar"))
                for x in range(cantidadDestinos):
                    print(f"Destino #: {x + 1}")
                    codigoDestino=input("Ingrese el codigo del destino: ")
                    nombreDestino=input("Ingrese el nombre del destino: ")

                    clientes[codigoCliente]["Destinos"][codigoDestino] = {
                        "nombre": nombreDestino,
                    }
        case 2:
            print("Listado de datos")

        case 3:
            print("Saliendo...")
            break
        case _:
            print("Opcion Invalida")


