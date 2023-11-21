import tkinter as tk
from setting_backgrount import BackGround
from Login import LoginOne



class LeftWindow:

    def __init__(self, master):
        self.master = master
        self.program_window = tk.Frame(master, bg='#012B35')
        self.help_window = tk.Frame(master, bg='#0F434F', width=200)
        self.left_window = tk.Frame(master, bg="#427A82", width=250)
      

        self.open_window_button = tk.Button(
            master,
            width=24,
            text="Меню",
            bg="Lightblue",
            activebackground="Lightblue",
            command=self.toggle_window
        )
        self.open_window_button.pack(anchor='nw', pady=10, padx=34)

        

        self.programm_Button = tk.Button(
            self.left_window,
            text="Login",
            width=24,
            pady=10,
            padx=10,
            anchor='n',
            bg="#012E34",
            fg="white",
            activebackground="#012E34",
            activeforeground="white",
            command = self.open_Login
            
        )
        self.programm_Button.pack(pady=(20, 0))
        self.left_window.pack_propagate(False)

        # Змінено порядок додавання Frame
        self.program_window.pack_forget()
        self.help_window.pack_forget()

        self.setting_buttom = tk.Button(
            self.left_window,
            text="Налаштування",
            width=24,
            padx=10,
            pady=10,
            bg="#012E34",
            fg="white",
            activebackground="#012E34",
            activeforeground="white",
            command=self.open_setting,
        )
        self.setting_buttom.pack(side="bottom", pady=(50, 20))
        self.setting_buttom.pack_propagate(False)

        # background
        self.bg_botton = tk.Button(self.help_window,
                                   text="Змінити фон",
                                   width=24,
                                   bg="#6B949E",
                                   fg="white",
                                   command=self.open_menu_bg
                                   )
        self.bg_botton.pack()
        self.bg_botton.place(x=20, y=50)

        self.bg_Lable = tk.Label(self.help_window,
                                 text="Змінити колір заднього фону",
                                 bg="#0F434F",
                                 fg="white",
                                 activebackground="#0F434F",
                                 )
        self.bg_Lable.pack()
        self.bg_Lable.place(x=20, y=20)

    def toggle_window(self):
        if not self.left_window.winfo_ismapped():
            self.left_window.pack(side="left", fill="y", expand=False, anchor='w')
        else:
            self.left_window.pack_forget()
            self.program_window.pack_forget()
            self.help_window.pack_forget()

    def open_Login(self):
        if not hasattr(self, 'Login_menu'):
            self.Login_menu = LoginOne()
        self.Login_menu.open_Login()

    def open_menu_bg(self):
        if not hasattr(self, 'menu_bg_instance'):
            self.menu_bg_instance = BackGround()
        self.menu_bg_instance.open_menu_bg()

    def open_program_window(self):
        if not self.program_window.winfo_ismapped():
            self.program_window.pack(fill='both', expand=True)
            self.help_window.pack_forget()
            self.program_window.lift()

        else:
            self.program_window.pack_forget()

    def open_setting(self):
        if not self.help_window.winfo_ismapped():
            self.help_window.pack(fill="both", expand=True)
            self.program_window.pack_forget()
            self.help_window.lift()
        else:
            self.help_window.pack_forget()

    def hide_text(self):
        if hasattr(self.create_window_instance, 'text_off') and callable(self.create_window_instance.text_off):
            self.create_window_instance.text_off()