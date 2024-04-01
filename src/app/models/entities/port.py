from dataclasses import dataclass
from .ship import Ship, ShipStatus
# from ..container import Container
import simpy

@dataclass
class ShipRegister:
    time: float
    ship: Ship

@dataclass
class PortRecords:
    arrival: list[ShipRegister]
    docked: list[ShipRegister]
    unloaded: list[ShipRegister]
    departured: list[ShipRegister]


class Port:
    def __init__(self,
                 container,
                 numBerth: int,
                 unloadRate: float) -> None:
        self._container = container
        self._berths = simpy.Resource(container.env, numBerth)
        self._unloadRate = unloadRate
        
        self._totalUnloaded = 0.0
        self._records = PortRecords([],[],[],[])        

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
        # print(f'{self._container.env.now: .2f}h |   users: {self.occupancy} and queue: {self.queue}')
        self._container.stdio.port_status(self._container.env.now, self)
        yield self._container.env.process(self._portPorcess(ship))
        self._container.stdio.port_status(self._container.env.now, self)
        # print(f'{self._container.env.now: .2f}h |   users: {self.occupancy} and queue: {self.queue}')

    def _portPorcess(self, ship: Ship):
        self.records.arrival.append(ShipRegister(self._container.env.now, ship))

        # print(f'{self._container.env.now: .2f}h |   registring {ship.name} at port')
        self._container.stdio.port_registring(self._container.env.now, ship)
        ship.status = ShipStatus.waitting
        with self.berths.request() as request:
            yield request
            tryDock = True
            while tryDock:
                if request.triggered:
                    self._container.stdio.port_status(self._container.env.now, self)
                    # print(
                    #     f'{self._container.env.now: .2f}h |   users: {self.occupancy} and queue: {self.queue}')
                    yield self._container.env.process(self._docking(ship))
                    yield self._container.env.process(self._unloading(ship))
                    yield self._container.env.process(self._departuring(ship))
                    tryDock = False
                else:
                    tryDock = True
                self._container.stdio.port_status(self._container.env.now, self)
        #         print(
        #             f'{self._container.env.now: .2f}h |   users: {self.occupancy} and queue: {self.queue}')
        # pass

    def _docking(self, ship: Ship):
        dockingTime = 0.2  # WARNING

        # print(f'{self._container.env.now: .2f}h |   docking {ship.name}.')
        self._container.stdio.docking(self._container.env.now, ship)
        ship.status = ShipStatus.docking

        yield self._container.env.timeout(dockingTime)

        # print(f'{self._container.env.now: .2f}h |   docked {ship.name}.')
        self._container.stdio.docked(self._container.env.now, ship)
        ship.status = ShipStatus.docked
        self.records.docked.append(ShipRegister(self._container.env.now, ship))

    def _unloading(self, ship: Ship):
        # print(f'{self._container.env.now: .2f}h |   unloading {ship.name}.')
        self._container.stdio.unloading(self._container.env.now, ship)
        ship.status = ShipStatus.unloading

        yield self._container.env.process(self._unloadShip(ship))

        # print(f'{self._container.env.now: .2f}h |   unloaded {ship.name}.')
        self._container.stdio.unloaded(self._container.env.now, ship)
        ship.status = ShipStatus.unloaded
        self.records.unloaded.append(ShipRegister(self._container.env.now, ship))

    def _departuring(self, ship: Ship):
        departureTime = 0.1  # WARNING

        # print(f'{self._container.env.now: .2f}h |   departuring {ship.name}.')
        self._container.stdio.departuring(self._container.env.now, ship)
        ship.status = ShipStatus.departuring

        yield self._container.env.timeout(departureTime)

        # print(f'{self._container.env.now: .2f}h |   departured {ship.name}.')
        self._container.stdio.departured(self._container.env.now, ship)
        ship.status = ShipStatus.departured
        self.records.departured.append(ShipRegister(self._container.env.now, ship))

    def _unloadShip(self, ship: Ship):
        timeStep = 0.1  # WARNING
        while ship.holdup > 0:
            try_amount = timeStep*self.unloadRate
            yield self._container.env.timeout(timeStep)            
            amount = ship.unloading(try_amount)
            self._totalUnloaded += amount
