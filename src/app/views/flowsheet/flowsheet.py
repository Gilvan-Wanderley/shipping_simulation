import tkinter as tk
from .ship_view import ShipView
from ...models.entities import Ship


class Flowsheet(tk.Canvas):
    def __init__(self, master: tk.Misc, simulater) -> None:
        super().__init__(master, background='#0096C7',height=200, width=1030)
        self._ships_waitting : list[ShipView] = []
        self._ships_unloading : list[ShipView] = []
        self._slowly = tk.DoubleVar(self, 10)
        self.create_rectangle((830, 0), (1040, 210) , fill='#DDD', )
        self._scalebar = tk.Scale(self, from_=0, to=20, 
                                  orient='horizontal',
                                  label='Animation Speed',
                                  length=200,
                                  showvalue=False,
                                  variable=self._slowly)
        
        self.create_window(105,205, window=self._scalebar, anchor='s')
        self._time_id = self.create_text(5,5, 
                                         text=f'Time: {0.00: .2f} days', 
                                         anchor='nw',
                                         fill='white',
                                         font=('15'))
       

    @property
    def slowly(self) -> float:
        return self._scalebar.cget('to') - self._slowly.get()
    
    def update_time(self, time: float) -> None:
        self.itemconfig(self._time_id, text=f'Time: {time: .2f} days')

    def arrived_ship(self, ship: Ship) -> None:
        ship_view = ShipView(self, ship)
        ship_view.id = self.create_image(50, 91, image=ship_view)
        while not ship_view.on_wait_stage:
             ship_view.action()
        self._ships_waitting.append(ship_view)
    
    def docking_ship(self, ship: Ship) -> None:
        docking_sv = [sv for sv in self._ships_waitting if sv._ship == ship]
        for sv_docking in docking_sv:
            while not sv_docking.on_port:
                sv_docking.action()
            self._ships_unloading.append(sv_docking)
            self._ships_waitting.remove(sv_docking)
        
    def departuring_ship(self, ship: Ship) -> None:
        departuring_sv = [sv for sv in self._ships_unloading if sv._ship == ship]
        for sv_departuring in departuring_sv:
            while sv_departuring.on_port:
                sv_departuring.action()
            self._ships_unloading.remove(sv_departuring)

    

    