import json
from typing import Union
from ..utils.objs import SimulationValueObject, ShipPropertiesValueObject


class HandlerFile():
    def __init__(self) -> None:
        self._path = ''

    @property
    def path(self) -> str:
        return self._path
    
    @path.setter
    def path(self, path: str):
        self._path = path

    def save_file(self, simulation_obj: SimulationValueObject):
        simulation_dict = simulation_obj.to_dict()
        with open(self.path, 'w') as sim_file:
            json.dump(simulation_dict, sim_file)

    def load_obj(self, new_path: str) -> tuple[bool, Union[SimulationValueObject, None]]:
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
    
    def _create_obj(self, simulation_dict: dict) -> SimulationValueObject:
        simulation_handler = SimulationValueObject()
        simulation_handler.port.num_berths = simulation_dict['port']['num_berths']
        simulation_handler.port.unload_rate = simulation_dict['port']['unload_rate']

        for ship in simulation_dict['ships']:
            simulation_handler.ships.add(ShipPropertiesValueObject(**ship))

        return simulation_handler