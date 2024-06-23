from test import *

acc1 = BankAccount(100000, "Jewel")
acc2 = BankAccount(2000, "Angel")

acc1.getBalance()
acc2.getBalance()


acc1.transfer(2000, acc2)

juhi = InterestRewardAcc(1000,"juhi")
juhi.getBalance()
juhi.deposit(100)

jackie = SavingsAcc(2000,"jackie")
jackie.getBalance()
jackie.deposit(34500)