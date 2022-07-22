class ATM:

    ########
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()

    def menu(self):  
        print("\n  ====== How , We can hepl you? ======")  
        print("""
            1) Create pin
            2) Depsoit Amount
            3) Withdraw Amount
            4) Balance Chck
            5) Exit 
        """)
        ch = int(input("Enter your choice: \n"))
        if ch == 1:
            self.create_pin()
        elif ch == 2:
            self.depost()
        elif ch == 3:
            self.withdraw()
        elif ch == 4:
            self.check_bala()
        else:
            print("Please choose right option")     

    #function create 
    def create_pin(self):
        self.pin = input("Create a pin \n")
        print("Pin created successfully")
        self.menu()

    def depost(self):
        temp = input("Enter your pin\n")
        if temp == self.pin:
            amount = int(input("Enter your amount \n"))
            self.balance = self.balance+amount
            print("Deposit successfully")
        else:
            print("Pin is wrong! Try again")    
        self.menu()

    def withdraw(self):
        temp = input("Enter your pin\n")
        if temp == self.pin:
            amount = int(input("Enter your amount \n"))     
            if amount <= self.balance: 
                self.balance=self.balance-amount
                print("Amount has withdraw")
            else:
                print("Balance is not Sufficent to withdraw!")
        else:
            print("Pin is wrong! Try again") 
        self.menu()        

    def check_bala(self):
        temp = input("Enter your pin\n")
        if temp == self.pin:
            print("Balance : ",self.balance)
        else:
            print("Pin is wrong! Try again")  
        self.menu()   

sbi  = ATM()            