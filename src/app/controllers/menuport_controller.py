import tkinter as tk
from ..simulater import Simulater
from tkinter import messagebox

class MenuPortController():
    def __init__(self, simulater: Simulater, app) -> None:
        self._simulater = simulater
        self._app = app.master

    def update_command(self, num_berthsvar: tk.IntVar, unoading_ratevar: tk.DoubleVar) -> None:
        nun_berths = 0
        unoading_rate = 0.0

        try: 
            nun_berths = num_berthsvar.get()
            if nun_berths < 1:
                raise Exception()
            num_berthsvar.set(nun_berths)
        except:
            messagebox.showerror('Erro', 'Invalid value for Nº Berths!')
            num_berthsvar.set(1)
            return
        
        try: 
            unoading_rate = unoading_ratevar.get()
            if unoading_rate <= 0.0:
                raise Exception()
        except:
            messagebox.showerror('Erro','Invalid value for Unloading Rate!')
            unoading_ratevar.set(0.0)
            return
        
        self._simulater.builder.sim_obj.port.num_berths = nun_berths
        self._simulater.builder.sim_obj.port.unload_rate = unoading_rate
        messagebox.showinfo('Port','Port updated!')
        self._app.rerender()