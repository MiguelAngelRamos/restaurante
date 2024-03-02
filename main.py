from restaurante.gestor_reservas import hacer_reservas, listar_reservas

def mostrar_menu():
    print("\n *** Menú del Sistema de Reservas del Restaurante Bucle Infinito ***")
    print("1. Hacer una reserva")
    print("2. Cancelar una reserva")
    print("3. Listar reservas para una fecha")
    print("4. Salir")
    opcion = input("Por favor, eliga una opción: ")
    return opcion

def procesar_opcion(opcion):
    if opcion == "1":
        fecha = input("Ingresa la fecha de la reserva (YYYY-MM-DD): ")
        nombre_cliente = input("Ingresa el nombre del cliente: ")
        hacer_reservas(fecha, nombre_cliente)
        
    elif opcion == "2":
        fecha = input("Ingresa la fecha de la reserva a cancelar (YYYY-MM-DD): ")
        nombre_cliente = input("Ingresa el nombre del cliente: ")
        # TODO: Aqui debo programar la lógica para cancelar la reserva
    elif opcion == "3":
        fecha = input("Ingresa la fecha para listar las reservas (YYYY-MM-DD): ")
        reservas = listar_reservas(fecha)
        if reservas:
            print("Reservas para", fecha, ":", ", ".join(reservas))
            # TODO: hacer ejercicios con metodod de listas
    elif opcion == "4":
        print("Saliendo del programa...")
    else:
        print("Opción no válida, Por favor, intenta de nuevo.")

if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        if opcion == "4":
            procesar_opcion(opcion)
            break
        procesar_opcion(opcion)

# print("hola mundo como estan,\n espero que muy bien este es un programa escrito python")
