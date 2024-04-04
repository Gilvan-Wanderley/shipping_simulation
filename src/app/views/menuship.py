import tkinter as tk
from tkinter import ttk
from ..simulater import Simulater
from ..controllers import MenuShipController
from ..services.image_handler import ImageSource


class MenuShip(tk.Frame):
    def __init__(self, master, simulater: Simulater) -> None:
        super().__init__(master)
        self._app = master.master
        self._simulater = simulater
        self._controller = MenuShipController(simulater, self._app)
        self._vars = {
            'new':{
                'name': tk.StringVar(value='Ship Name'),
                'capacity': tk.DoubleVar(),
                'frequency': tk.DoubleVar()
            },
            'edit':{
                'selected': tk.StringVar(),
                'capacity': tk.DoubleVar(),
                'frequency': tk.DoubleVar()
            }
        }
        self.build_view()

    def build_view(self) -> None:
        self._image = ImageSource.get_photo_image('ship_menu', (190,110))
        self._tilte = ttk.Label(self, text='Ship Menu')
        self._tilte.pack()

        self._content = ttk.Notebook(self)
        self._content.pack(fill="both", expand=True, padx=4, pady=4)

        self._content.new = self._new_tab()
        self._content.edit = self._edit_tab()

    def _onclick_create(self) -> None:
        self._controller.create_command(self._vars['new']['name'],
                                       self._vars['new']['capacity'], 
                                       self._vars['new']['frequency'])

    def _onclick_update(self) -> None:
        self._controller.update_command(self._vars['edit']['selected'],
                                       self._vars['edit']['capacity'], 
                                       self._vars['edit']['frequency'])
        ship_name = self._vars['edit']['selected'].get()
        ship_prop = self._simulater.builder.sim_obj.ships.ship_props(ship_name)
        self._vars['edit']['capacity'].set(ship_prop.capacity)
        self._vars['edit']['frequency'].set(ship_prop.frequency)

    def _onclick_delete(self) -> None:
        self._controller.delete_command(self._vars['edit']['selected'])
        self._vars['edit']['selected'].set('')
        self._vars['edit']['capacity'].set(0.0)
        self._vars['edit']['frequency'].set(0.0)

    def _onselect(self, event) -> None:
        ship_prop = self._simulater.builder.sim_obj.ships.ship_props(event.widget.get())
        self._vars['edit']['capacity'].set(ship_prop.capacity)
        self._vars['edit']['frequency'].set(ship_prop.frequency)
        self._content.edit.data.btn_delete['state'] = 'enable'
        self._content.edit.data.btn_update['state'] = 'enable'

    def _new_tab(self) -> tk.Frame:
        new = ttk.Frame(self)
        self._content.add(new, text='New')

        new.img = tk.Label(new, image=self._image)
        new.img.grid(row=0, column=0, sticky=tk.N+tk.S)

        new.data = tk.Frame(new)
        new.data.grid(row=0, column=1, sticky=tk.N)

        new.data.lbl_name = tk.Label(new.data, text='Name: ')
        new.data.lbl_name.grid(row=0, column=0, sticky=tk.E, pady=4)

        new.data.ety_name = tk.Entry(new.data, textvariable=self._vars['new']['name'])
        new.data.ety_name.grid(row=0, column=1, sticky=tk.E, pady=4)

        new.data.lbl_capacity = tk.Label(new.data, text='Capacity: ')
        new.data.lbl_capacity.grid(row=1, column=0, sticky=tk.E, pady=4)

        new.data.txt_capacity = tk.Entry(new.data, textvariable=self._vars['new']['capacity'])
        new.data.txt_capacity.grid(row=1, column=1, sticky=tk.E, pady=4)
        new.data.txt_capacity_unit = tk.Label(new.data, text='tonne')
        new.data.txt_capacity_unit.grid(row=1, column=2, sticky=tk.W, padx=2, pady=4)

        new.data.lbl_frequency = tk.Label(new.data, text='Frequency: ')
        new.data.lbl_frequency.grid(row=2, column=0, sticky=tk.E, pady=4)

        new.data.txt_frequency = tk.Entry(new.data, textvariable=self._vars['new']['frequency'])
        new.data.txt_frequency.grid(row=2, column=1, sticky=tk.E, pady=4)
        new.data.txt_frequency_unit = tk.Label(new.data, text='days')
        new.data.txt_frequency_unit.grid(row=2, column=2, sticky=tk.W, padx=2, pady=4)

        new.data.btn_create = ttk.Button(new.data, text='Create', command=self._onclick_create)
        new.data.btn_create.grid(row=3, column=0, columnspan=3, sticky=tk.E, pady=4)

        return new

    def _edit_tab(self) -> tk.Frame:
        edit = tk.Frame(self)
        self._content.add(edit, text='Edit')

        edit.img = tk.Label(edit, image=self._image)
        edit.img.grid(row=0, column=0, sticky=tk.N+tk.S)

        edit.data = tk.Frame(edit)
        edit.data.grid(row=0, column=1, sticky=tk.N)

        edit.data.cbx_ship = ttk.Combobox(edit.data, textvariable=self._vars['edit']['selected'])
        edit.data.cbx_ship.grid(row=0, column=0, columnspan=2, sticky=tk.E+tk.W, pady=4)
        edit.data.cbx_ship.bind("<<ComboboxSelected>>", lambda event : self._onselect(event))
        edit.data.cbx_ship['values'] = self._simulater.builder.sim_obj.ships.ships_names()

        edit.data.lbl_capacity = tk.Label(edit.data, text='Capacity: ')
        edit.data.lbl_capacity.grid(row=1, column=0, sticky=tk.E, pady=4)

        edit.data.txt_capacity = tk.Entry(edit.data, textvariable=self._vars['edit']['capacity'])
        edit.data.txt_capacity.grid(row=1, column=1, sticky=tk.E, pady=4)
        edit.data.txt_capacity_unit = tk.Label(edit.data, text='tonne')
        edit.data.txt_capacity_unit.grid(row=1, column=2, sticky=tk.W, padx=2, pady=4)

        edit.data.lbl_frequency = tk.Label(edit.data, text='Frequency: ')
        edit.data.lbl_frequency.grid(row=2, column=0, sticky=tk.E, pady=4)

        edit.data.txt_frequency = tk.Entry(edit.data, textvariable=self._vars['edit']['frequency'])
        edit.data.txt_frequency.grid(row=2, column=1, sticky=tk.E, pady=4)
        edit.data.txt_frequency_unit = tk.Label(edit.data, text='days')
        edit.data.txt_frequency_unit.grid(row=2, column=2, sticky=tk.W, padx=2, pady=4)

        edit.data.btn_delete = ttk.Button(edit.data, text='Delete', command=self._onclick_delete, state='disabled')
        edit.data.btn_delete.grid(row=3, column=0, sticky=tk.W, pady=4)

        edit.data.btn_update = ttk.Button(edit.data, text='Update', command=self._onclick_update, state='disabled')
        edit.data.btn_update.grid(row=3, column=1, columnspan=2,  sticky=tk.E, pady=4)

        return edit