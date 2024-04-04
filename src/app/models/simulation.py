from ..utils.objs import SimulationResultsValueObject
from .container import Container
from .entities import Port, Ship, GenerateShip
from ..utils.objs import ShipResultsValueObject

class Simulation:
    def __init__(self, container: Container) -> None:
        self._container = container

        port_data = container.build.sim_obj.port
        ships_data = container.build.sim_obj.ships

        self._port = Port(container, port_data.num_berths, port_data.unload_rate)

        self._source_ships = []
        for props in ships_data.entities:
            ship = Ship(container, props.name, props.capacity)
            generate = GenerateShip(container, props.frequency, ship)
            container.env.process(generate.run(self.port))
            self._source_ships.append((ship, generate))

        self._results = SimulationResultsValueObject()

    @property
    def port(self) -> Port:
        return self._port
    
    @property
    def source_ships(self) -> list[tuple[Ship, GenerateShip]]:
        return self._source_ships
    
    @property
    def results(self) -> SimulationResultsValueObject:
        return self._results

    def run_up(self, end_time: float):
        self._container.env.run(until=end_time+0.001)

        self._results.ships_arrival = len(self.port.records.arrival) 
        self._results.ships_departure = len(self.port.records.departured)
        self._results.unloaded_total = self.port.total_unloaded 

        for s in self.source_ships:
            (ship, gen ) = s
            self._results.ships_results.append(ShipResultsValueObject(
                ship.name,
                gen.total_unloaded,
                gen.count,
                gen.num_waitting,
                gen.num_dock,
                gen.num_departure
            ))