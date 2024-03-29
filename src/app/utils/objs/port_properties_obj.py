

class PortPropertiesObjectValue():
    def __init__(self) -> None:
        self._num_berths: int = None
        self._unload_rate: float = None
    
    @property
    def num_berths(self) -> int:
        return self._num_berths
    
    @num_berths.setter
    def num_berths(self, value: int) -> None:
        self._num_berths = value
    
    @property
    def unload_rate(self) -> float:
        return self._unload_rate
    
    @unload_rate.setter
    def unload_rate(self, value: int) -> None:
        self._unload_rate = value

    def is_complete(self) -> bool:
        return self.num_berths > 0 and self.unload_rate > 0