import tkinter as tk

END = tk.END

class Game:
    """
    Game(width=128, height=171, filler=" ", title="AsciiLIB Game")
    A simple ASCII "game" surface implemented on top of a Tkinter Text widget.
    The Game class manages a 2D character buffer (content) and renders it into
    a Tk Text widget. Coordinates are (x, y) with (0, 0) at the top-left corner;
    x is the column index and y is the row index.
    Parameters
    ----------
    width : int, optional
        Number of columns in the game surface (default 128).
    height : int, optional
        Number of rows in the game surface (default 171).
    filler : str, optional
        Single-character string used to initialize empty cells (default " ").
    title : str, optional
        Window title for the underlying Tk root (default "AsciiLIB Game").
    Attributes
    ----------
    width : int
        Surface width (number of columns).
    height : int
        Surface height (number of rows).
    filler : str
        Character used to initialize and clear the surface.
    tk : tkinter.Tk
        The Tk root window created for the game.
    area : tkinter.Text
        The Text widget used to display the ASCII surface. Configured with a
        monospaced font and black background by default.
    content : list[list[str]]
        2D list of characters representing the surface content. Indexed as
        content[y][x].
    Behavior summary
    ----------------
    - The text widget is filled by joining each row (list of characters) with
      no separator and appending a newline. The helper method _refresh_area()
      clears and re-inserts the entire content into the Text widget.
    - All public drawing/modification methods call _refresh_area() after
      performing changes, so the displayed text always reflects the buffer.
    - Coordinates and rectangles are clamped to the surface bounds where appropriate.
    Public methods
    --------------
    set_char(xy=(0, 0), char=" ")
        Set the single character at position (x, y) if the coordinates are within
        bounds. The display is refreshed after the change.
    clear()
        Reset the entire surface to the filler character and refresh the display.
    fill_area(top_left=(0, 0), bottom_right=None, char=" ")
        Fill a rectangular region (inclusive) with the provided char. If
        bottom_right is None, the region covers to the bottom-right corner of
        the surface. Coordinates outside the surface are ignored/clamped.
    swap_area(top_left1=(0, 0), bottom_right1=None, top_left2=(0, 0))
        Swap the contents of two rectangular regions of the same size. The first
        rectangle is defined by top_left1 and bottom_right1 (inclusive).
        If bottom_right1 is None, the first rectangle defaults to the entire
        surface. The second rectangle's top-left is top_left2; its size is taken
        from the first rectangle. Only overlapping in-bounds cells are swapped.
        The display is refreshed after the operation.
    draw_rectangle(top_left=(0, 0), bottom_right=None, border_char="#", fill_char=None)
        Draw a rectangle border using border_char. If bottom_right is None, the
        rectangle extends to the bottom-right corner of the surface. If
        fill_char is provided (not None), the rectangle interior (exclusive of
        the border) is filled with fill_char. Coordinates are inclusive and
        clamped to surface bounds. The display is refreshed after the draw.
    on_key_press(callback)
        Register a callback for Tk "<KeyPress>" events. The callback will
        receive the Tk event object.
    on_key_release(callback)
        Register a callback for Tk "<KeyRelease>" events.
    on_mouse_click(callback)
        Register a callback for Tk "<Button>" (mouse click) events.
    Notes and usage tips
    --------------------
    - This class creates a Tk root (self.tk) but does not call mainloop().
      After constructing Game and attaching any event callbacks, you must call
      game.tk.mainloop() (or integrate into your own Tk mainloop) to start the UI.
    - Rendering strategy: the entire Text widget is cleared and repopulated on
      each change. For very large surfaces or frequent updates, this may be
      inefficient; consider batching updates or modifying the Text widget more
      incrementally if performance is a concern.
    - No explicit validation is performed on characters passed in (char,
      border_char, fill_char). It is assumed these are single-character strings.
    - swap_area computes width and height as inclusive differences between the
      two corners; ensure the intended rectangle sizes and positions do not
      overlap incorrectly when swapping.
    - The coordinate system and rectangle endpoints are inclusive: both x1 and x2,
      y1 and y2, if provided, are treated as part of the rectangle.
    Example
    -------
    >>> game = Game(width=40, height=10, filler='.')
    >>> game.set_char((5, 2), '@')
    >>> game.draw_rectangle((1,1), (10,5), border_char='*', fill_char=' ')
    >>> game.fill_area((15,2), (20,4), '#')
    >>> game.on_key_press(lambda e: print('Pressed', e.keysym))
    >>> game.tk.mainloop()
    """
    def __init__(self, width=128, height=171, filler=" ", title="AsciiLIB Game"):
        self.width = width
        self.height = height

        self.filler = filler
        
        self.tk = tk.Tk()
        self.tk.title(title)
        self.area = tk.Text(self.tk, width=self.width, height=self.height, font=("Courier", 10), fg="white", bg="black")
        
        self.content = [[self.filler for _ in range(self.width)] for _ in range(self.height)]
        for row in self.content:
            self.area.insert(END, "".join(row) + "\n")
        self.area.pack()
    
    # HELPER METHODS #
    def _refresh_area(self):
        self.area.delete("1.0", END)
        for row in self.content:
            self.area.insert(END, "".join(row) + "\n")
    
    def set_char(self, xy=(0, 0), char=" "):
        x, y = xy
        if 0 <= x < self.width and 0 <= y < self.height:
            self.content[y][x] = char
        self._refresh_area()
        
    
    # BASIC METHODS #
    
    def clear(self):
        self.content = [[self.filler for _ in range(self.width)] for _ in range(self.height)]
        self._refresh_area()
    
    def fill_area(self, top_left=(0, 0), bottom_right=None, char=" "):
        if bottom_right is None:
            bottom_right = (self.width - 1, self.height - 1)
        x1, y1 = top_left
        x2, y2 = bottom_right
        for y in range(y1, min(y2 + 1, self.height)):
            for x in range(x1, min(x2 + 1, self.width)):
                self.content[y][x] = char
        self._refresh_area()
    
    def swap_area(self, top_left1=(0, 0), bottom_right1=None, top_left2=(0, 0)):
        if bottom_right1 is None:
            bottom_right1 = (self.width - 1, self.height - 1)
        x1a, y1a = top_left1
        x1b, y1b = bottom_right1
        x2a, y2a = top_left2
        
        width = x1b - x1a + 1
        height = y1b - y1a + 1
        
        for y in range(height):
            for x in range(width):
                if (0 <= x1a + x < self.width and 0 <= y1a + y < self.height and
                    0 <= x2a + x < self.width and 0 <= y2a + y < self.height):
                    self.content[y1a + y][x1a + x], self.content[y2a + y][x2a + x] =  self.content[y2a + y][x2a + x], self.content[y1a + y][x1a + x]
        self._refresh_area()

    def draw_rectangle(self, top_left=(0, 0), bottom_right=None, border_char="#", fill_char=None):
        if bottom_right is None:
            bottom_right = (self.width - 1, self.height - 1)
        x1, y1 = top_left
        x2, y2 = bottom_right
        
        for x in range(x1, min(x2 + 1, self.width)):
            if 0 <= y1 < self.height:
                self.content[y1][x] = border_char
            if 0 <= y2 < self.height:
                self.content[y2][x] = border_char
        
        for y in range(y1, min(y2 + 1, self.height)):
            if 0 <= x1 < self.width:
                self.content[y][x1] = border_char
            if 0 <= x2 < self.width:
                self.content[y][x2] = border_char
        
        if fill_char is not None:
            for y in range(y1 + 1, min(y2, self.height)):
                for x in range(x1 + 1, min(x2, self.width)):
                    self.content[y][x] = fill_char
        
        self._refresh_area()
    
    def get_char(self, xy=(0, 0)):
        x, y = xy
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.content[y][x]
        return None
    
    # EVENT LISTENERS #

    def _define_event_listener(self, event, callback):
        self.tk.bind(event, callback)
    
    def on_key_press(self, callback):
        self._define_event_listener("<KeyPress>", callback)
    
    def on_key_release(self, callback):
        self._define_event_listener("<KeyRelease>", callback)
    
    def on_mouse_click(self, callback):
        self._define_event_listener("<Button>", callback)
    
    

if __name__ == "__main__":
    game = Game()
    def fill_next(x=0, y=0):
        if x >= game.width:
            return
        game.set_char((x, y), "*")
        nx, ny = x, y + 1
        if ny >= game.height:
            nx += 1
            ny = 0
        game.tk.after(int(1000 / 60), lambda: fill_next(nx, ny))

    game.tk.after(0, fill_next)
    game.tk.mainloop()
                
