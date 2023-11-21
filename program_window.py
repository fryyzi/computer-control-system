import tkinter as tk


class Program_Window:
    def __init__(self, master):
        self.master = master
        self.program_window = tk.Frame(master, bg="red", width=250)
        # Додайте сюди ваш код для створення і розміщення вмісту вікна программи

    def show_in_center(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        window_width = 250  # Ширина вікна программи
        window_height = 250  # Висота вікна программи

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

