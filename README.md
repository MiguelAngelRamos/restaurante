

### Sistema de Gestión de Reservas para Restaurante "El Bucle infinito"

**Contexto:**

El restaurante "El Bucle Infinito" busca implementar un sistema informático que le permita gestionar de manera eficiente las reservas de sus mesas. Dada la popularidad del restaurante, es crucial contar con un sistema que permita tanto a los clientes como al personal realizar, cancelar y consultar reservas de manera sencilla y efectiva. El objetivo es maximizar la satisfacción del cliente y la ocupación del restaurante.

**Requerimientos:**

1. **Crear un sistema de reservas inicial**: El sistema debe iniciar con una configuración básica que permita realizar operaciones de reserva. Se asume que el restaurante tiene una capacidad fija de mesas, pero el sistema debe ser flexible para gestionar las reservas según la demanda.

2. **Hacer Reservas**: Los clientes o el personal del restaurante deben poder hacer reservas indicando el nombre del cliente y la fecha de la reserva. La fecha puede ingresarse en diferentes formatos, pero el sistema debe procesarla de manera uniforme para evitar confusiones.

3. **Cancelar Reservas**: Debe ser posible cancelar una reserva existente, especificando el nombre del cliente y la fecha de la reserva.

4. **Listar Reservas**: El sistema debe ofrecer la capacidad de listar todas las reservas existentes para una fecha específica, proporcionando una visión clara de la ocupación del restaurante.

5. **Interfaz de Usuario**: Implementar un menú interactivo que permita a los usuarios (personal del restaurante o clientes que llaman por teléfono) seleccionar entre hacer una reserva, cancelar una reserva o listar las reservas para una fecha específica.

6. **Flexibilidad en el Formato de Fecha**: Aunque el sistema puede preferir un formato de fecha específico internamente (por ejemplo, YYYY-MM-DD), debe ofrecer flexibilidad para aceptar diferentes formatos de entrada (por ejemplo, DD-MM-YYYY), y convertirlos al formato estándar utilizado por el sistema.

**Consideraciones Adicionales:**

- El sistema debe ser capaz de manejar errores comunes, como intentos de reservar para fechas pasadas, cancelaciones de reservas no existentes y formatos de fecha incorrectos.
  
- La implementación inicial puede asumir que todas las operaciones se realizan para el mismo día y no requiere autenticación de usuarios.

- La interfaz de usuario debe ser clara y amigable, proporcionando mensajes adecuados para confirmar las acciones realizadas o informar sobre errores.
