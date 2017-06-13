import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as msg
import os
import sqlite3

class DataSourcesGUI(tk.Tk):

    def __init__(self, data_sources=None):
        super().__init__()

        if not data_sources:
            self.data_sources = []
        else:
            self.data_sources = data_sources
    
        self.data_sources_canvas = tk.Canvas(self)

        self.data_sources_frame = tk.Frame(self.data_sources_canvas)
        self.entry_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.data_sources_canvas, orient="vertical", command=self.data_sources_canvas.yview)

        self.data_sources_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title = "Edit Data Sources"
        self.geometry("300x400")

        self.data_types = ['Excel File', 'CSV Log File', 'Files', 'Folder']

        choice = tk.StringVar(self.entry_frame)
        choice.set('Excel File')

        self.data_source_create = tk.OptionMenu(self.entry_frame, *self.data_types)        
        
        self.data_sources_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.data_sources_canvas.create_window((0, 0), window=self.data_sources_frame, anchor="n")
        self.data_source_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.entry_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.data_source_create.focus_set()

        data_source1 = tk.Label(self.data_sources_frame, text="--- Add Data Sources Here ---", bg="lightgrey",
            fg="black", pady=10)
        data_source1.bind("<Button-1>", self.remove_data_source)

        self.data_sources.append(data_source1)

        for data_source in self.data_sources:
            data_source.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_data_source)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.data_sources_canvas.bind("<Configure>", self.data_sources_width)

        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

    def add_data_source(self, event=None):
        data_source_text = self.data_source_create.get(1.0,tk.END).strip()

        if len(data_source_text) > 0:
            new_data_source = tk.Label(self.data_sources_frame, text=data_source_text, pady=10)
            self.set_data_source_colour(len(self.data_sources), new_data_source)

            new_data_source.bind("<Button-1>", self.remove_data_source)
            new_data_source.pack(side=tk.TOP, fill=tk.X)

            self.data_sources.append(new_data_source)
        
        self.data_source_create.delete(1.0, tk.END)

    def remove_data_source(self, event):
        data_source = event.widget
        if msg.askyesno("Really Delete?", "Delete " + data_source.cget("text") + "?"):
            self.data_sources.remove(event.widget)
            event.widget.destroy()
            self.recolour_data_sources()

    def recolour_data_sources(self):
        for index, data_source in enumerate(self.data_sources):
            self.set_data_source_colour(index, data_source)
    
    def set_data_source_colour(self, position, data_source):
        _, data_source_style_choice = divmod(position, 2)
        my_scheme_choice = self.colour_schemes[data_source_style_choice]

        data_source.configure(bg=my_scheme_choice["bg"])
        data_source.configure(fg=my_scheme_choice["fg"])
    
    def on_frame_configure(self, event=None):
        self.data_sources_canvas.configure(scrollregion=self.data_sources_canvas.bbox("all"))

    def data_sources_width(self, event):
        canvas_width = event.width
        self.data_sources_canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.data_sources_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1
            
            self.data_sources_canvas.yview_scroll(move, "units")
   
if __name__ == "__main__":
    data_sources_gui = DataSourcesGUI()
    data_sources_gui.mainloop()
