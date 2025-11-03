import tkinter as tk
END = tk.END

class Game:
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
                
