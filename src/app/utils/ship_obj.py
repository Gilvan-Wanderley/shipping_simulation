from .ship_properties_obj import ShipPropertiesObjectValue

class ShipObjectValue():
    def __init__(self) -> None:
        self._entities : list[ShipPropertiesObjectValue] = []  
        
    @property
    def entities(self) -> list[ShipPropertiesObjectValue]:
        return self._entities
    
    def ship_props(self, name: str) -> ShipPropertiesObjectValue:
        if name not in self.ships_name():
            raise Exception(f'Invalid name ({name})!')
        return [e for e in self.entities if e.name == name][0]

    def ships_name(self) -> list[str]:
        return [e.name for e in self.entities]
    
    def add(self, ship_prop: ShipPropertiesObjectValue) -> None:
        if ship_prop.name in self.ships_name():
            raise Exception(f'Invalid name ({ship_prop.name})!')
        self.entities.append(ship_prop)

    def remove(self, name: str) -> None:
        if name not in self.ships_name():
            raise Exception(f'Invalid name ({name})!')

    def edit(self, name: str, capacity: float, frequency: float) -> None:
        if name not in self.ships_name():
            raise Exception(f'Invalid name ({name})!')
        ship = self.ship_props(name)
        ship.capacity = capacity
        ship.frequency = frequency