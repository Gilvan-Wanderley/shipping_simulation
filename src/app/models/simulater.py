from ..services import HandlerFile

class Simulater:
    def __init__(self) -> None:
        self._handler_file = HandlerFile()

    @property
    def handler_file(self) -> HandlerFile:
        return self._handler_file 