import simpy
from dataclasses import dataclass
from .standard_io import StandardInputOutput
from ..services import SimulationBuilder

@dataclass
class Container:
    env : simpy.Environment
    stdio: StandardInputOutput
    build: SimulationBuilder