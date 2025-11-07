import AsciiLIB as asl
import AsciiLIB.CharLib as cl

game = asl.Game(8, 8, " ", "Cornered")
is_player1_turn = True

for y in range(8):
    for x in range(8):
        if (x + y) % 2 == 0:
            game.set_char((x, y), cl["MAIN"]["BLANK"])
        else:
            game.set_char((x, y), cl["MAIN"]["BLOCK"])

player1_pos = [[0,0], [0, 1], [0, 2], [0, 3], [0,4], [0,5], [0,6], [0,7]]
for pos in player1_pos:
    game.set_char((pos[0], pos[1]), cl["MAIN"]["CIRCLE_BLACK"])

player2_pos = [[7,7], [7,6], [7,5], [7,4], [7,3], [7,2], [7,1], [7,0]]
for pos in player2_pos:
    game.set_char((pos[0], pos[1]), cl["MAIN"]["CIRCLE_WHITE"])

def on_key_press(event):
    global is_player1_turn
    key = event.keysym
    if key == "Return":
        is_player1_turn = not is_player1_turn
    elif key in ["Up", "Down", "Left", "Right"]:
        if is_player1_turn:
            for pos in player1_pos:
                if game.get_char((pos[0], pos[1])) == cl["MAIN"]["CIRCLE_BLACK"]:
                    x, y = pos
                    if key == "Up" and y > 0:
                        game.swap_areas((x, y), (x, y - 1))
                    elif key == "Down" and y < 7:
                        game.swap_areas((x, y), (x, y + 1))
                    elif key == "Left" and x > 0:
                        game.swap_areas((x, y), (x - 1, y))
                    elif key == "Right" and x < 7:
                        game.swap_areas((x, y), (x + 1, y))
                    break
        else:
            for pos in player2_pos:
                if game.get_char((pos[0], pos[1])) == cl["MAIN"]["CIRCLE_WHITE"]:
                    x, y = pos
                    if key == "Up" and y > 0:
                        game.swap_areas((x, y), (x, y - 1))
                    elif key == "Down" and y < 7:
                        game.swap_areas((x, y), (x, y + 1))
                    elif key == "Left" and x > 0:
                        game.swap_areas((x, y), (x - 1, y))
                    elif key == "Right" and x < 7:
                        game.swap_areas((x, y), (x + 1, y))
                    break

game.on_key_press(on_key_press)
game.tk.mainloop()