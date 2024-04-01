import simpy
from enum import Enum
from dataclasses import dataclass
# from ..container import Container


class ShipStatus(Enum):
    arrived = 'arrived'
    waitting= 'waitting'
    docking = 'docking'
    docked = 'docked'
    unloading = 'unloading'
    unloaded = 'unloaded'
    departuring = 'departuring'
    departured = 'departured'

@dataclass
class ShipRecord():
    time: float
    status: ShipStatus
    holdup: float

class Ship:
    def __init__(self, 
                 container, 
                 name: str,
                 capacityCargoHold: float) -> None:
        self._container = container
        self._name = name
        self._cargoHold = simpy.Container(container.env, capacityCargoHold, capacityCargoHold)

        self._records = []
        self._status = None
        pass
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def status(self) -> ShipStatus:
        return self._status
    
    @status.setter
    def status(self, status) -> None:        
        self._status = status
        self._record()

    @property
    def capacity(self) -> float:
        return self._cargoHold.capacity
    
    @property
    def holdup(self) -> float:
        return self._cargoHold.level
    
    @property
    def records(self) -> list[ShipRecord]:
        return self._records

    def unloading(self, amount) -> float:
        cargo = 0.0
        if amount > self.holdup:
            cargo = self.holdup
        else:
            cargo = amount
        self._cargoHold.get(cargo)
        self._record()
        return cargo

    def _record(self) -> None:
        self._records.append(ShipRecord(
            self._container.env.now,
            self.status,
            self.holdup
        ))

    