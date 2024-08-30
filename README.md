# Project1PythonIronhack
En este primer proyecto hemos modificado un juego de tipo Escape room desarrollado en Python a partir de una código predifinido.
Hemos añadido una opción que es poner una palabra secreta para abrir una puerta, para asi de esta forma hacer el juego un poco mas dificil.

Aqui los diferentes enlaces para acceder al Google Coolab para poder jugar y a la presentación donde explicamos lo que hemos realizado.

https://colab.research.google.com/drive/1ep_6fBqWUJqg92pGSyuYahG9IYR2gLSr?authuser=0#scrollTo=xYWfAtnqcjdE

https://www.canva.com/design/DAGPJmmBt9A/EuDg0ztt-LqI1dTdPGCJSw/view?utm_content=DAGPJmmBt9A&utm_campaign=designshare&utm_medium=link&utm_source=editor

Para que el codigo funcione el archivo EscapeRoomFunctions debe estar en una carpeta en llamada Functions en el propio Google drive del usuario.

Aqui explico el funcionamiento del juego.

Este juego es una aventura interactiva de texto en la que el jugador debe explorar diferentes habitaciones, encontrar llaves y desbloquear puertas para finalmente escapar de la casa. Aquí te explico cómo funciona el juego, paso a paso:

Configuración del juego
Objetos y habitaciones: El juego define varias habitaciones (game_room, bedroom1, bedroom2, livingroom, outside) y objetos como muebles (couch, piano, queenbed, etc.), puertas (door_a, door_b, door_c, door_d) y llaves para algunas puertas (key_a, key_b, key_c).
Relaciones entre objetos: Las relaciones entre objetos y habitaciones se definen en el diccionario object_relations, que indica qué objetos se encuentran en cada habitación y qué habitaciones están conectadas por cada puerta.
Inicio del juego
El juego comienza con la función start_game(game_state), que introduce al jugador en la historia: se despierta en un sofá en una casa extraña y debe encontrar una forma de escapar.
El juego se inicia llamando a play_room(game_state, game_state["current_room"]), que gestiona la interacción del jugador dentro de la habitación actual.
Interacción del jugador
Explorar una habitación: El jugador puede optar por "explorar" la habitación actual, lo que le permite ver los objetos presentes en esa habitación (explore_room(room)).
Examinar un objeto: El jugador también puede optar por "examinar" un objeto en la habitación. Dependiendo del tipo de objeto, puede encontrar una llave, abrir una puerta o descubrir que el objeto no tiene nada interesante. Esto se maneja en examine_item(game_state, item_name).

Puertas y llaves
Algunas puertas requieren llaves para ser abiertas, y otras pueden requerir que el jugador ingrese una palabra secreta (como en el caso de "door d", que responde a la palabra secreta abracadabra).
Si el jugador tiene la llave correcta para una puerta, la función examine_item permitirá abrirla y mover al jugador a la siguiente habitación.

Progreso y finalización del juego
El jugador progresa de una habitación a otra resolviendo los desafíos de encontrar llaves y abrir puertas.
El objetivo final es alcanzar la "habitación objetivo", que en este caso es outside, lo que significa que el jugador ha escapado de la casa y ganado el juego.

Lógica principal
start_game(game_state): Introduce la historia y comienza la interacción.
play_room(game_state, room): Maneja la interacción en la habitación actual y repite el ciclo hasta que el jugador escape o decida detenerse.
explore_room(room): Permite al jugador ver qué objetos hay en la habitación.
examine_item(game_state, item_name): Permite al jugador interactuar con los objetos, abrir puertas y encontrar llaves.
get_next_room_of_door(door, current_room): Determina la habitación a la que lleva una puerta.

Ejemplo de Jugabilidad
El jugador se despierta en game_room y explora la habitación, descubriendo un piano y una door a.
Si examina el piano, encuentra la key for door a.
Luego, examina door a, usa la llave y pasa a bedroom1.
El jugador continúa explorando y encontrando llaves hasta que finalmente abre door d con la palabra secreta y escapa a outside, ganando el juego.
El juego es un sencillo "escape room" basado en texto donde el jugador resuelve pequeños acertijos y explora para encontrar una salida.







