import tkinter as tk

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Shipping Simulation')
        self.geometry('1024x740')
        self.mainloop()