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
    

if __name__ == "__main__":
    game = Game()
    game.tk.mainloop()