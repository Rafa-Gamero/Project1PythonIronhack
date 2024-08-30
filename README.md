# Project1PythonIronhack

## Escape Room - Python Game Project by Rafa, Gabriela, Carlos and Ambar

This project is a modification of a text-based Escape Room game developed in Python using predefined code. Our team has added a new feature where the player must input a secret word to unlock a door, adding an extra layer of difficulty to the game.
This README is available in multiple languages.

## Available Languages

- [English (Inglés)](README.md)
- [Español (Spanish)](README.spanish.md)
  
### Project Links

- **Play on Google Colab:** [Escape Room on Google Colab](https://colab.research.google.com/drive/1ep_6fBqWUJqg92pGSyuYahG9IYR2gLSr?authuser=0#scrollTo=xYWfAtnqcjdE)
- **Project Presentation:** [Presentation on Canva](https://www.canva.com/design/DAGPJmmBt9A/EuDg0ztt-LqI1dTdPGCJSw/view?utm_content=DAGPJmmBt9A&utm_campaign=designshare&utm_medium=link&utm_source=editor)

> **Note:** To ensure the code runs correctly, the file `EscapeRoomFunctions.py` must be placed in a folder named `Functions` within your Google Drive.

### Game Description

This game is an interactive text-based adventure where the player must explore different rooms, find keys, and unlock doors to eventually escape the house. Here's how the game works:

#### 1. **Game Setup**

- **Objects and Rooms:** The game defines several rooms (`game_room`, `bedroom1`, `bedroom2`, `livingroom`, `outside`) and objects like furniture (`couch`, `piano`, `queenbed`, etc.), doors (`door_a`, `door_b`, `door_c`, `door_d`), and keys for some doors (`key_a`, `key_b`, `key_c`).
- **Object Relationships:** The relationships between objects and rooms are defined in the `object_relations` dictionary, which indicates what objects are in each room and which rooms are connected by each door.

#### 2. **Starting the Game**

The game begins with the `start_game(game_state)` function, which introduces the player to the story: they wake up on a couch in a strange house and must find a way to escape. The game proceeds by calling `play_room(game_state, game_state["current_room"])`, which manages the player's interactions within the current room.

#### 3. **Player Interaction**

- **Explore a Room:** The player can choose to "explore" the current room, allowing them to see the objects present in that room (`explore_room(room)`).
- **Examine an Object:** The player can also choose to "examine" an object in the room. Depending on the type of object, they may find a key, unlock a door, or discover that the object has nothing interesting. This is handled in `examine_item(game_state, item_name)`.

#### 4. **Doors and Keys**

Some doors require keys to be opened, while others may require the player to input a secret word (such as "door d," which responds to the secret word `abracadabra`). If the player has the correct key for a door, the `examine_item` function will allow them to open it and move to the next room.

#### 5. **Game Progression and Completion**

The player progresses from one room to another by solving challenges to find keys and unlock doors. The ultimate goal is to reach the "target room," which in this case is `outside`, meaning the player has successfully escaped the house and won the game.

### Main Logic

- **`start_game(game_state)`:** Introduces the story and starts the interaction.
- **`play_room(game_state, room)`:** Manages interaction in the current room and repeats the cycle until the player escapes or decides to stop.
- **`explore_room(room)`:** Allows the player to see what objects are in the room.
- **`examine_item(game_state, item_name)`:** Enables the player to interact with objects, unlock doors, and find keys.
- **`get_next_room_of_door(door, current_room)`:** Determines which room a door leads to.

### Gameplay Example

The player wakes up in `game_room` and explores the room, discovering a piano and `door_a`. If they examine the piano, they find the `key_for_door_a`. Then, they examine `door_a`, use the key, and proceed to `bedroom1`. The player continues exploring and finding keys until they eventually open `door_d` with the secret word and escape to `outside`, winning the game.




