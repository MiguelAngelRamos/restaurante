# Importa datetime para trabajar fechas
from datetime import datetime
from .utilidades import verificar_disponibilidad

# Diccionario que almacene las reservas
#* Las claves son las fechas
#* Los valores son las listas con los nombres de los clientes

reservas = {}

def hacer_reservas(fecha, nombre_cliente):
    # la fecha viene en formato str
    # Vamos a convertir la fecha de formato str a objeto de datetime, para gestionarla de manera en formato de fecha
    fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()

    if verificar_disponibilidad(fecha_obj):
        if fecha in reservas:
            reservas[fecha].append(nombre_cliente)
        else:
            # Sino creamos una entrada en el diccionario con esa fecha
            reservas[fecha] = [nombre_cliente]
        return True
    else: 
        return False
    

    # {
    #     "2024-04-15": ['miguel', 'macarena', 'romina']
    # }

def listar_reservas(fecha):
    return reservas.get(fecha, [])