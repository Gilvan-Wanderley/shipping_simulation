import tkinter as tk
from ..simulater import Simulater
from .menuport import MenuPort
from .menuship import MenuShip
from .menubuilder import MenuBuilder
from .menuresults import MenuResults
from .flowsheet import Flowsheet

class ContentLayout(tk.Canvas):
    def __init__(self, root, simulater: Simulater) -> None:
        super().__init__(root, background='#D9D9D9')
        self._frame = tk.Frame(self)
        self.create_window((0, 0), window=self._frame, anchor="nw")
        self._flowsheet = Flowsheet(self._frame)
        simulater.set_flowsheet(self._flowsheet)
        self._simulater = simulater
        self.build_view()

    def build_view(self) -> None:
        self._menu_port = MenuPort(self._frame, self._simulater)
        self._menu_ship = MenuShip(self._frame, self._simulater)
        self._menu_builder = MenuBuilder(self._frame, self._simulater)
        self._menu_results = MenuResults(self._frame, self._simulater)

        self._menu_port.grid(row=0, column=0, 
                            sticky=tk.N+tk.S+tk.E+tk.W, 
                            pady=5, padx=5)
        self._menu_ship.grid(row=0, column=1, 
                              sticky=tk.N+tk.S+tk.W+tk.E,                             
                              pady=5, padx=5)
        self._flowsheet.grid(row=1, column=0, columnspan=2, 
                                   sticky=tk.N+tk.S+tk.W+tk.E,
                                   pady=5, padx=5)
        self._menu_builder.grid(row=2, column=0,
                                sticky=tk.N+tk.S+tk.E+tk.W,
                                pady=5, padx=5)
        self._menu_results.grid(row=2, column=1,
                                 sticky=tk.N+tk.S+tk.E+tk.W,
                                 pady=5, padx=5)
        
        self.scrollbar = tk.Scrollbar(self._frame, orient=tk.VERTICAL, command=self.yview)
        self.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, rowspan=3, sticky=tk.N+tk.S+tk.E)
        self.bind("<Configure>", self.on_canvas_configure) 
    
    def on_canvas_configure(self, event):
        self.configure(scrollregion=self.bbox("all"))

    def rerender(self):
        self._menu_port.destroy()
        self._menu_ship.destroy()
        self._menu_builder.destroy()
        self._menu_results.destroy()
        self.build_view()