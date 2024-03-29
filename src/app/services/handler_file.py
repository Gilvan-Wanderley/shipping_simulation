import json
from ..utils import SimulationHandlerObjectValue, ShipPropertiesObjectValue

class HandlerFile():
    def __init__(self) -> None:
        self._path = ''

    @property
    def path(self) -> str:
        return self._path
    
    @path.setter
    def path(self, path: str):
        self._path = path

    def save_file(self, simulation_obj: SimulationHandlerObjectValue):
        simulation_dict = simulation_obj.to_dict()
        with open(self.path, 'w') as sim_file:
            json.dump(simulation_dict, sim_file)

    def load_obj(self, new_path: str) -> SimulationHandlerObjectValue:
        simulation_dict = {}
        with open (new_path, 'r') as sim_file:
            simulation_dict = json.load(sim_file)
        return self._create_obj(simulation_dict)
    
    def _create_obj(self, simulation_dict: dict) -> SimulationHandlerObjectValue:
        simulation_handler = SimulationHandlerObjectValue()
        simulation_handler.port.num_berths = simulation_dict['port']['num_berths']
        simulation_handler.port.unload_rate = simulation_dict['port']['unload_rate']

        for ship in simulation_dict['ships']:
            simulation_handler.ship.add(ShipPropertiesObjectValue(**ship))

        return simulation_handler