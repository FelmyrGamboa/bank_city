import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from bank_system import BankSystem
from bank_customer import BankCustomer
from bank_teller import BankTeller
from bank_manager import BankManager
from formatbirthdate import validate_and_format_birthdate
from PIL import ImageTk, Image

class CustomerPage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.customer_menu()

    def enter(self, event):
        self.canvas.config(cursor="hand2")

    def leave(self, event):
        self.canvas.config(cursor="")

    def customer_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.home_page_bg_img_tk = ImageTk.PhotoImage(Image.open("images/customermenu_bg.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.home_page_bg_img_tk, anchor=ctk.NW)

        self.use_atm_img_tk = ImageTk.PhotoImage(Image.open("images/customer_useatm.png"))
        self.transact_with_teller_img_tk = ImageTk.PhotoImage(Image.open("images/customer_transactwithteller.png"))

        self.use_atm_button = self.canvas.create_image(1020, 140, image=self.use_atm_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.transact_with_teller_button = self.canvas.create_image(300, 225, image=self.transact_with_teller_img_tk, anchor=ctk.NW, tag=self.tagname)

        self.canvas.tag_bind(self.use_atm_button, "<Button-1>", self.use_atm)
        self.canvas.tag_bind(self.transact_with_teller_button, "<Button-1>", self.transact_with_teller)

        self.customer_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.customer_back_button = self.canvas.create_image(20, 10, image=self.customer_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.customer_back_button, "<Button-1>", self.back)

        self.customer_menu_button_img_tk = ImageTk.PhotoImage(Image.open("images/customer_menu_button.png").resize((150, 150)))
        self.customer_menu_button = self.canvas.create_image(1750, 10, image=self.customer_menu_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.customer_menu_button, "<Button-1>", self.customer_requests)

        self.canvas.tag_bind(self.tagname, "<Enter>", self.enter)
        self.canvas.tag_bind(self.tagname, "<Leave>", self.leave)

    def customer_requests(self, event):
        self.destroy()
        customer_requests_page = CustomerRequests(self.parent, self.user)
        customer_requests_page.pack(fill=ctk.BOTH, expand=True)

    def transact_with_teller(self, event):
        system = BankSystem()
        check_account = system.check_account(self.user.username)
        if check_account:
            self.destroy()
            transact_with_teller_page = TransactWithTeller(self.parent, self.user)
            transact_with_teller_page.pack(fill=ctk.BOTH, expand=True)

    def use_atm(self, event):
        system = BankSystem()
        check_account = system.check_account(self.user.username)
        if check_account:
            self.destroy()
            atm_menu = ATMMenu(self.master, self.user, previous_page=self.master)
            atm_menu.pack(fill=ctk.BOTH, expand=True)

    def back(self, event):
        self.confirm_logout()

    def confirm_logout(self):
        response = CTkMessagebox(master=self, title="Logout", message="Are you sure you want to log out?", icon="question", option_1="Yes", option_2="No", sound=True)
        if response.get() == "Yes":
            self.destroy()
            self.parent.main_page()

class TransactWithTeller(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.transact_with_teller_menu()

    def enter(self, event):
        self.canvas.config(cursor="hand2")

    def leave(self, event):
        self.canvas.config(cursor="")

    def transact_with_teller_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.transact_with_teller_bg_img_tk = ImageTk.PhotoImage(Image.open("images/transact_with_teller.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.transact_with_teller_bg_img_tk, anchor=ctk.NW)

        self.customer_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.customer_back_button = self.canvas.create_image(20, 10, image=self.customer_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.customer_back_button, "<Button-1>", self.previous_page)

        self.deposit_button_img_tk = ImageTk.PhotoImage(Image.open("images/button.png").resize((75, 75)))
        self.deposit_button = self.canvas.create_image(480, 320, image=self.deposit_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.deposit_button, "<Button-1>", self.deposit)

        self.withdraw_button_img_tk = ImageTk.PhotoImage(Image.open("images/button.png").resize((75, 75)))
        self.withdraw_button = self.canvas.create_image(480, 510, image=self.withdraw_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.withdraw_button, "<Button-1>", self.withdraw)

        self.check_balance_button_img_tk = ImageTk.PhotoImage(Image.open("images/button.png").resize((75, 75)))
        self.check_balance_button = self.canvas.create_image(480, 700, image=self.check_balance_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.check_balance_button, "<Button-1>", self.check_balance)

        self.canvas.tag_bind(self.tagname, "<Enter>", self.enter)
        self.canvas.tag_bind(self.tagname, "<Leave>", self.leave)

    def previous_page(self, event):
        self.destroy()
        back_page = CustomerPage(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def deposit(self, event):
        self.destroy()
        back_page = Deposit(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def withdraw(self, event):
        self.destroy()
        back_page = Withdraw(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def check_balance(self, event):
        self.destroy()
        back_page = CheckBalance(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class Deposit (ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.deposit_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def deposit_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.deposit_page_img_tk = ImageTk.PhotoImage(Image.open("images/deposit.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.deposit_page_img_tk, anchor=ctk.NW)

        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((300, 120)))
        self.enter_button = self.canvas.create_image(820, 775, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", lambda event: self.deposit_transaction())

        self.deposit_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.deposit_back_button = self.canvas.create_image(20, 10, image=self.deposit_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.deposit_back_button, "<Button-1>", self.previous_page)

        self.amount_entry = ctk.CTkEntry(master=self,placeholder_text="₱ 0.00", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.birthday_entry = ctk.CTkEntry(master=self,placeholder_text="Format: Month Day, Year", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')

        self.amount_entry.place(x=787, y=342, anchor=ctk.CENTER)
        self.birthday_entry.place(x=787, y=527, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def previous_page(self, event):
        self.destroy()
        back_page = TransactWithTeller(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)
    
    def deposit_transaction(self):
        amount = self.amount_entry.get()
        birthday = self.birthday_entry.get()
        action = "Deposit"
        system = BankSystem()
        system.transact_with_telller(self.user, birthday, amount, action)
        self.amount_entry.delete(0, 'end')
        self.birthday_entry.delete(0, 'end')

class Withdraw (ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.withdraw_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def withdraw_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.withdraw_page_img_tk = ImageTk.PhotoImage(Image.open("images/withdraw.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.withdraw_page_img_tk, anchor=ctk.NW)

        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((300, 120)))
        self.enter_button = self.canvas.create_image(820, 775, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", lambda event: self.withdraw_transaction())

        self.withdraw_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.withdraw_back_button = self.canvas.create_image(20, 10, image=self.withdraw_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.withdraw_back_button, "<Button-1>", self.previous_page)

        self.amount_entry = ctk.CTkEntry(master=self,placeholder_text="₱ 0.00", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.birthday_entry = ctk.CTkEntry(master=self,placeholder_text="Format: Month Day, Year", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')

        self.amount_entry.place(x=787, y=342, anchor=ctk.CENTER)
        self.birthday_entry.place(x=787, y=527, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def withdraw_transaction(self):
        amount = self.amount_entry.get()
        birthday = self.birthday_entry.get()
        action = "Withdraw"
        system = BankSystem()
        system.transact_with_telller(self.user, birthday, amount, action)
        self.amount_entry.delete(0, 'end')
        self.birthday_entry.delete(0, 'end')
        
    def previous_page(self, event):
        self.destroy()
        back_page = TransactWithTeller(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class CheckBalance (ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.check_balance_menu()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def check_balance_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.check_balance_page_img_tk = ImageTk.PhotoImage(Image.open("images/check_balance.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.check_balance_page_img_tk, anchor=ctk.NW)

        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((300, 120)))
        self.enter_button = self.canvas.create_image(820, 775, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", lambda event: self.check_balance())

        self.check_balance_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.check_balance_button = self.canvas.create_image(20, 10, image=self.check_balance_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.check_balance_button, "<Button-1>", self.previous_page)

        self.amount_entry = ctk.CTkEntry(master=self,placeholder_text="Format: Month Day, Year", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.amount_entry.place(x=787, y=423, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())
    
    def check_balance(self):
        amount = None
        birthday = self.amount_entry.get()
        action = "Check Balance"
        system = BankSystem()
        system.transact_with_telller(self.user, birthday, amount, action)
        self.amount_entry.delete(0, 'end')
        self.birthday_entry.delete(0, 'end')

    def previous_page(self, event):
        self.destroy()
        back_page = TransactWithTeller(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

class CustomerRequests(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.customer_requests_menu()

    def enter(self, event):
        self.canvas.config(cursor="hand2")

    def leave(self, event):
        self.canvas.config(cursor="")

    def customer_requests_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.customer_requests_bg_img_tk = ImageTk.PhotoImage(Image.open("images/customer_requests.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.customer_requests_bg_img_tk, anchor=ctk.NW)

        self.customer_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.customer_back_button = self.canvas.create_image(20, 10, image=self.customer_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.customer_back_button, "<Button-1>", self.previous_page)

        self.manage_account_button_img_tk = ImageTk.PhotoImage(Image.open("images/button.png").resize((75, 75)))
        self.manage_account_button = self.canvas.create_image(480, 320, image=self.manage_account_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.manage_account_button, "<Button-1>", self.manage_account)

        self.apply_for_a_loan_button_img_tk = ImageTk.PhotoImage(Image.open("images/button.png").resize((75, 75)))
        self.apply_for_a_loan_button = self.canvas.create_image(480, 510, image=self.apply_for_a_loan_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.apply_for_a_loan_button, "<Button-1>", self.apply_for_a_loan)

        self.lock_unlock_button_img_tk = ImageTk.PhotoImage(Image.open("images/button.png").resize((75, 75)))
        self.lock_unlock_button = self.canvas.create_image(480, 700, image=self.lock_unlock_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.lock_unlock_button, "<Button-1>", self.lock_unlock)

        self.canvas.tag_bind(self.tagname, "<Enter>", self.enter)
        self.canvas.tag_bind(self.tagname, "<Leave>", self.leave)

    def previous_page(self, event):
        self.destroy()
        back_page = CustomerPage(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def manage_account(self, event):
        self.destroy()
        back_page = ManageAccount(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def apply_for_a_loan(self, event):
        system = BankSystem()
        check_account = system.check_account(self.user.username)
        if check_account:
            self.destroy()
            back_page = ApplyForALoan(self.parent, self.user)
            back_page.pack(fill=ctk.BOTH, expand=True)

    def lock_unlock(self, event):
        system = BankSystem()
        system.lock_or_unlock_account(self.user)

class ManageAccount (ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.manage_account_menu()

    def enter(self, event):
        self.canvas.config(cursor="hand2")

    def leave(self, event):
        self.canvas.config(cursor="")

    def manage_account_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.manage_account_bg_img_tk = ImageTk.PhotoImage(Image.open("images/manage_account.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.manage_account_bg_img_tk, anchor=ctk.NW)

        self.customer_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.customer_back_button = self.canvas.create_image(20, 10, image=self.customer_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.customer_back_button, "<Button-1>", self.previous_page)

        self.request_account_button_img_tk = ImageTk.PhotoImage(Image.open("images/button.png").resize((75, 75)))
        self.request_account_button = self.canvas.create_image(480, 392, image=self.request_account_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.request_account_button, "<Button-1>", self.request_acc)

        self.account_request_status_button_img_tk = ImageTk.PhotoImage(Image.open("images/button.png").resize((75, 75)))
        self.account_request_status_button = self.canvas.create_image(480, 590, image=self.account_request_status_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.account_request_status_button, "<Button-1>", self.account_req)

        self.canvas.tag_bind(self.tagname, "<Enter>", self.enter)
        self.canvas.tag_bind(self.tagname, "<Leave>", self.leave)

    def previous_page(self, event):
        self.destroy()
        back_page = CustomerRequests(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def request_acc(self, event):
        system = BankSystem()
        system.request_bank(self.user)

    def account_req(self, event):
        system = BankSystem()
        system.account_request_status(self.user)

class ApplyForALoan (ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.apply_for_a_loan_menu()

    def enter(self, event):
        self.canvas.config(cursor="hand2")

    def leave(self, event):
        self.canvas.config(cursor="")

    def apply_for_a_loan_menu(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.apply_for_a_loan_bg_img_tk = ImageTk.PhotoImage(Image.open("images/apply_for_a_loan.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.apply_for_a_loan_bg_img_tk, anchor=ctk.NW)

        self.customer_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.customer_back_button = self.canvas.create_image(20, 10, image=self.customer_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.customer_back_button, "<Button-1>", self.previous_page)

        self.request_loan_button_img_tk = ImageTk.PhotoImage(Image.open("images/button.png").resize((75, 75)))
        self.request_loan_button = self.canvas.create_image(480, 392, image=self.request_loan_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.request_loan_button, "<Button-1>", self.request_loan)
        self.canvas.tag_bind(self.request_loan_button, "<Enter>", self.enter)
        self.canvas.tag_bind(self.request_loan_button, "<Leave>", self.leave)

        self.loan_application_status_button_img_tk = ImageTk.PhotoImage(Image.open("images/button.png").resize((75, 75)))
        self.loan_application_status_button = self.canvas.create_image(480, 590, image=self.loan_application_status_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.loan_application_status_button, "<Button-1>", self.loan_application)
        self.canvas.tag_bind(self.loan_application_status_button, "<Enter>", self.enter)
        self.canvas.tag_bind(self.loan_application_status_button, "<Leave>", self.leave)

    def previous_page(self, event):
        self.destroy()
        back_page = CustomerRequests(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def request_loan(self, event):
        self.destroy()
        back_page = RequestLoan(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def loan_application(self, event):
        system = BankSystem()
        system.loan_application_status(self.user)

class RequestLoan(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.request_loan_amount()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def request_loan_amount(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.request_loan_page_img_tk = ImageTk.PhotoImage(Image.open("images/enter_loan_amount.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.request_loan_page_img_tk, anchor=ctk.NW)

        self.enter_button_img_tk = ImageTk.PhotoImage(Image.open("images/enter_button.png").resize((300, 120)))
        self.enter_button = self.canvas.create_image(820, 775, image=self.enter_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.enter_button, "<Button-1>", self.enter_loan)

        self.request_loan_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((190, 170)))
        self.request_loan_button = self.canvas.create_image(20, 10, image=self.request_loan_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.request_loan_button, "<Button-1>", self.previous_page)

        self.amount_entry =  ctk.CTkEntry(master=self,  placeholder_text= "₱ 0.00",bg_color="white", fg_color="white", border_color="white", width=390, height=45, font=("Poppins", 20, "bold"), text_color="#8B3C1D", justify='center')
        self.amount_entry.place(x=787, y=423, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def previous_page(self, event):
        self.destroy()
        back_page = ApplyForALoan(self.parent, self.user)
        back_page.pack(fill=ctk.BOTH, expand=True)

    def enter_loan(self, event):
        system = BankSystem()
        amount = self.amount_entry.get()
        system.entered_loan_for_request(self.user, amount)
        self.amount_entry.delete(0, 'end')

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

        self.canvas.create_image(1508, 515, image=self.images['pin_enter'], anchor=ctk.NW, tag=f"{self.tagname}_enter")
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Button-1>", self.handle_enter_change_pin_button)
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Enter>", self.enter)
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Leave>", self.leave)

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

        self.canvas.create_image(20, 10, image=self.images['back_button'], anchor=ctk.NW, tag=f"{self.tagname}_back")
        self.canvas.tag_bind(f"{self.tagname}_back", "<Button-1>", lambda event: back_to_previous_page())
        self.canvas.tag_bind(f"{self.tagname}_back", "<Enter>", self.enter)
        self.canvas.tag_bind(f"{self.tagname}_back", "<Leave>", self.leave)

        self.entry_old_pin = ctk.CTkEntry(master=self,placeholder_text="Enter old PIN here", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.entry_old_pin.place(x=204, y=324, anchor=ctk.NW)
        self.entry_old_pin.bind("<FocusIn>", lambda event: self.set_active_field("new_pin"))
        self.entry_old_pin.bind("<FocusOut>", self.reset_active_field)

        self.entry_new_pin = ctk.CTkEntry(master=self,placeholder_text="Enter new PIN here", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.entry_new_pin.place(x=204, y=458, anchor=ctk.NW)
        self.entry_new_pin.bind("<FocusIn>", lambda event: self.set_active_field("old_pin"))
        self.entry_new_pin.bind("<FocusOut>", self.reset_active_field)

        self.active_field = None
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

        self.entry_field = ctk.CTkEntry(master=self,placeholder_text="₱ 0.00", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.entry_field.place(x=204, y=410, anchor=ctk.NW)

        self.canvas.create_image(1508, 515, image=self.images['pin_enter'], anchor=ctk.NW, tag=f"{self.tagname}_enter")
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Button-1>", lambda event: self.handle_enter_amount_button(action))
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Enter>", self.enter)
        self.canvas.tag_bind(f"{self.tagname}_enter", "<Leave>", self.leave)

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

    def handle_enter_change_pin_button(self, event):
        x, y = event.x, event.y
        widget = self.canvas.find_closest(x, y)
        tags = self.canvas.gettags(widget)
        if tags and tags[0].endswith("_enter"):
            old_pin = self.entry_old_pin.get()
            new_pin = self.entry_new_pin.get()
            system = BankSystem()
            system.atm_change_pin(self.user, old_pin, new_pin)
            self.atm_main_page()
            self.entry_new_pin.place_forget()
            self.entry_old_pin.place_forget()
    
    def handle_enter_amount_button(self, action):
        amount = int(self.entry_field.get())
        system = BankSystem()
        if action == "withdraw":
            system.atm_transactions(self.user,action, amount)
            self.entry_field.delete(0,'end')
        if action == "deposit":
            system.atm_transactions(self.user,action, amount)
            self.entry_field.delete(0,'end')

    def enter_pin_page(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.images['atm_enterpin'], anchor=ctk.NW)

        self.entry_field = ctk.CTkEntry(master=self,placeholder_text="Enter PIN here", bg_color="white", fg_color="white", border_color="white", width=430, height=67, font=("Poppins", 30, "bold"), text_color="#8B3C1D", justify='center')
        self.entry_field.place(x=204, y=410, anchor=ctk.NW)

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

        self.canvas.update()

    def enter_pin(self, event, num):
        if self.entry_field:
            current_value = self.entry_field.get()
            new_value = current_value + str(num)
            self.entry_field.delete(0, 'end')
            self.entry_field.insert(0, new_value)

    def handle_enter_pin(self):
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
                previous_page = CustomerPage(self.parent, self.user)
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
        previous_page = CustomerPage(self.parent, self.user)
        previous_page.pack(fill=ctk.BOTH, expand=True)

