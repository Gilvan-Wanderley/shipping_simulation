from typing import Union
from tkinter import ttk
import tkinter as tk


class LabelVariable(ttk.Frame):
    def __init__(self, 
                 master, 
                 text: str, 
                 var: Union[tk.DoubleVar, tk.IntVar, tk.StringVar], 
                 unit:str = '') -> None:
        super().__init__(master)
        self._label = ttk.Label(self, text=text)
        self._var = ttk.Label(self, textvariable=var)
        self._unit = ttk.Label(self, text=unit)

        self._label.pack(side='left')
        self._var.pack(side='left')
        self._unit.pack(side='left', padx=2)


