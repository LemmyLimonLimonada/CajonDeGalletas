# Tarea 2: DCCombatientes 🐈


**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

El código implementa un sistema de combate entre diferentes tipos de combatientes, que pueden evolucionar y usar items para mejorar sus habilidades. Además, maneja la creación y gestión de un ejército de gatos combatientes.

### Cosas implementadas y no implementadas :white_check_mark: :x:

- 🟠 PEP8: Debido a la longitud de mis variables, muchas veces tuve que pasar mas de las 100 caracteres de longitud.

- ✅ Sistema de combate: El código permite que los combatientes se enfrenten entre sí en combates por turnos, con diversas estadísticas que influyen en el resultado. La mayor parte del sistema de combate esta redactado como una funcion de la clase Ejercito en gato.py en donde se reciben dos objetos de clase Ejercito y usando la lista que tiene de propiedad en donde se encuentran los objetos de clase Combatiente, se enfrentan hasta que alguno de las dos listas se encuentre vacia. El combate trata de ser lo mas informativo posible explicando daños recibidos, causados y que clase de enemigo se esta enfrentando nuestro gato. Cuando el ejercito enemigo se queda sin gatos se avanza a la siguiente ronda hasta ganar, en donde se cerrara el programa automaticamente. Ocurrira igual si el jugador pierde la partida. 

- ✅ Creación de gatos: Se pueden cargar datos desde archivos de texto para crear gatos con estadísticas personalizadas.

- ✅ Evolución de gatos: Los gatos pueden evolucionar a clases superiores utilizando items específicos.

- ✅ Uso de items: Existen diferentes items, como pergaminos y lanzas, que pueden ser utilizados para mejorar las habilidades de los gatos. Estos item son objetos con herencia con uso exclusivo para los objetos de clase Combatiente. 

- ✅ Manejo de oro: El sistema de oro permite comprar items y pagar por la evolución de los gatos asi como se asegura que haya una compra efectiva antes de reducir el oro. Estos casos pueden ocurrir al comprar un item sin tener gatos o que selecciones la evolucion de un gato con el item equivocado.

- ✅ Menús interactivos: Se implementa varios menú interactivo para que el usuario pueda realizar diferentes acciones, como combatir, presentar el ejército, comprar items y evolucionar personajes.

- ❌ Validación de datos: Aunque se espera que los datos cargados sean válidos, no se implementa una validación exhaustiva de los mismos al momento en el que redacto esto. Es decir, si se hacen gatos con atributos invalidos no ocurrira nada y el programa seguria con normalidad. Aunque hice una funcion para revisar que los datos fueran correctos no lo termine de usar.




## Ejecución :computer:
Para ejecutar el código, se deben utilizar los módulos principales gato.py, main.py, parametros.py y data/*.txt.


## Librerías :books:
### Librerías externas utilizadas
Se utilizan las siguientes librerías externas:

1. os: Para manejar operaciones del sistema, como la verificación de la existencia de archivos.
2. random: Para generar números aleatorios en el sistema de combate.

## Supuestos y consideraciones adicionales :thinking:
1. Se asume que los datos cargados desde archivos de texto tienen un formato válido y coherente.
2. No se realiza una validación exhaustiva de los datos ingresados por el usuario en el menú interactivo.


## Referencias de código externo :book:

No se menciona explícitamente ninguna referencia de código externo.

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/main/Tareas/Bases%20Generales%20de%20Tareas%20-%20IIC2233.pdf).