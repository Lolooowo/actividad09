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
def mayorDestinos(clientes, codigo):
    if codigo == len(clientes):
        cliente = clientes[codigo]
        mayor = 0
        numeroDestinos = int
        for clave, valor in cliente["codigoDestino"].items():
            numeroDestinos = cliente["codigoDestino"]["numeroDestino"].get(clave, numeroDestinos)
            if  numeroDestinos > mayor:
                mayor = numeroDestinos
        return mayor
    else:
        cliente = clientes[codigo]
        mayor = 0
        numeroDestinos = int
        for clave, valor in cliente["codigoDestino"].items():
            numeroDestinos = cliente["codigoDestino"]["numeroDestino"].get(clave, numeroDestinos)            if numeroDeDestinos > mayor:
                mayor = numeroDestinos
        mayores = mayorDestinos(clientes, codigo + 1)
        if mayor > mayores:
            mayor = mayores

        return mayor



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
for codigo, cliente in clientes.items():
    print(f"\tCliente: {codigo}")
    print(f"\tNombre: {cliente['nombre']}")
    print(f"Destino")
print(f"El numero total de viajes ingresados son: {sumaDestinos(clientes, 1)}")
print(f"El que tiene mayor destinos es: {mayorDestinos(clientes, 1)}")