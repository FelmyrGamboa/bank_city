import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from bank_system import BankSystem
from bank_customer import BankCustomer
from bank_teller import BankTeller
from bank_manager import BankManager
from formatbirthdate import validate_and_format_birthdate
from PIL import ImageTk, Image
from customer_interface import CustomerPage
from teller_interface import TellerPage
from manager_interface import ManagerPage

class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, role):
        super().__init__(parent)
        self.parent = parent
        self.role = role
        self.tagname = "event"
        self.login_page()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def login_page(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.login_page_img_tk = ImageTk.PhotoImage(Image.open("images/login_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.login_page_img_tk, anchor=ctk.NW)

        self.login_button_img_tk = ImageTk.PhotoImage(Image.open("images/login_button.png").resize((440, 100)))
        self.login_button = self.canvas.create_image(740, 775, image=self.login_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.login_button, "<Button-1>", self.login)

        self.login_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.login_back_button = self.canvas.create_image(20, 10, image=self.login_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.login_back_button, "<Button-1>", self.back)

        self.username_entry = ctk.CTkEntry(master=self, placeholder_text= "Enter username here", bg_color="white", fg_color="white", border_color="white", width=268, height=45, font=("Poppins", 20, "bold"), text_color="#8B3C1D", justify='center')
        self.password_entry = ctk.CTkEntry(master=self, show ="*", placeholder_text= "Enter password here", bg_color="white", fg_color="white", border_color="white", width=268, height=45, font=("Poppins", 20, "bold"), text_color="#8B3C1D", justify='center')

        self.username_entry.place(x=785, y=399, anchor=ctk.CENTER)
        self.password_entry.place(x=785, y=557, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

        self.parent.bind("<Return>", self.login)
        
    def login(self, event = None):
        system = BankSystem()
        username = self.username_entry.get()
        password = self.password_entry.get()

        system.login(self.role, username, password)
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        user = system.logged_in_user
        if isinstance(system.logged_in_user, BankCustomer):
            self.destroy()
            customer_page = CustomerPage(self.parent, user)
            customer_page.pack(fill=ctk.BOTH, expand=True)

        elif isinstance(system.logged_in_user, BankManager):
            self.destroy()
            manager_page = ManagerPage(self.parent, user)
            manager_page.pack(fill=ctk.BOTH, expand=True)

        elif isinstance(system.logged_in_user, BankTeller):
            self.destroy()
            teller_page = TellerPage(self.parent, user)
            teller_page.pack(fill=ctk.BOTH, expand=True)
        

    def back(self, event):
        self.destroy()
        previous_page = RoleSelectionPage(self.parent)
        previous_page.pack(fill=ctk.BOTH, expand=True)

class RegisterPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.tagname = "event"
        self.role = "customer"
        self.register_page()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def register_page(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.register_page_img_tk = ImageTk.PhotoImage(Image.open("images/register_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.register_page_img_tk, anchor=ctk.NW)

        self.register_button_img_tk = ImageTk.PhotoImage(Image.open("images/register_button.png").resize((440, 100)))
        self.register_button = self.canvas.create_image(740, 845, image=self.register_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.canvas.tag_bind(self.register_button, "<Button-1>", self.register)

        self.register_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.register_back_button = self.canvas.create_image(20, 10, image=self.register_back_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.canvas.tag_bind(self.register_back_button, "<Button-1>", self.back)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

        self.firstname_entry = ctk.CTkEntry(master=self, placeholder_text= "Enter first name here", bg_color="white", fg_color="white", border_color="white", width=268, height=45, font=("Poppins", 20, "bold"), text_color="#8B3C1D", justify='center')
        self.firstname_entry.place(x=428, y=352, anchor=ctk.CENTER)

        self.middlename_entry = ctk.CTkEntry(master=self, placeholder_text= "Enter middle name here", bg_color="white", fg_color="white", border_color="white", width=268, height=45, font=("Poppins", 20, "bold"), text_color="#8B3C1D", justify='center')
        self.middlename_entry.place(x=775, y=352, anchor=ctk.CENTER)

        self.lastname_entry = ctk.CTkEntry(master=self, placeholder_text= "Enter last name here", bg_color="white", fg_color="white", border_color="white", width=268, height=45, font=("Poppins", 20, "bold"), text_color="#8B3C1D", justify='center')
        self.lastname_entry.place(x=1120, y=352, anchor=ctk.CENTER)

        self.birthday_entry = ctk.CTkEntry(master=self, placeholder_text= "Format: Month Day, Year", bg_color="white", fg_color="white", border_color="white", width=390, height=45, font=("Poppins", 20, "bold"), text_color="#8B3C1D", justify='center')
        self.birthday_entry.place(x=535, y=470, anchor=ctk.CENTER)

        self.monthlysalary_entry = ctk.CTkEntry(master=self,  placeholder_text= "₱ 0.00",bg_color="white", fg_color="white", border_color="white", width=390, height=45, font=("Poppins", 20, "bold"), text_color="#8B3C1D", justify='center')
        self.monthlysalary_entry.place(x=1010, y=469, anchor=ctk.CENTER)

        self.username_entry = ctk.CTkEntry(master=self,placeholder_text= "Enter username here", bg_color="white", fg_color="white", border_color="white", width=400, height=45, font=("Poppins", 20, "bold"), text_color="#8B3C1D", justify='center')
        self.username_entry.place(x=865, y=562, anchor=ctk.CENTER)

        self.password_entry = ctk.CTkEntry(master=self,placeholder_text= "Enter password here", show="*", bg_color="white", fg_color="white", border_color="white", width=400, height=45, font=("Poppins", 20, "bold"), text_color="#8B3C1D", justify='center')
        self.password_entry.place(x=865, y=635, anchor=ctk.CENTER)

        self.parent.bind("<Return>", self.register)

    def register(self, event = None):
        first_name = self.firstname_entry.get()
        middle_name = self.middlename_entry.get()
        last_name = self.lastname_entry.get()
        birthdate = self.birthday_entry.get()
        monthly_salary = self.monthlysalary_entry.get()
        get_username = self.username_entry.get()
        get_password = self.password_entry.get()

        if BankSystem().register_user(first_name, middle_name, last_name, birthdate, monthly_salary, get_username, get_password):
            self.destroy()
            self.parent.main_page()

    def back(self, event):
        self.destroy()
        self.parent.main_page()

class RoleSelectionPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.tagname = "event"
        self.role_selection_page()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def role_selection_page(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.role_selection_bg_img_tk = ImageTk.PhotoImage(Image.open("images/chooserole_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.role_selection_bg_img_tk, anchor=ctk.NW)

        button_width, button_height = 395, 375

        self.customer_button_img_tk = ImageTk.PhotoImage(Image.open("images/customer_pic.png").resize((button_width, button_height)))
        self.teller_button_img_tk = ImageTk.PhotoImage(Image.open("images/teller_pic.png").resize((button_width, button_height)))
        self.manager_button_img_tk = ImageTk.PhotoImage(Image.open("images/manager_pic.png").resize((button_width, button_height)))

        self.customer_button = self.canvas.create_image(330, 390, image=self.customer_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.customer_button, "<Button-1>", self.select_customer)

        self.teller_button = self.canvas.create_image(765, 390, image=self.teller_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.teller_button, "<Button-1>", self.select_teller)

        self.manager_button = self.canvas.create_image(1200, 390, image=self.manager_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.manager_button, "<Button-1>", self.select_manager)

        self.register_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.register_back_button = self.canvas.create_image(20, 10, image=self.register_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.register_back_button, "<Button-1>", self.back)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def select_customer(self, event):
        self.destroy()
        login_page = LoginPage(self.parent, role="customer")
        login_page.pack(fill=ctk.BOTH, expand=True)

    def select_teller(self, event):
        self.destroy()
        login_page = LoginPage(self.parent, role="teller")
        login_page.pack(fill=ctk.BOTH, expand=True)

    def select_manager(self, event):
        self.destroy()
        login_page = LoginPage(self.parent, role="manager")
        login_page.pack(fill=ctk.BOTH, expand=True)

    def back(self, event):
        self.destroy()
        self.parent.main_page()