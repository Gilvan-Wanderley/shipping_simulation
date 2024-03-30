from .ship_properties_obj import ShipPropertiesValueObject

class ShipValueObject():
    def __init__(self) -> None:
        self._entities : list[ShipPropertiesValueObject] = []  
        
    @property
    def entities(self) -> list[ShipPropertiesValueObject]:
        return self._entities
    
    def is_complete(self) -> bool:
        return len(self._entities) > 0

    def ship_props(self, name: str) -> ShipPropertiesValueObject:
        if name not in self.ships_names():
            raise Exception(f'Invalid name ({name})!')
        return [e for e in self.entities if e.name == name][0]

    def ships_names(self) -> list[str]:
        if self.entities == []:
            return []
        else:
            return  [e.name for e in self.entities]
    
    def add(self, ship_prop: ShipPropertiesValueObject) -> None:
        if ship_prop.name in self.ships_names():
            raise Exception(f'Invalid name ({ship_prop.name})!')
        self.entities.append(ship_prop)

    def remove(self, name: str) -> None:
        if name not in self.ships_names():
            raise Exception(f'Invalid name ({name})!')

    def edit(self, name: str, capacity: float, frequency: float) -> None:
        if name not in self.ships_names():
            raise Exception(f'Invalid name ({name})!')
        ship = self.ship_props(name)
        ship.capacity = capacity
        ship.frequency = frequency