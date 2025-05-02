import tkinter
from tkinter import ttk

import sv_ttk
import darkdetect

import pywinstyles, sys, os

class ShipDetails (ttk.LabelFrame):
    COORD_WIDTH = 5;
    IMO_WIDTH = 10;

    def update_details(self, event):
        print("Update details triggered")
    def acquire(self, event):
        print("Acquire Vessel button clicked");
    
    def update_cpa(self, event):
        print("Update CPA triggered")
        lat = self.lat_entry.get()
        lon = self.lon_entry.get()

        if lat and lon:
            print(f"Latitude: {lat}, Longitude: {lon}");

    def __init__ (self, parent):
        super().__init__(parent, text="Ship Details", padding=15)
        self.parent = parent
        self.add_widgets()
    def add_widgets(self):
        self.ship_frame = ttk.Frame(self)
        self.ship_frame.grid(row=0, column=1, pady=(0, 10), sticky="ew")

        self.IMO_label = ttk.Label(self, text="IMO:")
        self.IMO_label.grid(row=0, column=0, pady=(0,10), sticky="w")

        self.IMO_entry = ttk.Entry(self.ship_frame, width=self.IMO_WIDTH)
        self.IMO_entry.grid(row=0, column=0, padx=(10, 10), sticky="w")
        self.IMO_entry.bind("<Return>", self.acquire)
        self.IMO_button = ttk.Button(self.ship_frame, text="Search", style="Accent.TButton")
        self.IMO_button.grid(row=0, column=1, sticky="e")

        self.IMO_button.bind("<Button-1>", self.acquire)

        self.vessel_name_label = ttk.Label(self, text="Name:")
        self.vessel_name_label.grid(row=1, column=0, sticky="w")
        self.vessel_name_entry = ttk.Entry(self)
        self.vessel_name_entry.grid(row=1, column=1, padx=(10, 0), sticky="ew")
        self.vessel_name_entry.bind("<Return>", self.update_details)

        self.nav_status_label = ttk.Label(self, text="Navigational Status:")
        self.nav_status_label.grid(row=2, column=0, pady=(10, 0), sticky="w")
        self.nav_status_entry = ttk.Label(self, text="Underway using engine")
        self.nav_status_entry.grid(row=2, column=1, padx=(10,0), pady=(10, 0), sticky="w")

        self.cpa_label = ttk.Label(self, text="Nearest Land:")
        self.cpa_label.grid(row=3, column=0, sticky="w")
        self.cpa_actual = ttk.Label(self, text="-")
        self.cpa_actual.grid(row=3, column=1, padx=(10, 0), sticky="ew")

        self.coord_frame = ttk.Frame(self)
        self.coord_frame.grid(row=4, column=0, columnspan=2, pady = 10, sticky="ew")
        self.lat_label = ttk.Label(self.coord_frame, text="LAT:")
        self.lat_label.grid(row=0, column=0, sticky="w")
        self.lat_entry = ttk.Entry(self.coord_frame, width=self.COORD_WIDTH)
        self.lat_entry.grid(row=0, column=1, padx=(5, 10), sticky="w")
        self.lat_entry.bind("<Return>", self.update_cpa)

        self.lon_label = ttk.Label(self.coord_frame, text="LON:")
        self.lon_label.grid(row=0, column=2, sticky="w")
        self.lon_entry = ttk.Entry(self.coord_frame, width=self.COORD_WIDTH)
        self.lon_entry.grid(row=0, column=3, padx=(5, 0), sticky="w")
        self.lon_entry.bind("<Return>", self.update_cpa)

class App(ttk.Frame):
    def __init__ (self, parent):
        super().__init__(parent, padding=15)

        for index in range(2):
            self.columnconfigure(index, weight=1)
            self.rowconfigure(index, weight=1)

        ShipDetails(self).grid(row=0, column=0, padx=(0, 10), sticky="nsew");

def main():
    root = tkinter.Tk()
    sv_ttk.set_theme("dark")
    
    root.title("Sealegs - Ship Strava Uploader Tool")

    App(root).pack(expand=True, fill="both")

    root.mainloop()

main()