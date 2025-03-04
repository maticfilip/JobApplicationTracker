import customtkinter as ctk
from menu import MainMenu
from add import AddFrame
from view import ViewFrame 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PDF Editor")
        self.configure(fg_color="#333333")
        window_height = 600
        window_width = 800

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.container = ctk.CTkFrame(self)  
        self.container.pack(expand=True)

        self.frames = {}

        for F in (MainMenu, AddFrame, ViewFrame):
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")  

        self.show_frame("MainMenu")  

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()  

if __name__ == "__main__":
    app = App()
    app.mainloop()