import tkinter as tk
from .components import MenuBar, ContentLayout, Footer
from .model import Simulater

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self._simulater = Simulater()
        self.title('Shipping Simulation')
        self.geometry('1024x740')
        self.setup()
        self.mainloop()

    def setup(self) -> None:
        self._menubar = MenuBar(self, self.simulater)
        self._content = ContentLayout(self, self.simulater)
        self._footer = Footer(self, self.simulater)
        self.configure(menu=self._menubar)
        self._footer.pack(side='bottom', fill='x')
        self._content.pack(side='left', fill='both', expand=True)
    
    @property
    def simulater(self) -> Simulater:
        return self._simulater