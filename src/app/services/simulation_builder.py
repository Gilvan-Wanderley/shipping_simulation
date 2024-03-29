from ..utils.objs import SimulationObjectValue

class SimulationBuilder():
    def __init__(self) -> None:
        self._simulation_obj = SimulationObjectValue()

    @property
    def simulation_obj(self) -> SimulationObjectValue:
        return self._simulation_obj
    
    @simulation_obj.setter
    def simulation_obj(self, sim_obj: SimulationObjectValue) -> None:
        self._simulation_obj = sim_obj

