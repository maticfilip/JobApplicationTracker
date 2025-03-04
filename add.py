import customtkinter as ctk
import csv
from tkinter import messagebox

class AddFrame(ctk.CTkFrame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
        def clear_entries(*entries):
            for entry in entries:
                entry.delete(0, "end")

        def save_to_csv(entry_company, entry_position, entry_date, entry_status, entry_deadline, entry_notes):
            company = entry_company.get()
            position = entry_position.get()
            date_applied = entry_date.get()
            status = entry_status.get()
            deadline = entry_deadline.get()
            notes = entry_notes.get()

            if not company or not position or not date_applied or not status:
                messagebox.showerror("Error", "Please fill in all required fields.")
                return

            with open("applications.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([company, position, date_applied, status, deadline, notes])
            
            messagebox.showinfo("Success", "Application saved successfully!")
            clear_entries(entry_company, entry_position, entry_date, entry_status, entry_deadline, entry_notes)
        frame = ctk.CTkFrame(self)
        ctk.CTkLabel(frame, text="Add a New Job Application", font=("Arial", 16, "bold")).pack(pady=10)

        entry_company = ctk.CTkEntry(frame, placeholder_text="Company")
        entry_company.pack(pady=5, fill="x", padx=10)
        entry_position = ctk.CTkEntry(frame, placeholder_text="Position")
        entry_position.pack(pady=5, fill="x", padx=10)
        entry_date = ctk.CTkEntry(frame, placeholder_text="Date Applied (YYYY-MM-DD)")
        entry_date.pack(pady=5, fill="x", padx=10)
        entry_status = ctk.CTkEntry(frame, placeholder_text="Status")
        entry_status.pack(pady=5, fill="x", padx=10)
        entry_deadline = ctk.CTkEntry(frame, placeholder_text="Deadline (YYYY-MM-DD)")
        entry_deadline.pack(pady=5, fill="x", padx=10)
        entry_notes = ctk.CTkEntry(frame, placeholder_text="Notes (Optional)")
        entry_notes.pack(pady=5, fill="x", padx=10)

        ctk.CTkButton(frame, text="Save Application", command=lambda: save_to_csv(entry_company, entry_position, entry_date, entry_status, entry_deadline, entry_notes)).pack(pady=10)
        ctk.CTkButton(frame, text="Back", command=lambda: controller.show_frame("MainMenu")).pack(pady=5)
        
        frame.pack(fill="both", expand=True, padx=10, pady=10)

    

    

    

        