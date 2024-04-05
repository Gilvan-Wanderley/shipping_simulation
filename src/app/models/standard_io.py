from .entities import Ship
from ..views.flowsheet import Flowsheet


class StandardInputOutput():
    def __init__(self, flowsheet: Flowsheet) -> None:
        self._flowsheet = flowsheet
        self._menu_result = self._flowsheet.master.master._menu_results

    def arrived_ship(self, time: float, ship: Ship) -> None:
        self._flowsheet.arrived_ship(ship)
        self.update_time(time)
        self._menu_result.update_results()

    def docking(self, time: float, ship: Ship) -> None:
        self._flowsheet.docking_ship(ship)
        self.update_time(time)
        self._menu_result.update_results()

    def departuring(self, time: float, ship: Ship) -> None:
        self._flowsheet.departuring_ship(ship)
        self.update_time(time)
        self._menu_result.update_results()

    def update_time(self, time: float) -> None:
        self._flowsheet.update_time(time)
        self._menu_result.update_results()