import tkinter as tk
from tkinter import ttk
from ..simulater import Simulater
from ..controllers import MenuBuilderController
from .components import LabelEntry, LabelVariable, TableView
import threading

class MenuBuilder(tk.Frame):
    def __init__(self, master, simulater: Simulater) -> None:
        super().__init__(master)
        self._simulater= simulater
        self._app = master.master
        self._controller = MenuBuilderController(simulater, self._app)

        self._run_up = tk.DoubleVar(value=0.0)
        self._unload_rate = tk.DoubleVar(value=simulater.builder.sim_obj.port.unload_rate)
        self._num_berths = tk.IntVar(value=simulater.builder.sim_obj.port.num_berths)

        self.build_view()
        

    def build_view(self) -> None:
        tilte = ttk.Label(self, text='Simulation Data')
        tilte.pack(padx=4, pady=4)
        self._run_frame()
        self._ships_frame()
        self._port_frame()

    def _run_simulation_command(self) -> None:
        self._controller.run_simulation_command(self._run_up)

    def _run_frame(self) -> None:
        run_menu = tk.Frame(self)
        run_menu.pack(side="bottom", fill="both", expand=True, padx=4, pady=4)

        run_menu.lbl_run = LabelEntry(run_menu, 'Run until: ', self._run_up, 'days')
        run_menu.lbl_run.pack(side='left', padx=4, pady=4)

        run_menu.btn_run = ttk.Button(run_menu, text='Run Simulation', 
                                      command= threading.Thread(target=self._run_simulation_command).start)
        run_menu.btn_run.pack(side='right', padx=4, pady=4)

    def _port_frame(self) -> None:
        port_menu = ttk.LabelFrame(self, text='Port')
        port_menu.pack(side="bottom", fill="x", expand=True, padx=4, pady=4)

        port_menu.num_berths = LabelVariable(port_menu, 'Nº of Berths:', self._num_berths)
        port_menu.num_berths.pack(fill='x', padx=10)

        port_menu.unload_rate = LabelVariable(port_menu, 'Unloading Rate:', self._unload_rate, 'tonne/h')
        port_menu.unload_rate.pack(fill='x', padx=10, pady=(2,10))

    def _ships_frame(self) -> None:
        ship_menu = ttk.LabelFrame(self, text='Ships')
        ship_menu.pack(side="bottom", fill="both", expand=True, padx=4, pady=4)

        header ={
            'name': {'text': 'Name', 
                     'width':40, 
                     'anchor':'w'},
            'capacity': {'text': 'Capacity', 
                         'width':40, 
                         'anchor':'center'},
            'frequency': {'text': 'Frequency', 
                          'width':40, 
                          'anchor':'center'}}
        
        ship_menu.table = TableView(ship_menu, header)
        ship_menu.table.pack(side="bottom", fill="both", expand=True, padx=4, pady=4)
        ship_menu.table.table.configure(height=6)

        self._load_ships_data(ship_menu.table)

    def _load_ships_data(self, table: TableView) -> None:
        sim_obj = self._simulater.builder.sim_obj
        for i, prop in enumerate(sim_obj.ships.entities):
            table.add_values(i, [prop.name, prop.capacity, prop.frequency])