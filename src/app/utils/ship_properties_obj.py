from dataclasses import dataclass


@dataclass
class ShipPropertiesObjectValue():
    name: str = None
    capacity: float = None
    frequency: float = None