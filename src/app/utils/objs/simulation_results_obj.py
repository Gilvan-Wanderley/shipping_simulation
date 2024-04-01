from .ship_results_obj import  ShipResultsValueObject

class SimulationResultsValueObject():
    unloaded_total: float = 0.0
    ships_arrival: int = 0
    ships_departure: int = 0

    def __init__(self) -> None:
        self._ships : list[ShipResultsValueObject] = []
        # self._result = {
        #     'unloaded_total': 0.0,
        #     'ships_arrival': 0,
        #     'ships_departure': 0,
        #     'ships': []
        # }

    @property
    def ships_results(self) -> list[ShipResultsValueObject]:
        return self._ships

    # @property
    # def unloaded_total(self) -> float:
    #     return self._result['unloaded_total']

    # @unloaded_total.setter
    # def unloaded_total(self, value: float) -> None:
    #     self._result['unloaded_total'] = value

    # @property
    # def ships_arrival(self) -> int:
    #     return self._result['ships_arrival']

    # @ships_arrival.setter
    # def ships_arrival(self, value: int) -> None:
    #     self._result['ships_arrival'] = value

    # @property
    # def ships_departure(self) -> int:
    #     return self._result['ships_departure']

    # @ships_departure.setter
    # def ships_departure(self, value: int) -> None:
    #     self._result['ships_departure'] = value