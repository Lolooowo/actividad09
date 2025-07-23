clientes = {}

#def sumaDestinos(clientes):


numeroClientes = int(input("¿Cuantos clientes desea ingresar?: "))
for i in range (numeroClientes):
    codigoClinte = "CL" + str(i+1)
    print(f"\t CLiente: {codigoClinte}")
    nombre = input("Ingrese el nombre del cliente: ")
    clientes[codigoClinte] = {
        "nombre": nombre,
    }
    numDestinos = int(input("¿Cuantos destinos desea ingresar?: "))
    for x in range (numDestinos):
        codigoDestino = x+1
        destino = input(f"\t Destino {x+1}: ")
        clientes[codigoClinte]["codigoDestino"] = {
            "destino": destino,
        }
