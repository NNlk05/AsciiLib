# **AsciiLIB**

AsciiLIB is a simple Python library designed for developers looking to create retro-style text-based games and applications. It provides a straightforward Game class that abstracts the complexity of rendering a 2D character grid into a Tkinter window. This allows you to focus on your game's logic, "drawing" with characters, rather than the boilerplate of window management and screen-drawing.

This library is ideal for projects where a retro aesthetic is desired, such as simple roguelikes, MUDs, text adventures, or other ASCII-art-based applications. It prioritizes simplicity and ease of use over raw performance, making it perfect for game jams, educational purposes, or hobby projects.

The library also includes the CharLib utility, a comprehensive dictionary for easy access to a wide range of Unicode characters. This curated collection is perfect for building detailed text-based user interfaces and adding graphical flair to your project, removing the need to hunt down and copy-paste obscure glyphs.

## **Core Components**

- **Game (\_\_init\_\_.py):** This is the main class for creating an ASCII game surface. It functions as a high-level wrapper around a Tkinter Text widget, effectively turning it into a simple, addressable character grid. This means you don't need to learn the intricacies of Tkinter to get started. It manages an internal 2D list (a character buffer) that represents your screen, and provides straightforward drawing and event handling methods. The coordinate system is (x, y) with (0, 0\) in the top-left corner, and the buffer is indexed as content\[y\]\[x\]. The class handles the full-screen refresh internally—every time you call a drawing method, the changes are automatically "flushed" to the visible window.
- **CharLib (CharLib.py):** This module provides a large, pre-categorized Python dictionary of Unicode glyphs. It's designed to solve the problem of finding and managing the right characters for text-based UIs. Instead of hard-coding obscure Unicode characters (e.g., '╔', '═'), you can access them by a clear, readable name (e.g., CharLib\["PIPE_EXTENDED"\]\["DOUBLE_BOTTOM_LEFT_TURN"\]). This makes your drawing code far more maintainable. Categories include:
  - **MAIN:** Basic shapes like blocks, circles, and triangles.
  - **PIPE_ASCII:** Simple \+, \-, | for fallbacks.
  - **PIPE_EXTENDED:** A full suite of single-line, heavy, and double-line box-drawing characters.
  - **PIPE_BLOCKS:** Shading characters and half-blocks for more detailed graphics.
  - **BRAILLE:** The full set of 256 braille patterns. These are especially useful as they can be combined to create fine-grained 2x4 pixel-per-character graphics.

## **Features**

The Game class provides several fundamental methods for manipulating the character grid. All drawing methods automatically refresh the display, so you always see the latest state.

- set_char(xy, char): The most atomic drawing operation. This is the fundamental building block for all other drawing, setting a single character at a specific (x, y) coordinate in the buffer.
- draw_rectangle(top_left, bottom_right, border_char, fill_char): Draws a bordered rectangle. The top_left and bottom_right coordinates are inclusive. The border is made of border_char. If fill_char is provided (not None), the entire interior of the rectangle (exclusive of the border) is filled with that character.
- fill_area(top_left, bottom_right, char): A simpler fill operation that sets all characters within the specified rectangular bounds (inclusive) to char. This is useful for clearing large sections of the screen, drawing solid panels, or laying down a background.
- swap_area(rect1, top_left2): Swaps the contents of two rectangular regions of the same size. This is a surprisingly powerful method for buffer manipulation. You can use it to create pop-up dialogs (swapping the screen area to a buffer, drawing the dialog, then swapping back) or to implement efficient scrolling/panning of a map view.
- clear(): A utility method that resets the entire surface buffer to the default filler character you specified when creating the Game. This is perfect for transitions between game states or levels.
- on_key_press(callback), on_key_release(callback), on_mouse_click(callback): These methods bind basic user input to your functions. You pass a callback function (e.g., def my_handler(event): ...), which will be automatically called when the event occurs. The event object passed to your callback contains useful information, most notably event.keysym for key events, which gives you a string like "w", "Escape", or "Up".

## **Quick Start Example**

Here is a minimal example of how to use the Game class, with expanded comments to explain the logic.

```python
import AsciiLIB

# \--- Create the game window \---
# Create a 40-column by 10-row game window.
# The 'filler' is the default character used when clearing the screen.
game = AsciiLIB.Game(width=40, height=10, filler='.')

# --- Draw some static elements ---

# Set a single '@' character at (x=5, y=2)
# This will be our "player"
game.set_char((5, 2), '@')

# Draw a rectangle from (1,1) to (10,5)
# The border will be '*' and the inside will be filled with ' ' (space)
# This creates a simple "room" or "info box"
game.draw_rectangle((1, 1), (10, 5), border_char='*', fill_char=' ')

# Fill a solid block of '#' characters, like a wall or obstacle
game.fill_area((15, 2), (20, 4), '#')

# --- Set up event handling ---

# We need to store the player's position *outside* the handler
# so we can remember it between key presses.
# NOTE: The 'player_pos' tuple in handle_key is a FLAWED approach
# as the (5, 2) is hard-coded. A real game would use mutable variables.
player_x = 5
player_y = 2

# Define a function to handle key presses
def handle_key(event):
 global player_x, player_y # Tell the function to modify the global variables

    print(f"Key pressed: {event.keysym}")

    # Store the player's old position
    old_x, old_y = player_x, player_y

    # Simple movement logic based on the key symbol
    if event.keysym == 'w' or event.keysym == 'Up':
        player_y -= 1
    elif event.keysym == 's' or event.keysym == 'Down':
        player_y += 1
    elif event.keysym == 'a' or event.keysym == 'Left':
        player_x -= 1
    elif event.keysym == 'd' or event.keysym == 'Right':
        player_x += 1

    # --- Update the screen ---
    # Clear the old position by drawing the filler character
    game.set_char((old_x, old_y), '.')
    # Draw the player at the new position
    game.set_char((player_x, player_y), '@')

    # Use 'q' or 'Escape' to quit the application
    if event.keysym == 'q' or event.keysym == 'Escape':
        game.tk.destroy() # Close the Tkinter window

# Bind the 'handle_key' function to any key press event
game.on_key_press(handle_key)

# --- Start the application ---
# This call starts the Tkinter main loop.
# It's a blocking call, meaning your script will pause here
# while the window is open and listening for events.
game.tk.mainloop()
```

## **Credits**

The CharLib component and its organizational concept is inspired by fromariel's [ASCII/Unicode Grid Studio](https://fromariel.github.io/CODEXVault_GODOT/tools/ascii.html).

## **License**

This project is licensed under the **MIT License**. See the LICENSE file for complete details.
