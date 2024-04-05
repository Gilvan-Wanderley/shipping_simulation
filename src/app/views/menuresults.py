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
            'unloaded_total': tk.DoubleVar(value="{:,.1f}".format(self._simulater.results.unloaded_total)),
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
    
    def update_results(self) -> None:
        self._simulater.simulation.update_result_obj()
        self._results['unloaded_total'].set("{:,.1f}".format(self._simulater.results.unloaded_total))
        self._results['ships_arrival'].set(self._simulater.results.ships_arrival)
        self._results['ships_departure'].set(self._simulater.results.ships_departure)
        self._results['ships'] = self._simulater.results.ships_results 
        self._load_ships(self._ship_table)
        

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
        self._ship_table = TableView(ship_menu, header)
        self._ship_table = TableView(ship_menu, header)
        self._ship_table.pack(side="bottom", fill="both",expand=True, padx=4, pady=4)
        self._ship_table.table.configure(height=6)

        self._load_ships(self._ship_table)

    def _load_ships(self, table: TableView):
        for i, ship in enumerate(self._results['ships']):
            if table.exist(i):
                table.remove_value(i)
            table.add_value(i, [ship.name,
                                 "{:,.1f}".format(ship.unloaded),
                                 ship.arrival,
                                 ship.waitting, 
                                 ship.dock, 
                                 ship.departure
                                 ])