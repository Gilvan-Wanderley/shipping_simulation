from .ship import Ship, ShipStatus
from .port import Port


class GenerateShip:
    def __init__(self, 
                 container, 
                 frequency: float,
                 shipType: Ship) -> None:
        self._container = container
    
        self._frequency = frequency
        self._shipType = shipType

        self._records = []
        self._count = 0

    @property
    def records(self) -> list[Ship]:
        return self._records

    @property
    def total_unloaded(self) -> float:
        unload = 0.0
        for s in self.records:
            unload += s.capacity - s.holdup
        return unload

    @property
    def num_departure(self) -> int:
        count = 0
        for s in self.records:
            if s.status == ShipStatus.departured:
                count += 1
        return count
    
    @property
    def num_waitting(self) -> int:
        count = 0
        for s in self.records:
            if s.status == ShipStatus.waitting:
                count += 1
        return count
    
    @property
    def num_dock(self) -> int:
        count = 0
        for s in self.records:
            if s.status in [ShipStatus.docked, 
                            ShipStatus.docking,
                            ShipStatus.unloading,
                            ShipStatus.unloaded]:
                count += 1
        return count

    @property
    def count(self) -> int:
        return self._count

    @property
    def frequency(self) -> float:
        return self._frequency

    @frequency.setter
    def frequency(self, frequency: float) -> None:
        self._frequency = frequency

    def run(self, port: Port):
        while True:
            yield self._container.env.timeout(self.frequency)
            ship = self._createShip(self._count)
            self._container.env.process(port.run(ship))
            self._count += 1

    def _createShip(self, id: int) -> Ship:
        ship = Ship(self._container,
                    f'{self._shipType.name}[{id}]',
                    self._shipType.capacity)
        ship.status = ShipStatus.arrived
        self._container.stdio.arrived_ship(self._container.env.now,
                                          ship)
        self._records.append(ship)
        return ship
