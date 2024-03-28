import tkinter as tk
from ..models import Simulater

class ContentLayout(tk.Frame):
    def __init__(self, app: tk.Tk, simulater: Simulater) -> None:
        super().__init__(app, background='#D9D9D9')
        self._simulater = simulater