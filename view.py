import customtkinter as ctk
import os
import csv
from tkinter import ttk


class ViewFrame(ctk.CTkFrame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
        def load_data(tree):
            for row in tree.get_children():
                tree.delete(row)
            if os.path.exists("applications.csv"):
                with open("applications.csv", newline="") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        tree.insert("", "end", values=row)

        frame = ctk.CTkFrame(self)
        ctk.CTkLabel(frame, text="Saved Job Applications", font=("Arial", 16, "bold")).pack(pady=10)

        frame_table = ctk.CTkFrame(frame)
        frame_table.pack(fill="both", expand=True, padx=10, pady=10)
        
        columns = ("Company", "Position", "Date Applied", "Status", "Deadline", "Notes")
        tree = ttk.Treeview(frame_table, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")
        tree.pack(fill="both", expand=True)
        
        ctk.CTkButton(frame, text="Refresh Table", command=lambda: load_data(tree)).pack(pady=10)
        ctk.CTkButton(frame, text="Back", command=lambda: controller.show_frame("MainMenu")).pack(pady=5)

        
        load_data(tree)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
