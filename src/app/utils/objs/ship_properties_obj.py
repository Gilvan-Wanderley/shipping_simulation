from dataclasses import dataclass


@dataclass
class ShipPropertiesValueObject():
    name: str = None
    capacity: float = None
    frequency: float = None