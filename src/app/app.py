import tkinter as tk
from .components import MenuBar, ContentLayout

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Shipping Simulation')
        self.geometry('1024x740')
        self.setup()
        self.mainloop()

    def setup(self) -> None:
        self._menubar = MenuBar(self)
        self.configure(menu=self._menubar)
        self._content = ContentLayout(self)
        self._content.pack(side='left', fill='both', expand=True)


        pass