import tkinter as tk
from tkinter import ttk
from ...models.entities import Ship, ShipStatus
from ...utils.image_handler import ImageSource
import time
from PIL import ImageTk


class ShipView(ImageTk.PhotoImage):
    def __init__(self, canvas: tk.Canvas, ship: Ship) -> None:
        super().__init__(ImageSource.get_image('ship_flow', (100,25)))
        self._canvas = canvas
        # self._id  = canvas.create_image(50, 91, image=img)
        self._ship = ship
        self._on_port = False
        self._on_wait_stage = False

    @property
    def on_port(self) -> bool:
        return  self._on_port
    
    @property
    def on_wait_stage(self) -> bool:
        return  self._on_wait_stage

    @property
    def ship(self) -> Ship:
        return self._ship

    @property
    def status(self) -> ShipStatus:
        return self._ship.status

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int) -> None:
        self._id = value
    
    @property
    def position(self) -> tuple[int, int]:
        _, y0, x1, _ = self._canvas.bbox(self.id)
        return (x1, y0)
    
    def action(self) -> None:        
        match self.status:
            case ShipStatus.arrived:
                self._canvas.move(self.id, 5.0, 0.0)
                time.sleep(10/1000)
                if self.position[0] >= 350:
                    self._on_wait_stage = True
            case ShipStatus.waitting:
                pass
            case ShipStatus.docking:
                self._canvas.move(self.id, 5.0, 0.0)
                time.sleep(10/1000)
                if self.position[0] >= 830:
                    self._on_port = True
            case ShipStatus.docked:
                pass
            case ShipStatus.unloading:
                pass
            case ShipStatus.unloaded:
                pass
            case ShipStatus.departuring:
                self._canvas.move(self.id, 0.0, -5.0)
                time.sleep(10/1000)
                if self.position[1] <= -13.0:
                    self._canvas.move(self.id, 0.0, -5.0)
                    self._on_port = False
                pass
            case ShipStatus.departured:
                pass
            case _:
                print('erroo')
                pass