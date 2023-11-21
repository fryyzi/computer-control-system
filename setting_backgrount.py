import tkinter as tk

class BackGround:
    def __init__(self):
        self.window_bg = tk.Tk()
        

    def open_menu_bg(self):
            if not self.window_bg.winfo_ismapped():
                self.window_bg.mainloop()