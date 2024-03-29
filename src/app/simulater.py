from .services import HandlerFile, SimulationBuilder

class Simulater:
    def __init__(self) -> None:
        self._handler_file = HandlerFile()
        self._builder = SimulationBuilder()

    @property
    def handler_file(self) -> HandlerFile:
        return self._handler_file 
    
    @property
    def builder(self) -> SimulationBuilder:
        return self._builder 
    
    