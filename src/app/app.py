import tkinter as tk
from .components import MenuBar

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Shipping Simulation')
        self.geometry('1024x740')
        self.setup()
        self.mainloop()

    def setup(self) -> None:
        self.menubar = MenuBar(self)
        self.configure(menu=self.menubar)


        pass