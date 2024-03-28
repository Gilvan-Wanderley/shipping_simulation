import tkinter as tk
from ..models import Simulater


class Footer(tk.Frame):
    def __init__(self, app: tk.Tk, simulater: Simulater) -> None:
        super().__init__(app, background='#ffffff')
        self._simulater = simulater

        name = 'Not file selected.'
        if simulater.handler_file.path != '':
            name = simulater.handler_file.path 

        self._label = tk.Label(self, 
                               text='Developed by Balkony - 2024®', 
                               background='#ffffff')
        
        self._file = tk.Label(self, text=f'File: {name}', background='#ffffff')
        
        self._label.pack(side='right', anchor=tk.W )
        self._file.pack(side='left', anchor=tk.W )