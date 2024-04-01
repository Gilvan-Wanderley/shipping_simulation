import tkinter as tk
from tkinter import messagebox
from ..simulater import Simulater


class MenuBuilderController:
    def __init__(self, simulater: Simulater, app) -> None:
        self._simulater = simulater
        self._app = app.master

    def run_simulation_command(self, end_timevar: tk.DoubleVar):
         if not self._simulater.builder.sim_obj.port.is_complete():
            messagebox.showerror('Erro', 'The port must be configured!')
            return
        
         if not self._simulater.builder.sim_obj.ships.is_complete():
            messagebox.showerror('Erro', 'At least one ship is needed!')
            return
        
         end_time = 0.0
         try:
            end_time = end_timevar.get()
            if end_time <= 0.0:
                raise Exception()
         except:
            messagebox.showerror('Erro', 'Invalid value for run until')
            end_timevar.set(0.0)
            return
        
         self._simulater.run_up(end_time) 
         self._app.rerender()