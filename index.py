import os
from message import Message
from interface import UserInterface
from user import User
from account import Account
from auth import Auth


def main():
    message = Message()
    ui = UserInterface()
    auth = Auth()
    
    #authenticate user
    login_attempts = 0
    failed_Attempt = False
    while login_attempts < 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        if failed_Attempt:
            message.print("please try again")
        message.print("Welcome to the bank of Py!")
        message.print("please login to continue.")

        userName = input("Username: ")
        password = input("password")

        user = auth.login(userName, password)
        if not user:
            login_attempts += 1
            failedAttempt = True
        else:
            break

        if not user:
        message.print("Too many failed attempts. Exiting...")
        return
    

    #register UI
    ui.register_command("deposit", user.deposit, "deposit [accountNumber] [amount] - deposit an amount into an account")
    ui.register_command("withdraw", user.withdraw, "withdraw [accountNumber] [amount] - withdraw an amount from an account")
    ui.register_command("transfer", user.transfer, " transfer [fromAccountNumber] [toAccountNumber] [amount] - transfer an amount from one account to another account")

    #Main Loop
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        message.print("What can we do for you today?")
        user.show_accounts()
        ui.show_commands()
        user_inputs = input().lower().split(" ")

        #exit check
        if(user_inputs[0] == "exit"):
            print("Goodbye")
            break

        if user_inputs:
            ui.execute_command(user_inputs[0], user_inputs[1:])
        



if __name__ == "__main__":
    main()
   

