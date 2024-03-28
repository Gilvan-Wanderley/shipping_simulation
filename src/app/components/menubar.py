import tkinter as tk
from ..model import Simulater

class MenuBar(tk.Menu):
    def __init__(self, app: tk.Tk, simulater: Simulater) -> None:
        super().__init__(app)
        self._simulater = simulater
        
        self.options_menu = tk.Menu(self, tearoff=0)
        self.options_menu.add_command(label='Save', 
                                      command=self.save_command)
        self.options_menu.add_command(label='Save as', 
                                      command=self.save_as_command)
        self.options_menu.add_command(label='Load', 
                                      command=self.load_command)
        self.options_menu.add_separator()
        self.options_menu.add_command(label='Exit', 
                                      command=self.quit)
        
        self.add_cascade(label='Options', menu=self.options_menu)
        
        app.configure(menu=self)

    def save_command(self):
        pass

    def save_as_command(self):
        pass

    def load_command(self):
        pass
