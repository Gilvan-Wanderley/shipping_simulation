import simpy
from .services import HandlerFile, SimulationBuilder
from .utils.objs import SimulationResultsValueObject
from .models import Simulation, Container, StandardInputOutput
from .views.flowsheet import Flowsheet

class Simulater:
    def __init__(self) -> None:
        self._handler_file = HandlerFile()
        self._builder = SimulationBuilder()
        self._results = SimulationResultsValueObject()
        self._flowsheet = None
    
    @property
    def handler_file(self) -> HandlerFile:
        return self._handler_file 
    
    @property
    def builder(self) -> SimulationBuilder:
        return self._builder 
    
    @property
    def results(self) -> SimulationResultsValueObject:
        return self._results 
    
    @results.setter
    def results(self, value: SimulationResultsValueObject) -> None:
        self._results  = value
    
    def set_flowsheet(self, flowsheet: Flowsheet) -> None:
        self._flowsheet = flowsheet

    def run_up(self, end_time: float) -> None:
        container = Container(simpy.Environment(),
                              StandardInputOutput(self._flowsheet),
                              self._builder)
        simulation = Simulation(container)
        simulation.run_up(end_time)
        self._results = simulation.results