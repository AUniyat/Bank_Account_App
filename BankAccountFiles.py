__author__ = 'ALEX'
#this file holds the text file manipulation and account creation functions.
#as well as account manipulation and balance manipulation

#two lists are created to hold account names and user balance
AccountNames = []
AccountBalance = []

#the two text files are opened here
namefile = open("C:\Users\ALEX\PycharmProjects\ITEC 2905 Assignment 2\Names.txt", "r")
balancefile = open("C:\Users\ALEX\PycharmProjects\ITEC 2905 Assignment 2\Balance.txt", "r")

#here the saved user names and balance numbers are pulled
for line in namefile:
    AccountNames.append(line[:-1])
namefile.close()

for line in balancefile:
    AccountBalance.append(line[:-1])
balancefile.close()

def check_customer():  #the function that is called when creating a new account
    name = ""

    while name not in AccountNames:
        name=raw_input("Type in your name for this new bank account\n")
        if len(name) > 7:
            print "Sorry your username is too long"
            continue

        if name not in AccountNames and len(name) < 8:
            AccountNames.append(name)
            file_write(AccountNames)
            break

        print("Sorry, that user name is already in use")

    if len(name) < 8: #depositing an initial $100 into the account.
        AccountBalance.append(0)
        balance = 100.0
        AccountBalance[AccountNames.index(name)] = balance
        file_write(AccountBalance)

    return name, balance

def existing_customer(): #the function that is called when a returning customer logs in
    name = ""
    while name not in AccountNames:
        name = raw_input("Please enter your username :")
        if name in AccountNames:
            username = name
            balance = float(AccountBalance[AccountNames.index(name)])
            return username, balance
        else:
            print "Sorry it appears the name you entered is not registered"
            print "Would you like to enter another name?"
            try2 = raw_input("y/n")
            if try2.lower()=='y':
                existing_customer()
            else:
                print "Goodbye"
                exit()

def file_write(item): #a function that is called to write the user info into the text files
    if item == AccountNames:
        text = open("C:\Users\ALEX\PycharmProjects\ITEC 2905 Assignment 2\Names.txt", "w")
        for i in item:
            text.write(i+"\n")
        text.close()

    elif item == AccountBalance:
        text=open("C:\Users\ALEX\PycharmProjects\ITEC 2905 Assignment 2\Balance.txt", "w")
        for i in item:
            text.write(str(i)+"\n")
        text.close()

def balance_update(ind, amount): #a function that updates the user balance and links the name to the balance
    account_number = AccountNames.index(ind)
    accnt_balance = float(AccountBalance[account_number])
    accnt_balance = amount
    AccountBalance[account_number]=accnt_balance
    text=open("C:\Users\ALEX\PycharmProjects\ITEC 2905 Assignment 2\Balance.txt", "w")
    for i in AccountBalance:
        text.write(str(i) + "\n")
    text.close()

def delete_account(name): #a function that is called when the user wants to delete their account
    account_id = AccountNames.index(name)
    del AccountNames[account_id]
    file_write(AccountNames)
    del AccountBalance[account_id]
    file_write(AccountBalance)
    return None



