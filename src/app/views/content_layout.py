import tkinter as tk
from ..simulater import Simulater
from .menuport import MenuPort
from .menuship import MenuShip
from .menubuilder import MenuBuilder
from .menuresults import MenuResults

class ContentLayout(tk.Frame):
    def __init__(self, app, simulater: Simulater) -> None:
        super().__init__(app, background='#D9D9D9')
        
        self._menu_port = MenuPort(self, simulater)
        self._menu_ship = MenuShip(self, simulater)
        self._frame_animation = tk.Frame(self, height=50, width=100, background='blue')
        self._menu_builder = MenuBuilder(self, simulater)
        self._menu_results = MenuResults(self, simulater)

        self._menu_port.grid(row=0, column=0, 
                            sticky=tk.N+tk.S+tk.E+tk.W, 
                            pady=5, padx=5)
        self._menu_ship.grid(row=0, column=1, 
                              sticky=tk.N+tk.S+tk.W+tk.E,                             
                              pady=5, padx=5)
        self._frame_animation.grid(row=1, column=0, columnspan=2, 
                                   sticky=tk.N+tk.S+tk.W+tk.E,
                                   pady=5, padx=5)
        self._menu_builder.grid(row=2, column=0,
                                sticky=tk.N+tk.S+tk.E+tk.W,
                                pady=5, padx=5)
        self._menu_results.grid(row=2, column=1,
                                 sticky=tk.N+tk.S+tk.E+tk.W,
                                 pady=5, padx=5)