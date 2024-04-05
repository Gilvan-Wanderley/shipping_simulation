from ..simulater import Simulater
from ..utils.objs import ShipPropertiesValueObject
from tkinter import messagebox
import tkinter as tk


class MenuShipController():
    def __init__(self, simulater: Simulater, app) -> None:
        self._simulater = simulater
        self._app = app.master

    def create_command(self, namevar: tk.StringVar, capacityvar: tk.DoubleVar, frequencyvar: tk.DoubleVar):
        name = namevar.get()
        if name in self._simulater.builder.sim_obj.ships.ships_names():
            messagebox.showerror('Erro', 'There is a ship with this name, change ship name!')
            return

        capacity = self._validate_capacity(capacityvar)
        if type(capacity) is Exception:
            return 

        frequency = self._validate_frequency(frequencyvar)
        if type(frequency) is Exception:
            return 
        
        self._simulater.builder.sim_obj.ships.add(ShipPropertiesValueObject(**{'name':name, 
                                                                                     'capacity':capacity, 
                                                                                     'frequency': frequency}))
        messagebox.showinfo('Ship','Ship created successfully.')
        self._app.rerender()

    def update_command(self, namevar: tk.StringVar, capacityvar: tk.DoubleVar, frequencyvar: tk.DoubleVar):
        name = namevar.get()
        if name not in self._simulater.builder.sim_obj.ships.ships_names():
            messagebox.showerror('Erro', "There isn't a ship with this name, change ship name!")
            return
        
        capacity = self._validate_capacity(capacityvar)
        if type(capacity) is Exception:
            return 

        frequency = self._validate_frequency(frequencyvar)
        if type(frequency) is Exception:
            return 

        self._simulater.builder.sim_obj.ships.edit(name, capacity, frequency)
        messagebox.showinfo('Ship','Ship edited successfully.')
        self._app.rerender()

    def delete_command(self, namevar: tk.StringVar):
        name = namevar.get()
        if name not in self._simulater.builder.sim_obj.ships.ships_names():
            messagebox.showerror('Erro', "There isn't a ship with this name, change ship name!")
            return

        self._simulater.builder.sim_obj.ships.remove(name)
        messagebox.showinfo('Ship','Ship removed successfully.')
        self._app.rerender()

    def _validate_capacity(self, capacityvar: tk.DoubleVar) -> float:
        try:
            capacity = capacityvar.get()
            if capacity <= 0.0:
                raise Exception()
            capacityvar.set(capacity)
        except:
            messagebox.showerror('Erro', 'Invalid value for Capacity!')
            capacityvar.set(0.0)
            return Exception()
        return capacity

    def _validate_frequency(self, frequencyvar: tk.DoubleVar) -> float:
        try:
            frequency = frequencyvar.get()
            if frequency <= 0.0:
                raise Exception()
            frequencyvar.set(frequency)
        except:
            messagebox.showerror('Erro', 'Invalid value for Frequency!')
            frequencyvar.set(0.0)
            return Exception()
        return frequency