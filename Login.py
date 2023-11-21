import tkinter as tk

class LoginOne:
    def __init__(self):
        self.Login = tk.Tk()
        self.Login.geometry("200x200")
        self.Login.configure(bg="#4021FF")

        self.Login_Label = tk.Label(
            self.Login,
            text="Login",
            font=("Times New Roman", 18),
            bg="#BAAFFF",
            width="30"
        )
        self.Login_Label.pack()

        self.Text_Login = tk.Label(
            self.Login,
            text="Введіть логін",
            background="#4021FF",
            font=("Arial", 13)
        )
        self.Text_Login.place(x=37, y=33)

        self.Login_Entry_var = tk.StringVar()
        self.Password_Entry_var = tk.StringVar()

        self.Login_Entry = tk.Entry(self.Login, textvariable=self.Login_Entry_var)
        self.Login_Entry.place(x=37, y=60)

        self.Password_Label = tk.Label(self.Login,
                                       text="Введіть пароль",
                                       background="#4021FF",
                                       font=("Arial", 13)
                                       )
        self.Password_Label.place(x=37, y=80)

        self.Password_Entry = tk.Entry(self.Login, textvariable=self.Password_Entry_var, show="*")
        self.Password_Entry.place(x=37, y=100)

        self.Login_Button = tk.Button(self.Login,
                                      text='Увійти',
                                      command=self.Logi
                                      )
        self.Login_Button.pack(side="bottom")

    def open_Login(self):
        if not self.Login.winfo_ismapped():
            self.Login.mainloop()

    def Logi(self):
        login = self.Login_Entry_var.get()
        password = self.Password_Entry_var.get()

        if login == "Fryyzi" and password == "123":
            self.Log = tk.Toplevel(self.Login)
            self.Log.geometry("200x200")
            self.Log.configure(bg="#4021FF")

            self.Log_Label = tk.Label(self.Log, text="Welcome!", font=("Arial", 14), bg="#4021FF")
            self.Log_Label.pack()

            self.Log.wait_window()

if __name__ == "__main__":
    app = LoginOne()
    app.open_Login()
