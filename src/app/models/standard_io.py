from abc import ABC
from .entities import Ship, Port

class StandardInputOutput(ABC):
    def create_ship(self, time: float, ship: Ship):
        print(f'{time: .2f}h |   {ship.name} arrivel.')

    def port_status(self, time: float, port: Port):
        print(f'{time: .2f}h |   users: {port.occupancy} and queue: {port.queue}')

    def port_registring(self, time: float, ship: Ship):
        print(f'{time: .2f}h |   registring {ship.name} at port')

    def docking(self, time: float, ship: Ship):
        print(f'{time: .2f}h |   docking {ship.name}.')

    def docked(self, time: float, ship: Ship):
        print(f'{time: .2f}h |   docked {ship.name}.')

    def unloading(self, time: float, ship: Ship):
        print(f'{time: .2f}h |   unloading {ship.name}.')

    def unloaded(self, time: float, ship: Ship):
        print(f'{time: .2f}h |   unloaded {ship.name}.')

    def departuring(self, time: float, ship: Ship):
        print(f'{time: .2f}h |   departuring {ship.name}.')

    def departured(self, time: float, ship: Ship):
        print(f'{time: .2f}h |   departured {ship.name}.')