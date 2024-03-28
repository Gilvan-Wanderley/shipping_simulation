import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from ..models import Simulater

class MenuBar(tk.Menu):
    def __init__(self, app, simulater: Simulater) -> None:
        super().__init__(app)
        self._app = app
        self._simulater = simulater

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
        
        app.configure(menu=self)

    def save_command(self):
        if self._simulater.handler_file.path == '':
            if not self._is_selected():
                return
        self._save()

    def save_as_command(self):
        if not self._is_selected():
            return
        self._save()

    def load_command(self):
        new_path = filedialog.askopenfilename(defaultextension=".bky", 
                                              filetypes=[("Balkony files", 
                                                          "*.bky")])
        if new_path=='':
            return
        simulation_obj = self._simulater.handler_file.load_obj(new_path)
        #Need a build model
        pass


    def _is_selected(self) -> bool:
        self._simulater.handler_file.path = filedialog.asksaveasfilename(defaultextension=".bky", 
                                                                         filetypes=[("Balkony files",
                                                                                     "*.bky")])
        if self._simulater.handler_file.path == '':
            return False
        return True
    
    def _save(self) -> None:
        self._simulater.handler_file.save_file()
        messagebox.showinfo('Saved', 'Simulation saved successfuly.')
        self._app.rerender()