from ..utils.objs import SimulationValueObject


class SimulationBuilder():
    def __init__(self) -> None:
        self._simulation_obj = SimulationValueObject()

    @property
    def sim_obj(self) -> SimulationValueObject:
        return self._simulation_obj
    
    @sim_obj.setter
    def sim_obj(self, sim_obj: SimulationValueObject) -> None:
        self._simulation_obj = sim_obj

