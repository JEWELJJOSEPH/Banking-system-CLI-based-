class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, intialAmount, accName):
        self.balance = intialAmount
        self.name = accName
        print(f"\n Account '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\n Account '{self.name}' balance = '{self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getBalance()

    def vaiable_trans(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:2f}"
            )

    def withdraw(self, amount):
        try:
            self.vaiable_trans(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer..")
            self.vaiable_trans(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete!")
        except BalanceException as error:
            print(f"\nTransfer Interrupted.{error}")


class InterestRewardAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\n Deposit Complete.")
        self.getBalance()


class SavingsAcc(BankAccount):
    def __init__(self, intialAmount, accName):
        super().__init__(intialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.vaiable_trans(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\n withdraw Interrupted:{error}")


class SibilScore(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1)
        print("\nRecieved 1% of your deposit as reward")
        self.getBalance()
