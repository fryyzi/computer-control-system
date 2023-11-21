import tkinter as tk
from left_window import LeftWindow
import webbrowser
from PIL import Image, ImageTk

class CreateWindow:
    def __init__(self):
        # Create window
        self.window = tk.Tk()
        self.window.title("TechCommander")
        self.window.geometry("1920x1080")
        self.window.configure(bg="Lightblue")


        self.main_window = LeftWindow(self.window)

        self.text_behind = tk.Label(self.window,
                                    text="TechCommander",
                                    background="Lightblue",
                                    width=30,
                                    font=("Arial", 28),
        )
        self.text_behind.place(x=460, y=0)

        self.text_behind_2 = tk.Label(self.window,
                                    text=" TechCommander - це програма для ефективного керування комп'ютером. \nВона має вбудовану базу даних, яка дозволяє швидко та зручно керувати різними програмами та налаштуваннями. \nЗабезпечте собі зручність та продуктивність в одному інтуїтивно зрозумілому інтерфейсі.",
                                    font=("Arial", 16),
                                    bg="Lightblue",
        )
        self.text_behind_2.place(x=270, y=240)
        self.text_behind.lift()

        self.open_web_site = tk.Button(self.window,
                                       text = "Відкрити браузер",
                                       font = ("Arial", 16),
                                       command = self.open_menu_site
                                       )
        self.open_web_site.pack(side="bottom")

        self.window.mainloop()

    def open_web(self):
        webbrowser.open_new("https://www.google.com.ua/?hl=ru")

    def open_MyWebSite(self):
        webbrowser.open_new("https://chat.openai.com/c/93dad4c8-87e0-468b-9fee-5491d1cf9b9d") 

    def create_button(self):
        self.test = tk.Button(self.win)
        return self.test
    
    def open_menu_site(self):
        image = Image.open("free-icon-jpg-337940.jpg")
        image = image.resize((50, 50))

        self.photo = ImageTk.PhotoImage(image)

        self.menu_site = tk.Tk()
        self.menu_site.geometry("200x200")


        self.open_my_webSite = tk.Button(self.menu_site,
                                        text = "Відкрити наш сайт!",
        )
        self.open_my_webSite.pack()

        self.open_webSite = tk.Button(self.menu_site,
                                      text = "Відкрити браузер!",
                                      command = self.open_web
        )
        self.open_webSite.pack()
    

if __name__ == "__main__":
    app = CreateWindow()
