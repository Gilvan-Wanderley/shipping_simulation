from ...simulater import Simulater
import tkinter as tk

class Flowsheet(tk.Canvas):
    def __init__(self, master: tk.Misc, simulater: Simulater) -> None:
        super().__init__(master, background='#0096C7',height=200, width=1030)
        self.create_rectangle((830, 0), (1040, 210) , fill='#DDD', )