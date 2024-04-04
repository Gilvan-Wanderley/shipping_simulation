from tkinter import ttk
import tkinter as tk

class TableView(ttk.Frame):
    def __init__(self, master, header: dict):
        super().__init__(master)

        self._table = ttk.Treeview(self,
                                  show='headings',
                                  columns=list(header.keys()))
        
        self.yview_scrollbar = ttk.Scrollbar(self, 
                                       orient='vertical',
                                       command= self._table.yview)
        
        for h in header:
            props = header[h]
            self._table.heading(h, text=props['text'])
            self._table.column(h, 
                                width=props['width'], 
                                anchor=props['anchor'])

        self._table.pack(side='left', fill="both", expand=True)
        self.yview_scrollbar.pack(side="right", fill="y")

    @property
    def table(self) -> ttk.Treeview:
        return self._table
    
    def add_value(self, index: int, values: list) -> None:
        self._table.insert(parent='', index=index, iid=index, values=values)

    def remove_value(self, index: int) -> None:
        self._table.delete(index)

    def exist(self, index: int) -> bool:
        return self._table.exists(index)