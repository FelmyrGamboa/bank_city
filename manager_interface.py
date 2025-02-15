import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from bank_system import BankSystem
from bank_customer import BankCustomer
from bank_teller import BankTeller
from bank_manager import BankManager
# from main_bank_system import main
from formatbirthdate import validate_and_format_birthdate
from PIL import ImageTk, Image

class ManagerPage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.manager_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def manager_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.home_page_bg_img_tk = ImageTk.PhotoImage(Image.open("images/managermenu_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.home_page_bg_img_tk, anchor=ctk.NW)

        self.use_atm_img_tk = ImageTk.PhotoImage(Image.open("images/manager_useatm.png"))
        self.admin_dashboard_img_tk = ImageTk.PhotoImage(Image.open("images/manager_admindashboard.png"))

        self.use_atm_button = self.canvas.create_image(1020, 140, image=self.use_atm_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.admin_dashboard_button = self.canvas.create_image(280, 360, image=self.admin_dashboard_img_tk, anchor=ctk.NW, tag=self.tagname)

        self.canvas.tag_bind(self.use_atm_button, "<Button-1>", self.use_atm)
        self.canvas.tag_bind(self.admin_dashboard_button, "<Button-1>", self.admin_dashboard)

        self.manager_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.manager_back_button = self.canvas.create_image(20, 10, image=self.manager_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.manager_back_button, "<Button-1>", self.back)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def use_atm(self, event):
        self.destroy()
        atm_menu = ATMMenu(self.master, self.user, previous_page=self.master)
        atm_menu.pack(fill=ctk.BOTH, expand=True)

    def admin_dashboard(self, event):
        self.destroy()
        back_page = AdminDashboard(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def back(self, event):
        self.confirm_logout()

    def confirm_logout(self):
        response = CTkMessagebox(master=self, title="Logout", message="Are you sure you want to log out?", icon="question", option_1="Yes", option_2="No", sound=True)
        if response.get() == "Yes":
            self.destroy()
            self.parent.main_page()

class AdminDashboard(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.admin_dashboard_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def admin_dashboard_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.admin_dashboard_bg_img_tk = ImageTk.PhotoImage(Image.open("images/admindashboard_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.admin_dashboard_bg_img_tk, anchor=ctk.NW)

        self.manager_button_img_tk = ImageTk.PhotoImage(Image.open("images/manager_button.png"))
        self.admin_button_img_tk = ImageTk.PhotoImage(Image.open("images/manager_button.png"))

        self.manager_button = self.canvas.create_image(1100, 210, image=self.manager_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.admin_button = self.canvas.create_image(1100, 340, image=self.admin_button_img_tk, anchor=ctk.NW, tag=self.tagname)

        self.canvas.tag_bind(self.manager_button, "<Button-1>", self.show_manager_teller_operations)
        self.canvas.tag_bind(self.admin_button, "<Button-1>", self.show_manager_operations)

        self.admin_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.admin_back_button = self.canvas.create_image(20, 10, image=self.admin_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.admin_back_button, "<Button-1>", self.previous_page)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def show_manager_operations(self, event):
        self.destroy()
        manager_operations_page = ManagerOperations(self.parent, self.user)
        manager_operations_page.pack(fill=ctk.BOTH, expand=True)

    def show_manager_teller_operations(self, event):
        self.destroy()
        manager_teller_operations_page = Manager_Teller_Operations(self.parent, self.user)
        manager_teller_operations_page.pack(fill=ctk.BOTH, expand=True)

    def previous_page(self, event):
        self.destroy()
        back_page = ManagerPage(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)


class Manager_Teller_Operations(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.manager_operations_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def manager_operations_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.ManagerPov_bg_img_tk = ImageTk.PhotoImage(Image.open("images/ManagerPov_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.ManagerPov_bg_img_tk, anchor=ctk.NW)

        self.teller_op_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.teller_op_back_button = self.canvas.create_image(20, 10, image=self.teller_op_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.teller_op_back_button, "<Button-1>", self.previous_page)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

        x1, y1, r1 = 1180, 283, 30
        self.transact_with_customer_button = self.canvas.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill="#FFFFD2", outline="#AF663D", width=5)
        self.canvas.tag_bind(self.transact_with_customer_button, "<Button-1>", self.manager_transact_with_customer_action)
        self.canvas.tag_bind(self.transact_with_customer_button, "<Enter>", lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(self.transact_with_customer_button, "<Leave>", lambda event: self.canvas.config(cursor=""))

        x2, y2, r2 = 1180, 425, 30
        self.manage_customer_account_button = self.canvas.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill="#FFFFD2", outline="#AF663D", width=5)
        self.canvas.tag_bind(self.manage_customer_account_button, "<Button-1>", self.manage_customer_account_action)
        self.canvas.tag_bind(self.manage_customer_account_button, "<Enter>", lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(self.manage_customer_account_button, "<Leave>", lambda event: self.canvas.config(cursor=""))

    def previous_page(self, event):
        self.destroy()
        back_page = AdminDashboard(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def manager_transact_with_customer_action(self, event):
        self.destroy()
        Transact_with_Customer_page = Manager_Transact_with_Customer(self.parent, self.user)
        Transact_with_Customer_page.pack(fill=ctk.BOTH, expand=True)

    def manage_customer_account_action(self, event):
        self.destroy()
        Manage_Customer_Account_page = ManagerPov_Manage_Customer_Account(self.parent, self.user)
        Manage_Customer_Account_page.pack(fill=ctk.BOTH, expand=True)


class Manager_Transact_with_Customer(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.teller_username_accnum_menu()

    def enter(self, event=None):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def teller_username_accnum_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.check_balance_page_img_tk = ImageTk.PhotoImage(Image.open("images/manager_usernameaccnum.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.check_balance_page_img_tk, anchor=ctk.NW)

        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((300, 120)))
        self.enter_button = self.canvas.create_image(820, 775, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", lambda event: self.validate_customer())

        self.check_balance_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.check_balance_button = self.canvas.create_image(20, 10, image=self.check_balance_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.check_balance_button, "<Button-1>", self.previous_page)

        self.customer_name_entry = ctk.CTkEntry(master=self,  placeholder_text= "Enter customer's name here",bg_color="white", fg_color="white", border_color="white", width=540, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.account_number_entry = ctk.CTkEntry(self, placeholder_text="Enter customer's account number here", bg_color="white", fg_color="white", border_color="white", width=540, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')

        self.customer_name_entry.place(x=770, y=367, anchor=ctk.CENTER)
        self.account_number_entry.place(x=770, y=560, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())
    
    def validate_customer(self):
        username = self.customer_name_entry.get()
        account_number = self.account_number_entry.get()
        system = BankSystem()
        if system.verify_customer(self.user, username, account_number):
            self.destroy()
            transact_with_customer_page = ManagerPov_Transact_with_Customer(self.parent, self.user, username)
            transact_with_customer_page.pack(fill=ctk.BOTH, expand=True)
        else:
            self.customer_name_entry.delete(0, 'end')
            self.account_number_entry.delete(0, 'end')

    def previous_page(self, event):
        self.destroy()
        back_page = Manager_Teller_Operations(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ManagerPov_Transact_with_Customer(ctk.CTkFrame):
    def __init__(self, parent, user, username):
        super().__init__(parent)
        self.parent = parent
        self.username = username
        self.user = user
        self.tagname = "event"
        self.manager_transact_with_customer_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def manager_transact_with_customer_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.ManagerPov_bg_img_tk = ImageTk.PhotoImage(Image.open("images/ManagerTransactwithCustomer_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.ManagerPov_bg_img_tk, anchor=ctk.NW)

        self.teller_op_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.teller_op_back_button = self.canvas.create_image(20, 10, image=self.teller_op_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.teller_op_back_button, "<Button-1>", self.previous_page)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

        x1, y1, r1 = 1250, 290, 23
        self.check_balance_button = self.canvas.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill="#FFFFD2", outline="#AF663D", width=5)
        self.canvas.tag_bind(self.check_balance_button, "<Button-1>", self.manager_check_balance_action)
        self.canvas.tag_bind(self.check_balance_button, "<Enter>", lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(self.check_balance_button, "<Leave>", lambda event: self.canvas.config(cursor=""))

        x2, y2, r2 = 1250, 380, 23
        self.deposit_button = self.canvas.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill="#FFFFD2", outline="#AF663D", width=5)
        self.canvas.tag_bind(self.deposit_button, "<Button-1>", self.manager_deposit_action)
        self.canvas.tag_bind(self.deposit_button, "<Enter>", lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(self.deposit_button, "<Leave>", lambda event: self.canvas.config(cursor=""))

        x3, y3, r3 = 1250, 470, 23
        self.withdraw_button = self.canvas.create_oval(x3 - r3, y3 - r3, x3 + r3, y3 + r3, fill="#FFFFD2", outline="#AF663D", width=5)
        self.canvas.tag_bind(self.withdraw_button, "<Button-1>", self.manager_withdraw_action)
        self.canvas.tag_bind(self.withdraw_button, "<Enter>", lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(self.withdraw_button, "<Leave>", lambda event: self.canvas.config(cursor=""))

    def manager_check_balance_action(self, event):
        system = BankSystem()
        checked = system.check_account(self.username)
        if checked:
            self.destroy()
            back_page = ManagerPov_Teller_Check_Balance(self.parent, self.user, self.username)
            back_page.pack(fill=ctk.BOTH, expand=True)

    def manager_deposit_action(self, event):
        system = BankSystem()
        checked = system.check_account(self.username)
        if checked:
            self.destroy()
            back_page = ManagerPov_Teller_Deposit(self.parent, self.user, self.username)
            back_page.pack(fill=ctk.BOTH, expand=True)

    def manager_withdraw_action(self,event):
        system = BankSystem()
        checked = system.check_account(self.username)
        if checked:
            self.destroy()
            back_page = ManagerPov_Teller_Withdraw(self.parent, self.user, self.username)
            back_page.pack(fill=ctk.BOTH, expand=True)

    def previous_page(self, event):
        self.destroy()
        back_page = Manager_Teller_Operations(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ManagerPov_Teller_Check_Balance(ctk.CTkFrame):
    def __init__(self, parent, user, username):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.username = username
        self.tagname = "event"
        self.manager_check_balance_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def manager_check_balance_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.check_balance_page_img_tk = ImageTk.PhotoImage(Image.open("images/manager_teller_check_balance.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.check_balance_page_img_tk, anchor=ctk.NW)

        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((300, 120)))
        self.enter_button = self.canvas.create_image(820, 775, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", lambda event: self.check_balance())

        self.check_balance_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.check_balance_button = self.canvas.create_image(20, 10, image=self.check_balance_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.check_balance_button, "<Button-1>", self.previous_page)

        self.amount_entry = ctk.CTkEntry(master=self,placeholder_text="Format: Month Day, Year", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.amount_entry.place(x=787, y=450, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def check_balance(self):
        amount = None
        birthday = self.amount_entry.get()
        action = "Check Balance"
        system = BankSystem()
        system.transact_with_customer(self.user, birthday, amount, action, self.username)
        self.amount_entry.delete(0, 'end')

    def previous_page(self, event):
        self.destroy()
        back_page = ManagerPov_Transact_with_Customer(self.parent, self.user, self.username)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ManagerPov_Teller_Deposit(ctk.CTkFrame):
    def __init__(self, parent, user, username):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.username = username
        self.tagname = "event"
        self.manager_deposit_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def manager_deposit_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.check_balance_page_img_tk = ImageTk.PhotoImage(Image.open("images/manager_teller_deposit.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.check_balance_page_img_tk, anchor=ctk.NW)

        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((300, 120)))
        self.enter_button = self.canvas.create_image(820, 775, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", lambda event: self.deposit_transaction())

        self.teller_deposit_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.teller_deposit_button = self.canvas.create_image(20, 10, image=self.teller_deposit_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.teller_deposit_button, "<Button-1>", self.previous_page)

        self.amount_entry = ctk.CTkEntry(master=self,placeholder_text="₱ 0.00", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.birthday_entry = ctk.CTkEntry(master=self,placeholder_text="Format: Month Day, Year", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')

        self.amount_entry.place(x=787, y=367, anchor=ctk.CENTER)
        self.birthday_entry.place(x=787, y=567, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def deposit_transaction(self):
        amount = self.amount_entry.get()
        birthday = self.birthday_entry.get()
        action = "Deposit"
        system = BankSystem()
        system.transact_with_customer(self.user, birthday, amount, action, self.username)
        self.amount_entry.delete(0, 'end')
        self.birthday_entry.delete(0, 'end')

    def previous_page(self, event):
        self.destroy()
        back_page = ManagerPov_Transact_with_Customer(self.parent, self.user, self.username)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ManagerPov_Teller_Withdraw(ctk.CTkFrame):
    def __init__(self, parent, user, username):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.username = username
        self.tagname = "event"
        self.manager_withdraw_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def manager_withdraw_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.teller_withdraw_page_img_tk = ImageTk.PhotoImage(Image.open("images/manager_teller_withdraw.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.teller_withdraw_page_img_tk, anchor=ctk.NW)

        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((300, 120)))
        self.enter_button = self.canvas.create_image(820, 775, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", lambda event: self.withdraw_transaction())

        self.teller_withdraw_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.teller_withdraw_button = self.canvas.create_image(20, 10, image=self.teller_withdraw_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.teller_withdraw_button, "<Button-1>", self.previous_page)

        self.amount_entry = ctk.CTkEntry(master=self,placeholder_text="₱ 0.00", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.birthday_entry = ctk.CTkEntry(master=self,placeholder_text="Format: Month Day, Year", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')

        self.amount_entry.place(x=787, y=367, anchor=ctk.CENTER)
        self.birthday_entry.place(x=787, y=567, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())
    
    def withdraw_transaction(self):
        amount = self.amount_entry.get()
        birthday = self.birthday_entry.get()
        action = "Withdraw"
        system = BankSystem()
        system.transact_with_customer(self.user, birthday, amount, action, self.username)
        self.amount_entry.delete(0, 'end')
        self.birthday_entry.delete(0, 'end')


    def previous_page(self, event):
        self.destroy()
        back_page = ManagerPov_Transact_with_Customer(self.parent, self.user, self.username)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ManagerPov_Manage_Customer_Account(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.manager_customer_account_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def manager_customer_account_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.TellerPov_bg_img_tk = ImageTk.PhotoImage(Image.open("images/manager_manage_customer_account_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.TellerPov_bg_img_tk, anchor=ctk.NW)

        self.teller_op_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.teller_op_back_button = self.canvas.create_image(20, 10, image=self.teller_op_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.teller_op_back_button, "<Button-1>", self.previous_page)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

        x1, y1, r1 = 1088, 252, 17
        self.process_new_account_request_button = self.canvas.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill="#FFFFD2", outline="#AF663D", width=5)
        self.canvas.tag_bind(self.process_new_account_request_button, "<Button-1>", self.process_new_account_request_action)
        self.canvas.tag_bind(self.process_new_account_request_button, "<Enter>", lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(self.process_new_account_request_button, "<Leave>", lambda event: self.canvas.config(cursor=""))

        x2, y2, r2 = 1476, 252, 17
        self.request_account_deactivation_button = self.canvas.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill="#FFFFD2", outline="#AF663D", width=5)
        self.canvas.tag_bind(self.request_account_deactivation_button, "<Button-1>", self.request_account_deactivation_action)
        self.canvas.tag_bind(self.request_account_deactivation_button, "<Enter>", lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(self.request_account_deactivation_button, "<Leave>", lambda event: self.canvas.config(cursor=""))

        x3, y3, r3 = 1088, 373, 17
        self.transfer_loan_amount_button = self.canvas.create_oval(x3 - r3, y3 - r3, x3 + r3, y3 + r3, fill="#FFFFD2", outline="#AF663D", width=5)
        self.canvas.tag_bind(self.transfer_loan_amount_button, "<Button-1>", self.transfer_loan_amount_action)
        self.canvas.tag_bind(self.transfer_loan_amount_button, "<Enter>", lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(self.transfer_loan_amount_button, "<Leave>", lambda event: self.canvas.config(cursor=""))

        x4, y4, r4 = 1476, 373, 17
        self.process_lock_account_request_button = self.canvas.create_oval(x4 - r4, y4 - r4, x4 + r4, y4 + r4, fill="#FFFFD2", outline="#AF663D", width=5)
        self.canvas.tag_bind(self.process_lock_account_request_button, "<Button-1>", self.process_lock_account_request_action)
        self.canvas.tag_bind(self.process_lock_account_request_button, "<Enter>", lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(self.process_lock_account_request_button, "<Leave>", lambda event: self.canvas.config(cursor=""))

        x5, y5, r5 = 1267, 453, 17
        self.process_unlock_account_request_button = self.canvas.create_oval(x5 - r5, y5 - r5, x5 + r5, y5 + r5, fill="#FFFFD2", outline="#AF663D", width=5)
        self.canvas.tag_bind(self.process_unlock_account_request_button, "<Button-1>", self.process_unlock_account_request_action)
        self.canvas.tag_bind(self.process_unlock_account_request_button, "<Enter>", lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(self.process_unlock_account_request_button, "<Leave>", lambda event: self.canvas.config(cursor=""))

    def process_new_account_request_action(self, event):
        self.destroy()
        back_page = ManagerPov_TellerProcessNewAccountRequest(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def request_account_deactivation_action(self, event):
        self.destroy()
        back_page = ManagerPov_TellerRequestAccountDeactivation(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def transfer_loan_amount_action(self,event):
        self.destroy()
        back_page = ManagerPov_TellerTransferLoanAmmount(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def process_lock_account_request_action(self,event):
        self.destroy()
        back_page = ManagerPov_TellerProcessLockAccountRequest(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def process_unlock_account_request_action(self,event):
        self.destroy()
        back_page = ManagerPov_TellerProcessUnlockAccountRequest(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def previous_page(self, event):
        self.destroy()
        back_page = Manager_Teller_Operations(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ManagerPov_TellerProcessNewAccountRequest(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.process_new_acc_request_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def process_new_acc_request_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.tellerprocess_account_request_bg_img_tk = ImageTk.PhotoImage(Image.open("images/manager_process_account_request.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.tellerprocess_account_request_bg_img_tk, anchor=ctk.NW)

        system = BankSystem()
        self.accounts = system.managerpov_process_acc(self.user)
        self.label = ctk.CTkLabel(self, text=f"{self.accounts}", font=("Poppins", 35, "bold"), text_color="#8B3C1D", bg_color="white", fg_color="white", width=100, height=20)
        self.label.place(x=785, y=399, anchor=ctk.CENTER)

        self.teller_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.teller_back_button = self.canvas.create_image(20, 10, image=self.teller_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.teller_back_button, "<Button-1>", self.previous_page)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def previous_page(self, event):
        self.destroy()
        back_page =  ManagerPov_Manage_Customer_Account(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ManagerPov_TellerRequestAccountDeactivation(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.request_account_deactivation_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def request_account_deactivation_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.tellerrequest_account_deactivation_bg_img_tk = ImageTk.PhotoImage(Image.open("images/manager_tellerrequest_acc_deactivation.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.tellerrequest_account_deactivation_bg_img_tk, anchor=ctk.NW)

        self.teller_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.teller_back_button = self.canvas.create_image(20, 10, image=self.teller_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.teller_back_button, "<Button-1>", self.previous_page)

        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((400, 150)))
        self.enter_button = self.canvas.create_image(750, 735, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", self.request_account_deactivation)


        self.fullname_entry = ctk.CTkEntry(master=self,placeholder_text="Enter customer's fullname here", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 34, "bold"), text_color="#8B3C1D", justify='center')
        self.fullname_entry.place(x=780, y=455, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def request_account_deactivation(self, event):
        name = self.fullname_entry.get()
        system = BankSystem()
        system.managerpov_request_account_deactivation(self.user, name)
        self.fullname_entry.delete(0, 'end')

    def previous_page(self, event):
        self.destroy()
        back_page = ManagerPov_Manage_Customer_Account(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ManagerPov_TellerTransferLoanAmmount(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.transfer_loan_ammount_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def transfer_loan_ammount_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.tellertransfer_loan_ammount_bg_img_tk = ImageTk.PhotoImage(Image.open("images/manager_tellertransfer_loan_amount.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.tellertransfer_loan_ammount_bg_img_tk, anchor=ctk.NW)

        self.teller_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.teller_back_button = self.canvas.create_image(20, 10, image=self.teller_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.teller_back_button, "<Button-1>", self.previous_page)

        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((400, 150)))
        self.enter_button = self.canvas.create_image(750, 735, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", self.transfer_loan_amount)

        self.username_entry = ctk.CTkEntry(master=self,placeholder_text="Enter customer's username here", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 34, "bold"), text_color="#8B3C1D", justify='center')
        self.username_entry.place(x=780, y=453, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def transfer_loan_amount(self,event):
        account = self.username_entry.get()
        system = BankSystem()
        system.managerpov_transfer_loan_amount(self.user, account)
        self.username_entry.delete(0, 'end')

    def previous_page(self, event):
        self.destroy()
        back_page =  ManagerPov_Manage_Customer_Account(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ManagerPov_TellerProcessLockAccountRequest(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.process_lock_acc_request_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def process_lock_acc_request_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.tellerprocess_lock_acc_request_bg_img_tk = ImageTk.PhotoImage(Image.open("images/process_account_request.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.tellerprocess_lock_acc_request_bg_img_tk, anchor=ctk.NW)

        self.teller_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.teller_back_button = self.canvas.create_image(20, 10, image=self.teller_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.teller_back_button, "<Button-1>", self.previous_page)

        system = BankSystem()
        self.accounts = system.managerpov_process_lock_acc(self.user)
        self.label = ctk.CTkLabel(self, text=f"{self.accounts}", font=("Poppins", 35, "bold"), text_color="#8B3C1D", bg_color="white", fg_color="white", width=100, height=20)
        self.label.place(x=785, y=399, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def previous_page(self, event):
        self.destroy()
        back_page =  ManagerPov_Manage_Customer_Account(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ManagerPov_TellerProcessUnlockAccountRequest(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.process_unlock_acc_request_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def process_unlock_acc_request_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.process_unlock_acc_request_bg_img_tk = ImageTk.PhotoImage(Image.open("images/process_account_request.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.process_unlock_acc_request_bg_img_tk, anchor=ctk.NW)

        system = BankSystem()
        self.accounts = system.managerpov_process_unlock_acc(self.user)
        self.label = ctk.CTkLabel(self, text=f"{self.accounts}", font=("Poppins", 35, "bold"), text_color="#8B3C1D", bg_color="white", fg_color="white", width=100, height=20)
        self.label.place(x=785, y=399, anchor=ctk.CENTER)

        self.teller_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.teller_back_button = self.canvas.create_image(20, 10, image=self.teller_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.teller_back_button, "<Button-1>", self.previous_page)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def previous_page(self,event):
        self.destroy()
        back_page =  ManagerPov_Manage_Customer_Account(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ManagerOperations(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.buttons = {}
        self.manager_operations_menu()

    def enter(self, event):
        self.canvas.config(cursor="hand2")

    def leave(self, event):
        self.canvas.config(cursor="")

    def manager_operations_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.manager_operations_bg_img_tk = ImageTk.PhotoImage(Image.open("images/manageroperations_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.manager_operations_bg_img_tk, anchor=ctk.NW)

        self.approve_account_request_img_tk = ImageTk.PhotoImage(Image.open("images/manager_button.png"))
        self.approve_loan_application_img_tk = ImageTk.PhotoImage(Image.open("images/manager_button.png"))
        self.approve_account_deactivation_img_tk = ImageTk.PhotoImage(Image.open("images/manager_button.png"))
        self.approve_request_to_lock_account_img_tk = ImageTk.PhotoImage(Image.open("images/manager_button.png"))
        self.approve_request_to_unlock_account_img_tk = ImageTk.PhotoImage(Image.open("images/manager_button.png"))
        self.approve_lock_account_img_tk = ImageTk.PhotoImage(Image.open("images/manager_button.png"))
        self.approve_unlock_account_img_tk = ImageTk.PhotoImage(Image.open("images/manager_button.png"))

        self.buttons["approve_account_request"] = self.canvas.create_image(357, 125, image=self.approve_account_request_img_tk, anchor=ctk.NW)
        self.buttons["approve_loan_application"] = self.canvas.create_image(357, 260, image=self.approve_loan_application_img_tk, anchor=ctk.NW)
        self.buttons["approve_account_deactivation"] = self.canvas.create_image(357, 380, image=self.approve_account_deactivation_img_tk, anchor=ctk.NW)
        self.buttons["approve_request_to_lock_account"] = self.canvas.create_image(980, 125, image=self.approve_request_to_lock_account_img_tk, anchor=ctk.NW)
        self.buttons["approve_request_to_unlock_account"] = self.canvas.create_image(980, 258, image=self.approve_request_to_unlock_account_img_tk, anchor=ctk.NW)
        self.buttons["approve_lock_account"] = self.canvas.create_image(980, 380, image=self.approve_lock_account_img_tk, anchor=ctk.NW)
        self.buttons["approve_unlock_account"] = self.canvas.create_image(645, 525, image=self.approve_unlock_account_img_tk, anchor=ctk.NW)

        self.canvas.tag_bind(self.buttons["approve_account_request"], "<Button-1>", self.approve_account_request_page)
        self.canvas.tag_bind(self.buttons["approve_loan_application"], "<Button-1>", self.approve_loan_application_page)
        self.canvas.tag_bind(self.buttons["approve_account_deactivation"], "<Button-1>", self.approve_account_deactivation_page)
        self.canvas.tag_bind(self.buttons["approve_request_to_lock_account"], "<Button-1>", self.approve_request_to_lock_account_page)
        self.canvas.tag_bind(self.buttons["approve_request_to_unlock_account"], "<Button-1>", self.approve_request_to_unlock_account_page)
        self.canvas.tag_bind(self.buttons["approve_lock_account"], "<Button-1>", self.lock_account_page)
        self.canvas.tag_bind(self.buttons["approve_unlock_account"], "<Button-1>", self.unlock_account_page)

        for button in self.buttons.values():
            self.canvas.tag_bind(button, "<Enter>", self.enter)
            self.canvas.tag_bind(button, "<Leave>", self.leave)

        self.manager_operations_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.manager_operations_back_button = self.canvas.create_image(20, 10, image=self.manager_operations_back_button_img_tk, anchor=ctk.NW)
        self.canvas.tag_bind(self.manager_operations_back_button, "<Button-1>", self.previous_page)
        self.canvas.tag_bind(self.manager_operations_back_button, "<Enter>", self.enter)
        self.canvas.tag_bind(self.manager_operations_back_button, "<Leave>", self.leave)

    def approve_account_request_page(self, event):
        self.destroy()
        approve_account_request_page = ApproveAccountRequestPage(self.parent, self.user)
        approve_account_request_page.pack(fill=ctk.BOTH, expand=True)

    def approve_loan_application_page(self, event):
        self.destroy()
        approve_loan_application_page = ApproveLoanApplicationPage(self.parent, self.user)
        approve_loan_application_page.pack(fill=ctk.BOTH, expand=True)

    def approve_account_deactivation_page(self, event):
        self.destroy()
        approve_account_deactivation_page = ApproveAccountDeactivationPage(self.parent, self.user)
        approve_account_deactivation_page.pack(fill=ctk.BOTH, expand=True)

    def approve_request_to_lock_account_page(self, event):
        self.destroy()
        approve_request_to_lock_account_page = ApproveRequestToLockAccountPage(self.parent, self.user)
        approve_request_to_lock_account_page.pack(fill=ctk.BOTH, expand=True)

    def approve_request_to_unlock_account_page(self, event):
        self.destroy()
        approve_request_to_unlock_account_page = ApproveRequestToUnlockAccountPage(self.parent, self.user)
        approve_request_to_unlock_account_page.pack(fill=ctk.BOTH, expand=True)

    def lock_account_page(self, event):
        self.destroy()
        lock_account_page = LockAccountPage(self.parent, self.user)
        lock_account_page.pack(fill=ctk.BOTH, expand=True)

    def unlock_account_page(self, event):
        self.destroy()
        unlock_account_page = UnlockAccountPage(self.parent, self.user)
        unlock_account_page.pack(fill=ctk.BOTH, expand=True)

    def previous_page(self, event=None):
        self.destroy()
        back_page = AdminDashboard(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ApproveAccountRequestPage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.approve_account_request_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def approve_account_request_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.approve_account_request_bg_img_tk = ImageTk.PhotoImage(Image.open("images/process_account_request.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.approve_account_request_bg_img_tk, anchor=ctk.NW)

        system = BankSystem()
        self.processed_accounts = system.approve_account(self.user)
        self.label = ctk.CTkLabel(self, text=f"{self.processed_accounts}", font=("Poppins", 35, "bold"), text_color="#8B3C1D", bg_color="white", fg_color="white", width=100, height=20)
        self.label.place(x=785, y=399, anchor=ctk.CENTER)

        self.approve_account_request_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.approve_account_request_back_button = self.canvas.create_image(20, 10, image=self.approve_account_request_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.approve_account_request_back_button, "<Button-1>", self.previous_page)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())
    
    def previous_page(self, event):
        self.destroy()
        back_page = ManagerOperations(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ApproveLoanApplicationPage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.approve_loan_application_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def approve_loan_application_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.approve_loan_application_bg_img_tk = ImageTk.PhotoImage(Image.open("images/ManagerApproveLoanApplication_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.approve_loan_application_bg_img_tk, anchor=ctk.NW)

        self.approve_loan_application_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.approve_loan_application_back_button = self.canvas.create_image(20, 10, image=self.approve_loan_application_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.approve_loan_application_back_button, "<Button-1>", self.previous_page)
        
        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((400, 150)))
        self.enter_button = self.canvas.create_image(750, 735, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", self.loan_approval) 

        self.username_entry = ctk.CTkEntry(master=self,placeholder_text="Enter customer's username here", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.username_entry.place(x=780, y=453, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def loan_approval(self, event):
        customer_username = self.username_entry.get()
        system = BankSystem()
        system.approve_loan(self.user, customer_username)
        self.username_entry.delete(0, 'end')

    def previous_page(self, event=None):
        self.destroy()
        back_page = ManagerOperations(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ApproveAccountDeactivationPage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.approve_account_deactivation_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def approve_account_deactivation_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)
        self.bg_img_tk = ImageTk.PhotoImage(Image.open("images/approve_account_deactivation_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.bg_img_tk, anchor=ctk.NW)

        self.manager_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.manager_back_button = self.canvas.create_image(20, 10, image=self.manager_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.manager_back_button, "<Button-1>", self.previous_page)

        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((400, 150)))
        self.enter_button = self.canvas.create_image(750, 735, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", self.approve_acc_deact) 

        self.username_entry = ctk.CTkEntry(master=self,placeholder_text="Enter customer's username here", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.username_entry.place(x=765, y=335, anchor=ctk.CENTER)

        self.fullname_entry = ctk.CTkEntry(master=self,placeholder_text="Enter customer's fullname here", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.fullname_entry.place(x=765, y=527, anchor=ctk.CENTER)
    
        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def approve_acc_deact(self, event):
        teller_username = self.username_entry.get()
        customer_fullname = self.fullname_entry.get()
        system = BankSystem()
        system.approve_account_deactivation(self.user, teller_username, customer_fullname)
        self.username_entry.delete(0, 'end')
        self.fullname_entry.delete(0, 'end')

    def previous_page(self, event=None):
        self.destroy()
        back_page = ManagerOperations(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ApproveRequestToLockAccountPage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.approve_request_lock_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def approve_request_lock_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.approve_request_lock_bg_img_tk = ImageTk.PhotoImage(Image.open("images/process_account_request.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.approve_request_lock_bg_img_tk, anchor=ctk.NW)

        system = BankSystem()
        self.approved_accounts = system.approve_lock_account(self.user)
        self.label = ctk.CTkLabel(self, text=f"{self.approved_accounts}", font=("Poppins", 35, "bold"), text_color="#8B3C1D", bg_color="white", fg_color="white", width=100, height=20)
        self.label.place(x=785, y=399, anchor=ctk.CENTER)

        self.approve_request_lock_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.approve_request_lock_back_button = self.canvas.create_image(20, 10, image=self.approve_request_lock_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.approve_request_lock_back_button, "<Button-1>", self.previous_page)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def previous_page(self, event=None):
        self.destroy()
        back_page = ManagerOperations(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ApproveRequestToUnlockAccountPage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.approve_request_unlock_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def approve_request_unlock_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.approve_request_unlock_bg_img_tk = ImageTk.PhotoImage(Image.open("images/process_account_request.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.approve_request_unlock_bg_img_tk, anchor=ctk.NW)

        system = BankSystem()
        self.approved_accounts = system.approve_unlock_account(self.user)
        self.label = ctk.CTkLabel(self, text=f"{self.approved_accounts}", font=("Poppins", 35, "bold"), text_color="#8B3C1D", bg_color="white", fg_color="white", width=100, height=20)
        self.label.place(x=785, y=399, anchor=ctk.CENTER)

        self.approve_request_unlock_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.approve_request_unlock_back_button = self.canvas.create_image(20, 10, image=self.approve_request_unlock_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.approve_request_unlock_back_button, "<Button-1>", self.previous_page)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def previous_page(self, event=None):
        self.destroy()
        back_page = ManagerOperations(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class LockAccountPage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.lock_account_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def lock_account_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.lock_account_bg_img_tk = ImageTk.PhotoImage(Image.open("images/ManagerApproveLoanApplication_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.lock_account_bg_img_tk, anchor=ctk.NW)

        self.lock_account_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.lock_account_back_button = self.canvas.create_image(20, 10, image=self.lock_account_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.lock_account_back_button, "<Button-1>", self.previous_page)

        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((400, 150)))
        self.enter_button = self.canvas.create_image(750, 735, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", self.lock_account)

        self.username_entry = ctk.CTkEntry(master=self,placeholder_text="Enter customer's username here", bg_color="white", fg_color="white", border_color="white", width=380, height=33, font=("Poppins", 24, "bold"), text_color="#8B3C1D", justify='center')
        self.username_entry.place(x=780, y=453, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def lock_account(self, event):
        account = self.username_entry.get()
        system = BankSystem()
        system.lock_account(self.user, account)
        self.username_entry.delete(0, 'end')

    def previous_page(self, event=None):
        self.destroy()
        back_page = ManagerOperations(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class UnlockAccountPage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.unlock_account_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def unlock_account_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.unlock_account_bg_img_tk = ImageTk.PhotoImage(Image.open("images/ManagerApproveLoanApplication_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.unlock_account_bg_img_tk, anchor=ctk.NW)

        self.unlock_account_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.unlock_account_back_button = self.canvas.create_image(20, 10, image=self.unlock_account_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.unlock_account_back_button, "<Button-1>", self.previous_page)

        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((400, 150)))
        self.enter_button = self.canvas.create_image(750, 735, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", self.unlock_account)

        self.username_entry = ctk.CTkEntry(master=self,placeholder_text="Enter customer's username here", bg_color="white", fg_color="white", border_color="white", width=380, height=33, font=("Poppins", 24, "bold"), text_color="#8B3C1D", justify='center')
        self.username_entry.place(x=780, y=453, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def unlock_account(self, event):
        account = self.username_entry.get()
        system = BankSystem()
        system.unlock_account(self.user, account)
        self.username_entry.delete(0, 'end')

    def previous_page(self, event=None):
        self.destroy()
        back_page = ManagerOperations(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class ATMMenu(ctk.CTkFrame):
    def __init__(self, parent, user, previous_page):
        super().__init__(parent)
        self.parent = parent
        self.previous_page = previous_page
        self.user = user
        self.tagname = "event"
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)
        self.num_buttons = []
        self.entry_new_pin = None
        self.entry_old_pin = None
        self.entry_field = None
        self.active_field = None
        self.load_images()
        self.enter_pin_page()

    def load_images(self):
        self.images = {}
        self.images['atm_enterpin'] = ImageTk.PhotoImage(Image.open("images/atm_enterpin.png").resize((1920, 1000)))
        self.images['atm_mainmenu'] = ImageTk.PhotoImage(Image.open("images/atm_mainmenu.png").resize((1920, 1000)))
        self.images['atm_enteramount'] = ImageTk.PhotoImage(Image.open("images/atm_enteramount.png").resize((1920, 1000)))
        self.images['atm_buttons'] = ImageTk.PhotoImage(Image.open("images/atm_buttons.png").resize((50, 50)))
        self.images['pin_enter'] = ImageTk.PhotoImage(Image.open("images/pin_enter.png").resize((208, 125)))
        self.images['atm_checkbalance'] = ImageTk.PhotoImage(Image.open("images/atm_checkbalance.png").resize((1920, 1000)))
        self.images['atm_changepin'] = ImageTk.PhotoImage(Image.open("images/atm_changepin.png").resize((1920, 1000)))
        self.images['back_button'] = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.num_buttons = [
            ImageTk.PhotoImage(Image.open(f"images/pin_{i}.png").resize((135, 125))) for i in range(10)
        ]
        for i, img in enumerate(self.num_buttons):
            self.images[f'num_button_{i}'] = img

    def enter(self, event):
        self.canvas.config(cursor="hand2")

    def leave(self, event):
        self.canvas.config(cursor="")

    def deposit(self, event=None):
        self.enter_amount_page("deposit")

    def withdraw(self, event=None):
        self.enter_amount_page("withdraw")

    def check_balance(self, event=None):
        system = BankSystem()
        amount = None
        action = "check balance"
        system.atm_transactions(self.user, action, amount)

    def change_pin(self, event=None):
        self.change_pin_page("change_pin")

    def set_active_field(self, field_name):
        self.active_field = field_name

    def reset_active_field(self, event):
        self.active_field = None

    def change_pin_page(self, action):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.images['atm_changepin'], anchor=ctk.NW)

        self.entry_old_pin = ctk.CTkEntry(master=self,placeholder_text="Enter old PIN here", bg_color="white", fg_color="white", border_color="white", width=380, height=33, font=("Poppins", 24, "bold"), text_color="#8B3C1D", justify='center')
        self.entry_old_pin.place(x=204, y=324, anchor=ctk.NW)
        self.entry_old_pin.bind("<FocusIn>", lambda event: self.set_active_field("new_pin"))
        self.entry_old_pin.bind("<FocusOut>", self.reset_active_field)

        self.entry_new_pin = ctk.CTkEntry(master=self,placeholder_text="Enter new PIN here", bg_color="white", fg_color="white", border_color="white", width=380, height=33, font=("Poppins", 24, "bold"), text_color="#8B3C1D", justify='center')
        self.entry_new_pin.place(x=204, y=458, anchor=ctk.NW)
        self.entry_new_pin.bind("<FocusIn>", lambda event: self.set_active_field("old_pin"))
        self.entry_new_pin.bind("<FocusOut>", self.reset_active_field)

        self.parent.bind("<Return>", self.enter_change_pin)

        self.active_field = None

        button_positions = [
            (1176, 661), (1009, 223), (1176, 223),
            (1343, 223), (1009, 369), (1176, 369),
            (1343, 369), (1009, 515), (1176, 515),
            (1343, 515)
        ]

        for i, pos in enumerate(button_positions):
            button = self.canvas.create_image(pos[0], pos[1], image=self.images[f'num_button_{i}'], anchor=ctk.NW, tag=f"{self.tagname}{i}")
            self.canvas.tag_bind(f"{self.tagname}{i}", "<Button-1>", lambda event, num=i: self.enter_change_pin(event, num))
            self.canvas.tag_bind(f"{self.tagname}{i}", "<Enter>", self.enter)
            self.canvas.tag_bind(f"{self.tagname}{i}", "<Leave>", self.leave)

        enter_button = self.canvas.create_image(1508, 515, image=self.images['pin_enter'], anchor=ctk.NW)
        self.canvas.tag_bind(enter_button, "<Button-1>", self.enter_pin)

        self.canvas.create_image(1508, 515, image=self.images['pin_enter'], anchor=ctk.NW, tag=f"{self.tagname}_enter")
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Button-1>", self.handle_enter_change_pin_button)
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Enter>", self.enter)
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Leave>", self.leave)

        self.canvas.create_image(20, 10, image=self.images['back_button'], anchor=ctk.NW, tag=f"{self.tagname}_back")
        self.canvas.tag_bind(f"{self.tagname}_back", "<Button-1>", lambda event: back_to_previous_page())
        self.canvas.tag_bind(f"{self.tagname}_back", "<Enter>", self.enter)
        self.canvas.tag_bind(f"{self.tagname}_back", "<Leave>", self.leave)

        self.parent.bind("<Return>", lambda event: self.handle_enter_change_pin_button(action))

        self.canvas.update()

        def back_to_previous_page():
            self.entry_new_pin.place_forget()
            self.entry_old_pin.place_forget()
            self.atm_main_page()

    def set_active_field(self, field_name):
        self.active_field = field_name

    def enter_change_pin(self, event, num):
        if self.active_field == "old_pin" and self.entry_new_pin:
            current_value = self.entry_new_pin.get()
            new_value = current_value + str(num)
            self.entry_new_pin.delete(0, 'end')
            self.entry_new_pin.insert(0, new_value)
        elif self.active_field == "new_pin" and self.entry_old_pin:
            current_value = self.entry_old_pin.get()
            new_value = current_value + str(num)
            self.entry_old_pin.delete(0, 'end')
            self.entry_old_pin.insert(0, new_value)

    def handle_enter_change_pin_button(self, event=None):
        old_pin = self.entry_old_pin.get()
        new_pin = self.entry_new_pin.get()
        system = BankSystem()
        system.atm_change_pin(self.user, old_pin, new_pin)
        self.atm_main_page()
        self.entry_new_pin.place_forget()
        self.entry_old_pin.place_forget()

    def enter_amount_page(self, action):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.images['atm_enteramount'], anchor=ctk.NW)

        button_positions = [
            (1176, 661), (1009, 223), (1176, 223),
            (1343, 223), (1009, 369), (1176, 369),
            (1343, 369), (1009, 515), (1176, 515),
            (1343, 515)
        ]

        for i, pos in enumerate(button_positions):
            button = self.canvas.create_image(pos[0], pos[1], image=self.images[f'num_button_{i}'], anchor=ctk.NW, tag=f"{self.tagname}{i}")
            self.canvas.tag_bind(f"{self.tagname}{i}", "<Button-1>", lambda event, num=i: self.enter_amount(event, num))
            self.canvas.tag_bind(f"{self.tagname}{i}", "<Enter>", self.enter)
            self.canvas.tag_bind(f"{self.tagname}{i}", "<Leave>", self.leave)

        self.canvas.create_image(20, 10, image=self.images['back_button'], anchor=ctk.NW, tag=f"{self.tagname}_back")
        self.canvas.tag_bind(f"{self.tagname}_back", "<Button-1>", lambda event: back_to_previous_page())
        self.canvas.tag_bind(f"{self.tagname}_back", "<Enter>", self.enter)
        self.canvas.tag_bind(f"{self.tagname}_back", "<Leave>", self.leave)

        self.entry_field = ctk.CTkEntry(master=self,placeholder_text="₱ 0.00", bg_color="white", fg_color="white", border_color="white", width=380, height=33, font=("Poppins", 24, "bold"), text_color="#8B3C1D", justify='center')
        self.entry_field.place(x=204, y=410, anchor=ctk.NW)

        self.canvas.create_image(1508, 515, image=self.images['pin_enter'], anchor=ctk.NW, tag=f"{self.tagname}_enter")
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Button-1>", lambda event: self.handle_enter_amount_button(action))
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Enter>", self.enter)
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Leave>", self.leave)

        self.parent.bind("<Return>", lambda event: self.handle_enter_amount_button(action))

        self.canvas.update()

        def back_to_previous_page():
            self.entry_field.place_forget()
            self.atm_main_page()

    def enter_amount(self, event, num):
        if self.entry_field:
            current_value = self.entry_field.get()
            new_value = current_value + str(num)
            self.entry_field.delete(0, 'end')
            self.entry_field.insert(0, new_value)

    def handle_enter_amount_button(self, action):
        amount = int(self.entry_field.get())
        system = BankSystem()
        if action == "withdraw":
            system.atm_transactions(self.user, action, amount)
            self.entry_field.delete(0,'end')
        if action == "deposit":
            system.atm_transactions(self.user, action, amount)
            self.entry_field.delete(0,'end')

    def enter_pin_page(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.images['atm_enterpin'], anchor=ctk.NW)

        self.entry_field = ctk.CTkEntry(master=self,placeholder_text="Enter PIN here", bg_color="white", fg_color="white", border_color="white", width=380, height=33, font=("Poppins", 24, "bold"), text_color="#8B3C1D", justify='center')
        self.entry_field.place(x=204, y=410, anchor=ctk.NW)
        self.parent.bind("<Return>", self.enter_pin)

        button_positions = [
            (1176, 661), (1009, 223), (1176, 223),
            (1343, 223), (1009, 369), (1176, 369),
            (1343, 369), (1009, 515), (1176, 515),
            (1343, 515)
        ]

        for i, pos in enumerate(button_positions):
            button = self.canvas.create_image(pos[0], pos[1], image=self.images[f'num_button_{i}'], anchor=ctk.NW, tag=f"{self.tagname}{i}")
            self.canvas.tag_bind(f"{self.tagname}{i}", "<Button-1>", lambda event, num=i: self.enter_pin(event, num))
            self.canvas.tag_bind(f"{self.tagname}{i}", "<Enter>", self.enter)
            self.canvas.tag_bind(f"{self.tagname}{i}", "<Leave>", self.leave)

        enter_button = self.canvas.create_image(1508, 515, image=self.images['pin_enter'], anchor=ctk.NW)
        self.canvas.tag_bind(enter_button, "<Button-1>", self.enter_pin)

        self.canvas.create_image(1508, 515, image=self.images['pin_enter'], anchor=ctk.NW, tag=f"{self.tagname}_enter")
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Button-1>", lambda event: self.handle_enter_pin())
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Enter>", self.enter)
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Leave>", self.leave)

        back_button = self.canvas.create_image(20, 10, image=self.images['back_button'], anchor=ctk.NW)
        self.canvas.tag_bind(back_button, "<Button-1>", self.back_to_previous_page)
        self.canvas.tag_bind(back_button, "<Enter>", self.enter)
        self.canvas.tag_bind(back_button, "<Leave>", self.leave)

        self.parent.bind("<Return>", self.handle_enter_pin)

        self.canvas.update()

    def enter_pin(self, event, num):
        if self.entry_field:
            current_value = self.entry_field.get()
            new_value = current_value + str(num)
            self.entry_field.delete(0, 'end')
            self.entry_field.insert(0, new_value)

    def handle_enter_pin(self, event=None):
        entered_pin = self.entry_field.get()
        if len(entered_pin) == 4:
            system = BankSystem()
            authenticated = system.atm_check_pin(self.user, entered_pin)
            if authenticated == "Success":
                CTkMessagebox(master=self, title="Success", message="Welcome to Bank City ATM Services", icon="check", sound=True)
                self.entry_field.place_forget()
                self.atm_main_page()
                return
            elif authenticated == "Failed":
                self.entry_field.place_forget()
                self.destroy()
                previous_page = ManagerPage(self.parent, self.user)
                previous_page.pack(fill=ctk.BOTH, expand=True)
            else:
                self.entry_field.delete(0,'end')
        else:
            CTkMessagebox(master=self, title="Error!", message="Invalid PIN input", icon="cancel", sound=True)
            self.entry_field.delete(0,'end')

    def atm_main_page(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.images['atm_mainmenu'], anchor=ctk.NW)

        button_positions = [(485, 420), (485, 500), (1385, 420), (1385, 500)]
        actions = [self.deposit, self.withdraw, self.check_balance, self.change_pin]

        for i, pos in enumerate(button_positions):
            tag = f"{self.tagname}{i}"
            self.canvas.create_image(pos[0], pos[1], image=self.images['atm_buttons'], anchor=ctk.NW, tag=tag)
            self.canvas.tag_bind(tag, "<Button-1>", actions[i])
            self.canvas.tag_bind(tag, "<Enter>", self.enter)
            self.canvas.tag_bind(tag, "<Leave>", self.leave)

        self.canvas.create_image(20, 10, image=self.images['back_button'], anchor=ctk.NW, tag=f"{self.tagname}_back")
        self.canvas.tag_bind(f"{self.tagname}_back", "<Button-1>", self.back_to_previous_page)
        self.canvas.tag_bind(f"{self.tagname}_back", "<Enter>", self.enter)
        self.canvas.tag_bind(f"{self.tagname}_back", "<Leave>", self.leave)

    def back_to_previous_page(self, event):
        self.destroy()
        previous_page = ManagerPage(self.parent, self.user)
        previous_page.pack(fill=ctk.BOTH, expand=True)