import customtkinter as ctk

class MainMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller=controller

        ctk.CTkLabel(self, text="Job Tracker Main Menu", font=("Arial", 20, "bold")).pack(pady=20)
        ctk.CTkButton(self, text="Add Job Application", command=lambda: controller.show_frame("AddFrame")).pack(pady=10)
        ctk.CTkButton(self, text="View Applications", command=lambda: controller.show_frame("ViewFrame")).pack(pady=10)
        ctk.CTkButton(self, text="Quit", command=self.quit).pack(pady=10)
        self.pack(fill="both", expand=True, padx=10, pady=10)

