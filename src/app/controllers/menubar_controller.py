from tkinter import filedialog
from tkinter import messagebox
from ..models import Simulater

class MenuBarController():
    def __init__(self, simulater: Simulater) -> None:
            self._simulater = simulater

    def save_command(self) -> None:
        if self._simulater.handler_file.path == '':
            if not self._is_selected():
                return
        self._save()
    
    def save_as_command(self) -> None:
        if not self._is_selected():
            return
        self._save()
    
    def load_command(self) -> None:
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
        self._simulater.handler_file.save_file() #Need a build model as a input here
        messagebox.showinfo('Saved', 'Simulation saved successfuly.')
        self._app.rerender()