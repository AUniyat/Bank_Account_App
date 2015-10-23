__author__ = 'ALEX'
#A Bank Account App that has deposit, withdraw, and account creation functions
import BankAccountFiles  #importing the python file with some necessary functions

#The function that runs at the start of the program and asks what the user wishes to do
def start_bank_app():
   print "Welcome to Alex's Bank app, press 1 to create a new bank account"
   print  "or press 2 to access your existing account"
   starting_input = raw_input("> ")

   if starting_input=='1':
       customer=BankAccount()
   elif starting_input=='2':
       customer=returning_customer()
   else:
       print "your input was incorrect try again"
       start_bank_app()


#a class is made to direct the creation of the user account
class BankAccount():
    def __init__(self):
        self.username, self.balance=BankAccountFiles.check_customer() #account creation
        print "Thank you %s, your account is ready to use " % self.username
        print "$100 has been added to your account"
        self.user_choices() #the user choices function is called

    def user_choices(self): #a function that directs the user through the program
        print "choose the corresponding key to enter your choice"
        print """
        to check your balance press B.
        to make a deposit press D.
        to withdraw money press W.
        to delete your account press Z.
        to exit bank services press E.
        """
        user_input = raw_input("").lower()
        if user_input=='b':
            self.check_balance()
        elif user_input=='d':
            self.deposit_money()
        elif user_input=='w':
            self.withdraw_money()
        elif user_input=='z':
            print "Are you sure you want to delete your account? y/n"
            answer = raw_input("> ")
            if answer=='y':
                BankAccountFiles.delete_account(self.username)
                print "your account has been deleted"
            elif answer=="n":
                self.user_choices()
            else:
                print "Sorry your input was incorrect"
                self.user_choices()
        elif user_input=='e':
            print "goodbye"
            exit()
        else:
            print "Try again"
            self.user_choices()

    def check_balance(self): #a function that checks the balance of the user
        print "your account balance is {}".format(self.balance)
        self.continue_transaction()

    def withdraw_money(self): #a function that withdraws money from the user's account
        try:
            amount=float(raw_input("Please enter amount to be withdrawn :"))

        except:
            print "Please enter a number"
            self.user_choices()

        if amount > self.balance:
            print "you do not have sufficient funds"
            self.continue_transaction()
        self.balance -=amount
        print ("your new account balance is %.2f" % self.balance)
        BankAccountFiles.balance_update(self.username, self.balance)
        self.continue_transaction()

    def deposit_money(self): #a function that deposits money into the users account
        try:
            amount=float(raw_input(":Please enter amount to be deposited"))
        except:
            print "Please enter a number"
            self.user_choices()
        self.balance+=amount
        print ("your new account balance is %.2f" % self.balance)
        BankAccountFiles.balance_update(self.username, self.balance)
        self.continue_transaction()

    def continue_transaction(self): #a function that is called after the user is finished with each task
        input = raw_input("Do you want to continue using bank services? y/n").lower()
        if input == 'y':
            self.user_choices()
        elif input == 'n':
            print "Thank you for using our services"
            exit()
        else:
            self.continue_transaction()





class returning_customer(BankAccount): # a class is derives from the bank account class is called for returning customers
    def __init__(self):
        self.username, self.balance = BankAccountFiles.existing_customer()
        self.user_choices()


#some lines of codes I used to delete the 2 text files while experimenting
#open("C:\Users\ALEX\PycharmProjects\ITEC 2905 Assignment 2\Names.txt", 'w').close()
#open("C:\Users\ALEX\PycharmProjects\ITEC 2905 Assignment 2\Balance.txt", 'w').close()

start_bank_app() #the program starts running here

















