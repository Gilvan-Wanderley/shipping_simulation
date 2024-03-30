import tkinter as tk
from tkinter import ttk
from ..simulater import Simulater
from .components import TableView, LabelVariable

class MenuResults(tk.Frame):
    def __init__(self, master, simulater: Simulater) -> None:
        super().__init__(master)
        self._app = master.master
        self._simulater = simulater
        self._results ={
            'unloaded_total': tk.DoubleVar(value=simulater.results.unloaded_total),
            'ships_arrival': tk.IntVar(value=simulater.results.ships_arrival),
            'ships_departure': tk.IntVar(value=simulater.results.ships_departure),
            'ships': simulater.results.ships_results 
        }
        self.build_view()

    def build_view(self) -> None:
        tilte = ttk.Label(self, text='Summary of Results')
        tilte.pack(padx=4, pady=4)
        self._ships_frame()
        self._port_frame()

    def _port_frame(self) -> None: 
        port_menu = ttk.LabelFrame(self, text='Port' )
        port_menu.pack(side="bottom", fill="both", padx=4, pady=4)

        port_menu.unload_total = LabelVariable(port_menu,
                                                'Unloaded Total:',
                                                self._results['unloaded_total'],
                                                'tonne')

        port_menu.ships_arrival = LabelVariable(port_menu,
                                                 'Ships Arrival:',
                                                 self._results['ships_arrival'])

        port_menu.ships_departure = LabelVariable(port_menu,
                                                   'Ships Departure:',
                                                    self._results['ships_departure'])
        

        port_menu.unload_total.pack(padx=(4,4), pady=(0,2), anchor='w')
        port_menu.ships_arrival.pack(padx=(4,4), pady=(0,2), anchor='w')
        port_menu.ships_departure.pack(padx=(4,4), pady=(0,2), anchor='w')
    
    def _ships_frame(self) -> None:
        ship_menu = ttk.LabelFrame(self, text='Ships')
        ship_menu.pack(side="bottom", fill="both", expand=True, padx=4, pady=4)

        header ={
            'name': {'text': 'Name', 
                     'width':100, 
                     'anchor':'w'},
            'unloaded': {'text': 'Unloaded', 
                         'width':100, 
                         'anchor':'center'},
            'arrival': {'text': 'Arrival', 
                        'width':80, 
                        'anchor':'center'},
            'waitting': {'text': 'Watting', 
                         'width':80, 
                         'anchor':'center'},
            'dock': {'text': 'Dock', 
                     'width':80, 
                     'anchor':'center'},
            'departure': {'text': 'Departure', 
                          'width':80,
                          'anchor':'center'},
            }
        
        ship_menu.table = TableView(ship_menu, header)
        ship_menu.table.pack(side="bottom", fill="both",expand=True, padx=4, pady=4)
        ship_menu.table.table.configure(height=6)

        self._load_ships(ship_menu.table)

    def _load_ships(self, table: TableView):
        for i, ship in enumerate(self._results['ships']):
            table.add_values(i, [ship.name,
                                 ship.unloaded,
                                 ship.arrival,
                                 ship.waitting, 
                                 ship.dock, 
                                 ship.departure
                                 ])