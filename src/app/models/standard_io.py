from abc import ABC
from .entities import Ship, Port
from ..views.flowsheet import Flowsheet

class StandardInputOutput():
    def updadte(self):
        pass
    def __init__(self, flowsheet: Flowsheet) -> None:
        self._flowsheet = flowsheet

    def port_status(self, time: float, port: Port):
        print(f'{time: .2f}h |   users: {port.occupancy} and queue: {port.queue}')

    def port_registring(self, time: float, ship: Ship):
        print(f'{time: .2f}h |   registring {ship.name} at port')

    def arrived_ship(self, time: float, ship: Ship):
        self._flowsheet.arrived_ship(ship)

    def docking(self, time: float, ship: Ship):
        self._flowsheet.docking_ship(ship)

    def departuring(self, time: float, ship: Ship):
        self._flowsheet.departuring_ship(ship)
