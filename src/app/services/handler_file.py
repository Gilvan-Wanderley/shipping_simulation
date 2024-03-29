import json
from typing import Union
from ..utils import SimulationObjectValue, ShipPropertiesObjectValue

class HandlerFile():
    def __init__(self) -> None:
        self._path = ''

    @property
    def path(self) -> str:
        return self._path
    
    @path.setter
    def path(self, path: str):
        self._path = path

    def save_file(self, simulation_obj: SimulationObjectValue):
        simulation_dict = simulation_obj.to_dict()
        with open(self.path, 'w') as sim_file:
            json.dump(simulation_dict, sim_file)

    def load_obj(self, new_path: str) -> tuple[bool, Union[SimulationObjectValue, None]]:
        try:
            simulation_dict = {}
            response = True
            with open (new_path, 'r') as sim_file:
                simulation_dict = json.load(sim_file)
            simulation_obj = self._create_obj(simulation_dict)
        except:
            response = False
            simulation_obj = None
        return (response, simulation_obj)
    
    def _create_obj(self, simulation_dict: dict) -> SimulationObjectValue:
        simulation_handler = SimulationObjectValue()
        simulation_handler.port.num_berths = simulation_dict['port']['num_berths']
        simulation_handler.port.unload_rate = simulation_dict['port']['unload_rate']

        for ship in simulation_dict['ships']:
            simulation_handler.ship.add(ShipPropertiesObjectValue(**ship))

        return simulation_handler