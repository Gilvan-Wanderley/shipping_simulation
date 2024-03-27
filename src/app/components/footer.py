import tkinter as tk

class Footer(tk.Frame):
    def __init__(self, app) -> None:
        super().__init__(app, background='#ffffff') 

        self._label = tk.Label(self, 
                               text='Developed by Balkony - 2024®', 
                               background='#ffffff')
        
        self._label.pack(side='right', anchor=tk.W )