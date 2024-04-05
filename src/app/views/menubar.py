import tkinter as tk
from ..simulater import Simulater
from ..controllers import MenuBarController


class MenuBar(tk.Menu):
    def __init__(self, app, simulater: Simulater) -> None:
        super().__init__(app)
        self._app = app
        self._simulater = simulater
        self._controller = MenuBarController(simulater, app)
        self.build_view()        

    def build_view(self) -> None:
        self.options_menu = tk.Menu(self, tearoff=0)
        self.options_menu.add_command(label='Save', 
                                      command=self._controller.save_command)
        self.options_menu.add_command(label='Save as', 
                                      command=self._controller.save_as_command)
        self.options_menu.add_command(label='Load', 
                                      command=self._controller.load_command)
        self.options_menu.add_separator()
        self.options_menu.add_command(label='Exit', 
                                      command=self.quit)
        
        self.add_cascade(label='Options', menu=self.options_menu)
        
        self._app.configure(menu=self)
