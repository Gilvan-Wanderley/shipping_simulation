from .ship_obj import ShipValueObject
from .port_properties_obj import PortPropertiesValueObject


class SimulationValueObject():
    def __init__(self) -> None:
        self._port = PortPropertiesValueObject()
        self._ships = ShipValueObject()

    @property
    def port(self) -> PortPropertiesValueObject:
        return self._port
    
    @property
    def ships(self) -> ShipValueObject:
        return self._ships

    def is_complete(self) -> bool:
        if self._port.is_complete() or self._ships.is_complete():
            return True
        else:
            return False

    def to_dict(self) -> dict:
        simulation_dict = {
            'port': {
                'num_berths': self.port.num_berths,
                'unload_rate': self.port.unload_rate
            },
            'ships': []}
        for props in self._ships.entities:
            simulation_dict['ships'].append({
                'name': props.name,
                'capacity': props.capacity,
                'frequency': props.frequency
            })

        return simulation_dict
