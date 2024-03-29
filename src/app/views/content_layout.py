import tkinter as tk
from ..simulater import Simulater

class ContentLayout(tk.Frame):
    def __init__(self, app: tk.Tk, simulater: Simulater) -> None:
        super().__init__(app, background='#D9D9D9')
        
        self._frame_port = tk.Frame(self, height=50, width=50, background='blue')
        self._frame_ship = tk.Frame(self, height=50, width=50, background='blue')
        self._frame_animation = tk.Frame(self, height=50, width=100, background='blue')
        self._frame_resume = tk.Frame(self, height=50, width=50, background='blue')
        self._frame_results = tk.Frame(self, height=50, width=50, background='blue')

        self._frame_port.grid(row=0, column=0, 
                            sticky=tk.N+tk.S+tk.E+tk.W, 
                            pady=5, padx=5)
        self._frame_ship.grid(row=0, column=1, 
                              sticky=tk.N+tk.S+tk.W+tk.E,                             
                              pady=5, padx=5)
        self._frame_animation.grid(row=1, column=0, columnspan=2, 
                                   sticky=tk.N+tk.S+tk.W+tk.E,
                                   pady=5, padx=5)
        self._frame_resume.grid(row=2, column=0,
                                sticky=tk.N+tk.S+tk.E+tk.W,
                                pady=5, padx=5)
        self._frame_results.grid(row=2, column=1,
                                 sticky=tk.N+tk.S+tk.E+tk.W,
                                 pady=5, padx=5)