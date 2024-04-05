import tkinter as tk
from tkinter import ttk
from ..simulater import Simulater
from ..controllers import MenuPortController
from ..services.image_handler import ImageSource


class MenuPort(tk.Frame):
    def __init__(self, master, simulater: Simulater):
        super().__init__(master)
        self._app = master.master
        self._controller = MenuPortController(simulater, self._app)
        self._simulater = simulater

        self._num_berths = tk.IntVar(value= simulater.builder.sim_obj.port.num_berths)
        self._unloading_rate = tk.DoubleVar(value= simulater.builder.sim_obj.port.unload_rate)
        self.build_view()

    @property
    def num_berths(self) -> tk.IntVar:
        return self._num_berths
    
    @property
    def unloading_rate(self) -> tk.DoubleVar:
        return self._unloading_rate
    
    def build_view(self) -> None:
        self._image = ImageSource.get_photoimage('port_menu', (180,134))
        self._tilte = ttk.Label(self, text='Port Menu')
        self._tilte.pack()

        self._content = ttk.Notebook(self)
        self._content.pack(fill="both", expand=True, padx=4, pady=4)

        self._content.settings = self._setting_tab()

    def _update_command(self) -> None:
         self._controller.update_command(self.num_berths, self.unloading_rate)

    def _setting_tab(self) -> ttk.Frame:
        settings = ttk.Frame(self)
        self._content.add(settings, text='Settings')

        settings.img = tk.Label(settings, image=self._image)
        settings.img.grid(row=0, column=0, sticky=tk.N+tk.S)

        settings.data = ttk.Frame(settings)
        settings.data.grid(row=0, column=1, sticky=tk.N)

        settings.data.lbl_berths = ttk.Label(settings.data, text='Nº Berths: ')
        settings.data.lbl_berths.grid(row=0, column=0, sticky=tk.E, pady=4)

        settings.data.sbx_berths = ttk.Spinbox(settings.data, from_=1, to=10, 
                                               textvariable=self.num_berths,
                                               width=18)
        settings.data.sbx_berths.grid(row=0, column=1, sticky=tk.W, pady=4)

        settings.data.lbl_unloading_rate = tk.Label(settings.data, text='Unloading Rate: ')
        settings.data.lbl_unloading_rate.grid(row=1, column=0, sticky=tk.E, pady=4)

        settings.data.ety_unloading_rate = ttk.Entry(settings.data, textvariable=self.unloading_rate)
        settings.data.ety_unloading_rate.grid(row=1, column=1, sticky=tk.W, pady=4)

        settings.data.lbl_unloading_rate_unit = tk.Label(settings.data, text='tonne')
        settings.data.lbl_unloading_rate_unit.grid(row=1, column=2, sticky=tk.W)

        settings.data.btn_update = ttk.Button(settings.data, text='Update', 
                                              command= self._update_command)
        settings.data.btn_update.grid(row=3, column=0, columnspan=3, sticky=tk.E, pady=4)

        return settings

