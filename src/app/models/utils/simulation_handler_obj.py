from .ship_properties_obj import ShipPropertiesObjectValue
from .port_properties_obj import PortPropertiesObjectValue


class SimulationHandlerObjectValue():
    def __init__(self) -> None:
        self._port = PortPropertiesObjectValue()
        self._ship = ShipPropertiesObjectValue()

    @property
    def port(self) -> PortPropertiesObjectValue:
        return self._port
    
    @property
    def ship(self) -> ShipPropertiesObjectValue:
        return self._ship

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
        for props in self.ship.entities:
            simulation_dict['ships'].append({
                'name': props.name,
                'capacity': props.capacity,
                'frequency': props.frequency
            })

        return simulation_dict
