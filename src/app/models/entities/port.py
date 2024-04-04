import simpy
from dataclasses import dataclass, field
from .ship import Ship, ShipStatus

@dataclass
class ShipRegister:
    time: float
    ship: Ship

@dataclass
class PortRecords:
    arrival: list[ShipRegister] = field(default_factory=list)
    docked: list[ShipRegister] = field(default_factory=list)
    unloaded: list[ShipRegister] = field(default_factory=list)
    departured: list[ShipRegister] = field(default_factory=list)


class Port:
    def __init__(self,
                 container,
                 numBerth: int,
                 unloadRate: float) -> None:
        self._container = container
        self._berths = simpy.Resource(container.env, numBerth)
        self._unloadRate = unloadRate
        
        self._totalUnloaded = 0.0
        self._records = PortRecords()        

    @property
    def berths(self) -> simpy.Resource:
        return self._berths

    @property
    def queue(self) -> int:
        return len(self.berths.queue)

    @property
    def occupancy(self) -> int:
        return len(self.berths.users)

    @property
    def total_unloaded(self) -> float:
        return self._totalUnloaded

    @property
    def records(self) -> PortRecords:
        return self._records

    @property
    def unloadRate(self) -> float:
        return self._unloadRate

    @unloadRate.setter
    def unloadRate(self, unloadRate: float):
        self._unloadRate = unloadRate

    def run(self, ship: Ship):
        yield self._container.env.process(self._portPorcess(ship))

    def _portPorcess(self, ship: Ship):
        self.records.arrival.append(ShipRegister(self._container.env.now, ship))

        ship.status = ShipStatus.waitting
        with self.berths.request() as request:
            yield request
            tryDock = True
            while tryDock:
                if request.triggered:
                    yield self._container.env.process(self._docking(ship))
                    yield self._container.env.process(self._unloading(ship))
                    yield self._container.env.process(self._departuring(ship))
                    tryDock = False
                else:
                    tryDock = True

    def _docking(self, ship: Ship):
        dockingTime = 0.2  # WARNING

        ship.status = ShipStatus.docking
        self._container.stdio.docking(self._container.env.now, ship)
        yield self._container.env.timeout(dockingTime)
        ship.status = ShipStatus.docked
        self.records.docked.append(ShipRegister(self._container.env.now, ship))

    def _unloading(self, ship: Ship):
        ship.status = ShipStatus.unloading
        yield self._container.env.process(self._unloadShip(ship))
        ship.status = ShipStatus.unloaded
        self.records.unloaded.append(ShipRegister(self._container.env.now, ship))

    def _departuring(self, ship: Ship):
        departureTime = 0.1  # WARNING

        ship.status = ShipStatus.departuring
        self._container.stdio.departuring(self._container.env.now, ship)
        yield self._container.env.timeout(departureTime)
        ship.status = ShipStatus.departured
        self.records.departured.append(ShipRegister(self._container.env.now, ship))

    def _unloadShip(self, ship: Ship):
        timeStep = 0.1  # WARNING
        while ship.holdup > 0:
            try_amount = timeStep*self.unloadRate
            yield self._container.env.timeout(timeStep)            
            amount = ship.unloading(try_amount)
            self._totalUnloaded += amount
            self._container.stdio.update_time(self._container.env.now)