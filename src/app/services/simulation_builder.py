from ..utils.objs import SimulationObjectValue

class SimulationBuilder():
    def __init__(self) -> None:
        self._simulation_obj = SimulationObjectValue()

    @property
    def sim_obj(self) -> SimulationObjectValue:
        return self._simulation_obj
    
    @sim_obj.setter
    def sim_obj(self, sim_obj: SimulationObjectValue) -> None:
        self._simulation_obj = sim_obj

