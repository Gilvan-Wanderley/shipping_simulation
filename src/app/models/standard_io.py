from .entities import Ship
from ..views.flowsheet import Flowsheet

class StandardInputOutput():
    def __init__(self, flowsheet: Flowsheet) -> None:
        self._flowsheet = flowsheet

    def arrived_ship(self, time: float, ship: Ship) -> None:
        self._flowsheet.arrived_ship(ship)
        self.update_time(time)

    def docking(self, time: float, ship: Ship) -> None:
        self._flowsheet.docking_ship(ship)
        self.update_time(time)

    def departuring(self, time: float, ship: Ship) -> None:
        self._flowsheet.departuring_ship(ship)
        self.update_time(time)

    def update_time(self, time: float) -> None:
        self._flowsheet.update_time(time)