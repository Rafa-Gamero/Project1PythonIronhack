secret_word = "abracadabra"

couch = {
    "name": "couch",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}

# Outside

door_d = {
    "name": "door d",
    "type": "door",
}
outside = {
    "name": "outside",
    "type": "room",
}

# Habitación 1

bedroom1 = {
    "name": "bedroom1",
    "type": "room",
}

door_b = {
    "name": "door b",
    "type": "door",
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

door_c = {
    "name": "door c",
    "type": "door",
}

queenbed = {
    "name": "queen bed",
    "type": "furniture",
}
# Habitación 2

bedroom2 = {
    "name": "bedroom2",
    "type": "room",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}





# Living Room

livingroom = {
    "name": "living room",
    "type": "room",
}

dining_table = {
    "name": "dining table",
    "type": "furniture",
}
door_d = {
    "name": "door d",
    "type": "door",
}

all_rooms = [game_room, bedroom1, bedroom2, livingroom, outside]

all_doors = [door_a, door_b, door_c, door_d]

object_relations = {
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "door a": [game_room, bedroom1],
    "bedroom1": [queenbed, door_a, door_b, door_c],
    "queen bed": [key_b],
    "door b": [bedroom1, bedroom2],
    "bedroom2": [double_bed, dresser, door_b],
    "double bed": [key_c],
    "dresser": [],
    "door c": [bedroom1, livingroom],
    "living room": [dining_table, door_c, door_d],
    "dining table": [],
    "door d": [livingroom, outside],
    "outside": [door_d]
}

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

# Esta funcion prepara el escenario y luego delega a play_room la lógica específica del juego según el estado actual.
def start_game(game_state):
    """
    Start the game
    """
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before.")
    print("You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    print("In the distance, you hear someone suddenly shout 'abracadabra'")
    print("Me: What's happening?")
    play_room(game_state, game_state["current_room"])

# Esta funcion gestiona las interacciones del jugador dentro de una habitación específica, permitiéndole explorar o examinar elementos, y repite el ciclo de interacción hasta que el jugador alcance la "habitación objetivo" o decida hacer otra cosa.
def play_room(game_state, room):
    game_state["current_room"] = room
    if room == game_state["target_room"]:
        print("Congrats! You escaped the room!")
    else:
        print("You are now in " + room["name"])
        action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        if action == "explore":
            explore_room(room)
        elif action == "examine":
            examine_item(game_state, input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean.")
        play_room(game_state, room)

#Esta funcion permite al jugador explorar una habitación específica dentro del juego y describe los objetos que se encuentran en ella.
def explore_room(room):
    items = ", ".join(i["name"] for i in object_relations[room["name"]])
    print(f"You explore the room. This is {room['name']}. You find {items}")


# Esta funcion determina a qué habitación lleva una puerta en función de la habitación en la que el jugador se encuentra actualmente.
def get_next_room_of_door(door, current_room):
    return next(room for room in object_relations[door["name"]] if room != current_room)

#Esta funcion permite al jugador examinar un objeto específico en la habitación actual y manejar la interacción con dicho objeto, que puede ser una puerta u otro tipo de ítem.
def examine_item(game_state, item_name):
    current_room, next_room = game_state["current_room"], None
    for item in object_relations[current_room["name"]]:
        if item["name"] == item_name:
            output = f"You examine {item_name}. "
            if item["type"] == "door":
                have_key = any(key["target"] == item for key in game_state["keys_collected"])
                if item["name"] == "door d":
                    if input("The door responds to words. Enter the secret word: ").strip() == secret_word:
                        output += "The door opens."
                        next_room = get_next_room_of_door(item, current_room)
                    else:
                        output += "The word seems incorrect."
                elif have_key:
                    output += "You unlock it with a key."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It's locked and you don't have the key."
            else:
                if item["name"] in object_relations and object_relations[item["name"]]:
                    found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(found)
                    output += f"You find {found['name']}."
                else:
                    output += "There isn't anything interesting."
            print(output)
            break
    else:
        print("Item not found in the current room.")
    
    if next_room and input("Go to the next room? 'yes' or 'no'").strip().lower() == 'yes':
        play_room(game_state, next_room)
    else:
        play_room(game_state, current_room)