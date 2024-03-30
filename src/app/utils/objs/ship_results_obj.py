from dataclasses import dataclass

@dataclass
class ShipResultsValueObject():
    name: str
    unloaded: float
    arrival: int
    waitting: int
    dock: int
    departure: int