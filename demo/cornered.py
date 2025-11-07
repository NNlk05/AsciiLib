import AsciiLIB as asl
import AsciiLIB.CharLib as cl

game = asl.Game(8, 8, " ", "Cornered")
is_player1_turn = True

player1_selected_index = 0
player2_selected_index = 0

for y in range(8):
    for x in range(8):
        if (x + y) % 2 == 0:
            game.set_char((x, y), cl["MAIN"]["LIGHT_SHADE"])
        else:
            game.set_char((x, y), cl["MAIN"]["DARK_SHADE"])

player1_pos = [[0,0], [0, 1], [0, 2], [0, 3], [0,4], [0,5], [0,6], [0,7]]
for pos in player1_pos:
    game.set_char((pos[0], pos[1]), cl["MAIN"]["CIRCLE_BLACK"])

player2_pos = [[7,7], [7,6], [7,5], [7,4], [7,3], [7,2], [7,1], [7,0]]
for pos in player2_pos:
    game.set_char((pos[0], pos[1]), cl["MAIN"]["CIRCLE_WHITE"])

def on_key_press(event):
    global is_player1_turn, player1_selected_index, player2_selected_index
    key = event.keysym
    
    if key == "Return":
        is_player1_turn = not is_player1_turn
        print(f"Switched turn to Player {1 if is_player1_turn else 2}")
    
    elif key in ["a", "d"]:
        if is_player1_turn:
            player1_selected_index = (player1_selected_index + (1 if key == "d" else -1)) % len(player1_pos)
            print(f"Player 1 selected piece index: {player1_selected_index}")
        else:
            player2_selected_index = (player2_selected_index + (1 if key == "d" else -1)) % len(player2_pos)
            print(f"Player 2 selected piece index: {player2_selected_index}")

    # Handle movement
    elif key in ["Up", "Down", "Left", "Right"]:
        if is_player1_turn:
            x, y = player1_pos[player1_selected_index]
            new_x, new_y = x, y

            if key == "Up" and y > 0:
                new_y -= 1
            elif key == "Down" and y < 7:
                new_y += 1
            elif key == "Left" and x > 0:
                new_x -= 1
            elif key == "Right" and x < 7:
                new_x += 1
            if game.get_char((new_x, new_y)) in [cl["MAIN"]["BLANK"], cl["MAIN"]["BLOCK"]]:
                game.swap_areas((x, y), (new_x, new_y))
                player1_pos[player1_selected_index] = [new_x, new_y]
                print(f"Player 1 moved to {(new_x, new_y)}")

        else:
            x, y = player2_pos[player2_selected_index]
            new_x, new_y = x, y

            if key == "Up" and y > 0:
                new_y -= 1
            elif key == "Down" and y < 7:
                new_y += 1
            elif key == "Left" and x > 0:
                new_x -= 1
            elif key == "Right" and x < 7:
                new_x += 1
                
            if game.get_char((new_x, new_y)) in [cl["MAIN"]["BLANK"], cl["MAIN"]["BLOCK"]]:
                game.swap_areas((x, y), (new_x, new_y))
                player2_pos[player2_selected_index] = [new_x, new_y] # Crucial: Update the list
                print(f"Player 2 moved to {(new_x, new_y)}")


game.on_key_press(on_key_press)
game.tk.mainloop()
