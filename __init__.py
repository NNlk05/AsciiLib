import tkinter as tk

class Game:
    def __init__(self, width=80, height=60, filler=".", title="AsciiLIB game"):
        self.width = width
        self.height = height
        self.tk = tk.Tk()
        self.tk.title(title)
        self.area = tk.Text(self.tk, width=self.width, height=self.height, font=("Courier", 10))
        self.area.pack()

if __name__ == "__main__":
    game = Game()
    game.tk.mainloop()