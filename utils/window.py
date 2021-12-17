import utils
import tkinter as tk

from tkinter import ttk

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kahoot Flooder")
        self.root.resizable(False, False)

        self.mainframe = ttk.Frame(self.root, padding="20 20 20 20")
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.mainframe.columnconfigure(0, weight=1)

        # create a label and entry to ask for the game id
        self.game_id_label = ttk.Label(self.mainframe, text="Game Pin:")
        self.game_id_label.grid(column=1, row=1, sticky=tk.W, padx=(0,12))
        self.game_id_entry = ttk.Entry(self.mainframe, width=10)
        self.game_id_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

        # create a label and entry to ask for the bots username
        self.username_label = ttk.Label(self.mainframe, text="Bot name:")
        self.username_label.grid(column=1, row=2, sticky=tk.W, padx=(0,12))
        self.username_entry = ttk.Entry(self.mainframe, width=10)
        self.username_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))

        # create a label and entry to ask for the amount of bots
        self.amount_label = ttk.Label(self.mainframe, text="Bot amount:")
        self.amount_label.grid(column=1, row=3, sticky=tk.W, padx=(0,12))
        self.amount_entry = ttk.Entry(self.mainframe, width=10)
        self.amount_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))

        # create a label and entry to ask for the delay between bot joins
        self.delay_label = ttk.Label(self.mainframe, text="Join delay:")
        self.delay_label.grid(column=1, row=4, sticky=tk.W, padx=(0,12))
        self.delay_entry = ttk.Entry(self.mainframe, width=10)
        self.delay_entry.grid(column=2, row=4, sticky=(tk.W, tk.E))

        # create a button to start the flood, make it span across the whole row
        self.start_button = ttk.Button(self.mainframe, text="Start", command=lambda: utils.Flooder(self.game_id_entry.get(), self.username_entry.get(), self.amount_entry.get(), self.delay_entry.get(), self.root).start())
        self.start_button.grid(column=1, row=5, columnspan=2, pady=(20, 0), sticky=(tk.W, tk.E))