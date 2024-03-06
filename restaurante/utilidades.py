from . import reservas
from datetime import datetime
# Total de Mesas del Restaurante
TOTAL_MESAS = 10

def verificar_disponibilidad(fecha, hora):
    # Convertimos la fecha y hora de un string a un objeto
    fecha_hora_obj = datetime.strptime(f'{fecha} {hora}', '%Y-%m-%d %H:%M')

    # Vamos estar disponibles (entre las 9:00 y 23:00)
    if not (9 <= fecha_hora_obj.hour < 23):
        return False # Estamos fuera del rango
    
    # Contador el numero de resaras
    num_reservas_para_fecha = len(reservas.get(fecha, []))
    return num_reservas_para_fecha < TOTAL_MESAS