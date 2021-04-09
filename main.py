class Budget:
    def __init__(self, food,clothing,entertainment):
        self.food = food
        self.cloth = clothing
        self.enteri = entertainment


    def deposit(self):
        ask_deposit = int(input("which of you budget do you wish to deposit to ? \n(1) Food (2) Clothing (3) entertainment \n"))
        if ask_deposit == 1:
            amount_ask = int(input("how much do you want to deposit: \n"))
            self.food += amount_ask
            print(f"your new budget for food is: ₦{self.food}")
        elif ask_deposit == 2:
            amount_ask = int(input("how much do you want to deposit: \n"))
            self.cloth += amount_ask
            print(f"your new budget for food is: ₦{self.cloth}")
        elif ask_deposit == 3:
            amount_ask = int(input("how much do you want to deposit: \n"))
            self.enteri += amount_ask
            print(f"your new budget for food is: ₦{self.enteri}")

    
    def withdrawal(self):
        ask_deposit = int(input("which of you budget do you wish to withdraw from ? \n(1) Food (2) Clothing (3) entertainment \n"))
        if ask_deposit == 1:
            amount_ask = int(input("how much do you want to withdraw: \n"))
            self.food - amount_ask
            print(f"your new budget for food is: ₦{self.food}")
        elif ask_deposit == 2:
            amount_ask = int(input("how much do you want to withdraw: \n"))
            self.cloth - amount_ask
            print(f"your new budget for food is: ₦{self.cloth}")
        elif ask_deposit == 3:
            amount_ask = int(input("how much do you want to withdraw: \n"))
            self.enteri - amount_ask
            print(f"your new budget for food is: ₦{self.enteri}")
    
    def computing(self):
        print(f"Your budget balance are:  Food ₦({self.food}) | Clothing ₦({self.cloth}) | Entertainment ₦({self.enteri})")
    
    def transfer(self):
        print(f"You don't sufficient fund in your budget.Your budget are:  Food ₦({self.food}) | Clothing ₦({self.cloth}) | Entertainment ₦({self.enteri})")



my_budget = Budget(0,0,0)

bank = int(input("Welcome to zuri budgetvest. What do you want to do today? \n(1) Deposit | (2) withdrawal | (3) balance | (4) transfer \n"))
if bank == 1:
    my_budget.deposit()
elif bank == 2:
    my_budget.withdrawal()
elif bank == 3:
    my_budget.computing()
elif bank == 4:
    my_budget.transfer()
else:
    print("Invalid command!")

