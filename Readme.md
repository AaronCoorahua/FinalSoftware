Pregunta 3:

Podriamo agregar un nuevo atributo a la clase Cuenta para almacenar el número de mensajes enviados y un valor por mensaje. Además modificar el método pagar() para verificar si el destinatario es un contacto o "broadcast" y realizar las operaciones correspondientes. Por último dberíamos agregar un nuevo método en la clase Cuenta llamado broadcast() para enviar un mensaje a todos los contactos y actualizar el contador de mensajes enviados.
Los tests que deberiamos agregar serían 2:
- 1 test para comprobar el contador de mensajes enviados, y 1 test para cálculo del costo total de los mensajes.

El riesgo de introducir errores al modificar el código existente depende de la complejidad de los cambios y de la cobertura de pruebas que ya exista. Si el código actual cuenta con una buena cobertura de pruebas unitarias, es más probable que se detecten posibles errores antes de implementar los cambios.
