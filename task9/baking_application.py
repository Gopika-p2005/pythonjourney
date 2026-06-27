class BankAccount:

    def __init__(self,account_no,holder_name,balance):

        self.account_no=account_no

        self.holder_name=holder_name

        self.balance=balance

class SavingAccount(BankAccount):

    def __init__(self, account_no, holder_name, balance,interest_rate):

        super().__init__(account_no, holder_name, balance)

        self.interest_rate=interest_rate

    def display_savingaccount(self):

        print(self.account_no,self.holder_name,self.balance,self.interest_rate)

    def add_interest(self):

        total=self.balance+(self.balance*self.interest_rate/100)

        print("balance after interest",total)


SavingAccount_instance=SavingAccount(12345,"anju",10000,5)

SavingAccount_instance.display_savingaccount()

SavingAccount_instance.add_interest()
