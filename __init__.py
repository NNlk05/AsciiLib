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
    
    def _refresh_area(self):
        self.area.delete("1.0", END)
        for row in self.content:
            self.area.insert(END, "".join(row) + "\n")
    
    def set_char(self, xy=(0, 0), char=" "):
        x, y = xy
        if 0 <= x < self.width and 0 <= y < self.height:
            self.content[y][x] = char
            self._refresh_area()

if __name__ == "__main__":
    game = Game()
    game.tk.mainloop()