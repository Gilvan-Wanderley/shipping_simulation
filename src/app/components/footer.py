import tkinter as tk
from ..model import Simulater


class Footer(tk.Frame):
    def __init__(self, app: tk.Tk, simulater: Simulater) -> None:
        super().__init__(app, background='#ffffff')
        self._simulater = simulater

        self._label = tk.Label(self, 
                               text='Developed by Balkony - 2024®', 
                               background='#ffffff')
        
        self._label.pack(side='right', anchor=tk.W )