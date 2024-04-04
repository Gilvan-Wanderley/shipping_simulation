from .ship_results_obj import  ShipResultsValueObject

class SimulationResultsValueObject():
    unloaded_total: float = 0.0
    ships_arrival: int = 0
    ships_departure: int = 0

    def __init__(self) -> None:
        self._ships : list[ShipResultsValueObject] = []

    @property
    def ships_results(self) -> list[ShipResultsValueObject]:
        return self._ships
