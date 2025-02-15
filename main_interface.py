import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from bank_system import BankSystem
from bank_customer import BankCustomer
from bank_teller import BankTeller
from bank_manager import BankManager
from formatbirthdate import validate_and_format_birthdate
from PIL import ImageTk, Image
from login_interface import RoleSelectionPage, RegisterPage

class BankSystemApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Bank City")
        self.tagname = "event"
        self.main_page()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def main_page(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack()

        self.set_bg_img = ImageTk.PhotoImage(Image.open("images/mainpage_bg.png").resize((1920, 1000)))
        self.bg_img_canvas = self.canvas.create_image(0, 0, image=self.set_bg_img, anchor=ctk.NW)

        self.login_img_tk = ImageTk.PhotoImage(Image.open("images/login_button.png").resize((440, 100)))
        self.register_img_tk = ImageTk.PhotoImage(Image.open("images/register_button.png").resize((440, 100)))
        self.exit_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((130, 110)))

        self.login_button = self.canvas.create_image(740, 705, image=self.login_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.login_button, "<Button-1>", self.login)

        self.register_button = self.canvas.create_image(740, 805, image=self.register_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.register_button, "<Button-1>", self.register)

        self.exit_button = self.canvas.create_image(1790, 0, image=self.exit_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.exit_button, "<Button-1>", self.exit)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def login(self, event = None):
        self.canvas.destroy()
        role_selection_page = RoleSelectionPage(self)
        role_selection_page.pack(fill=ctk.BOTH, expand=True)

    def register(self, event = None):
        self.canvas.destroy()
        login_page = RegisterPage(self)
        login_page.pack(fill=ctk.BOTH, expand=True)

    def exit(self, event):
        self.canvas.delete("all")
        self.thank_img = ImageTk.PhotoImage(Image.open("images/thankyou_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.thank_img, anchor=ctk.NW)
        self.canvas.after(5000, self.timed_exit)

    def timed_exit(self):
        self.destroy()

if __name__ == "__main__":
    app = BankSystemApp()
    w, h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.geometry("%dx%d+0+0" % (w, h))
    app.mainloop()