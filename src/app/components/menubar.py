import tkinter as tk

class MenuBar(tk.Menu):
    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root)
        self.options_menu = tk.Menu(self, tearoff=0)
        self.options_menu.add_command(label='Save', 
                                      command=self.save_command)
        self.options_menu.add_command(label='Save as', 
                                      command=self.save_as_command)
        self.options_menu.add_command(label='Load', 
                                      command=self.load_command)
        self.options_menu.add_separator()
        self.options_menu.add_command(label='Exit', 
                                      command=self.quit)
        
        self.add_cascade(label='Options', menu=self.options_menu)
        
        root.configure(menu=self)

    def save_command(self):
        pass

    def save_as_command(self):
        pass

    def load_command(self):
        pass
