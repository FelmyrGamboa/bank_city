
from teller_processes import TellerProcesses
from CTkMessagebox import CTkMessagebox

class CustomerProccesses():

    @staticmethod
    def request_lock_or_unlock(customer):
            if customer.bank_account:
                if customer.bank_account.status == "Active":
                    CTkMessagebox(title="Lock Request Successful", message="Your request to lock your account has been forwarded to Bank Teller.", icon="check", sound=True)
                    customer.update_lock_request_status("Requested")

                elif customer.bank_account.status == "Locked":
                    CTkMessagebox(title="Unlock Request Successful", message="Your request to unlock your account has been forwarded to Bank Teller.", icon="check", sound=True)
                    customer.update_unlock_request_status("Requested")
            else:
                CTkMessagebox(title="Lock/Unlock Request Failed", message="You cannot utilize this option without a bank account.", icon="cancel", sound=True)

    @staticmethod
    def check_account_request_status(customer):
        if customer.check_request_account_status == "Approved":
            customer.display_account_details()
        elif customer.check_request_account_status == "Pending":
            CTkMessagebox(title="Account Request Status: Pending", message="Kindly wait for the Bank Teller to process your accont request", icon="info", sound=True)
        elif customer.check_request_account_status == "Processed":
            CTkMessagebox(title="Account Request Status: Processed", message="Kindly wait for the Bank Manager to approve your accont request", icon="info", sound=True)
        else:
            CTkMessagebox(title="No Pending Account Request", message="You may click the 'Request Account' button if you wish to apply for a bank account.", icon="info", sound=True)

    @staticmethod
    def check_loan_application_status(customer):
            if customer.loan_status == "Pending":
                CTkMessagebox(title="Loan Application Status: Pending", message="Kindly wait for Manager's approval.", icon="info", sound=True)
            elif customer.loan_status == "Denied":
                CTkMessagebox(title="Loan Application Status: Denied", message="You may try applying for a lower amount", icon="cancel", sound=True)
            elif customer.loan_status == "Approved":
                CTkMessagebox(title="Loan Application Status: Approved", message=f"Congratulations!Approved loan amount: {customer.requested_loan_amount}", icon="check", sound=True)
            else:
               CTkMessagebox(title="No Existing Loan Application", message="You may click the 'Request a Loan' button if you wish to apply for one.", icon="info", sound=True)
