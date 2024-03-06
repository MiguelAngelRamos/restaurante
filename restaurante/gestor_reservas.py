# Importa datetime para trabajar fechas
from datetime import datetime
from .utilidades import verificar_disponibilidad
from . import reservas


def hacer_reservas(fecha, hora, nombre_cliente):
    # la fecha viene en formato str
    # Vamos a convertir la fecha de formato str a objeto de datetime, para gestionarla de manera en formato de fecha
    # fecha_hora = f"{fecha} {hora}"
    # fecha_hora_obj = datetime.strptime(fecha_hora, '%Y-%m-%d %H:%M')

    if verificar_disponibilidad(fecha, hora):
        if fecha in reservas:
            reservas[fecha].append(nombre_cliente)
        else:
            # Sino creamos una entrada en el diccionario con esa fecha
            reservas[fecha] = [nombre_cliente]
        return True
    else: 
        return False

def cancelar_reserva(fecha, nombre_cliente):
    try:
        reservas[fecha].remove(nombre_cliente)
        return True
    except(KeyError, ValueError):
        return False

    # {
    #     "2024-04-15": ['miguel', 'macarena', 'romina']
    # }

def listar_reservas(fecha):
    return reservas.get(fecha, [])