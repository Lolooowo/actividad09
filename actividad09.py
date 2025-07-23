clientes = {}

def sumaDestinos(clientes, codigo):
    if codigo == len(clientes):
        cliente = clientes[codigo]
        numeroDestinos = 0
        for clave, valor in cliente["codigoDestino"].items():
            numeroDestinos = cliente["codigoDestino"].get(clave, numeroDestinos)
        return numeroDestinos
    else:
        cliente = clientes[codigo]
        numeroDestinos = 0
        for clave, valor in cliente["codigoDestino"].items():
            numeroDestinos = cliente["codigoDestino"].get(clave, numeroDestinos)
        return  numeroDestinos + sumaDestinos(clientes, codigo + 1)


numeroClientes = int(input("¿Cuantos clientes desea ingresar?: "))
for i in range (numeroClientes):
    codigoCliente =(i+1)
    print(f"\t CLiente: {codigoCliente}")
    nombre = input("Ingrese el nombre del cliente: ")
    clientes[codigoCliente] = {
        "nombre": nombre,
    }
    numDestinos = int(input("¿Cuantos destinos desea ingresar?: "))
    for x in range (numDestinos):
        codigoDestino = x+1
        destino = input(f"\t Destino {x+1}: ")
        clientes[codigoCliente]["codigoDestino"] = {
            "destino": destino,
            "totalDestinos" : numDestinos
        }
print("=== LISTADO DE CLIENTES Y DESTINOS VISITADOS ===")

print(f"El numero total de viajes ingresados son: {sumaDestinos(clientes, 1)}")