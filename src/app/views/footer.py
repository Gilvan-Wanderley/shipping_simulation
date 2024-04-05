import tkinter as tk
from ..simulater import Simulater


class Footer(tk.Frame):
    def __init__(self, app: tk.Tk, simulater: Simulater) -> None:
        super().__init__(app, background='#ffffff')
        self._simulater = simulater
        self.build_view()


    def build_view(self) -> None:
        self._name = 'Not file selected.'
        if self._simulater.handler_file.path != '':
            self._name = self._simulater.handler_file.path           
        self._label = tk.Label(self, 
                               text='Developed by Balkony - 2024®', 
                               background='#ffffff')
        
        self._file = tk.Label(self, text=f'File: {self._name}', background='#ffffff')
        
        self._label.pack(side='right', anchor=tk.W )
        self._file.pack(side='left', anchor=tk.W )

    def rerender(self) -> None:
        self._label.destroy()
        self._file.destroy()
        self.build_view()