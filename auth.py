import json
from user import User
from account import Account
from message import Message

message = Message()

class Auth:
    def __init__(self):
        pass

    def login_again(self, username, password):
        try:
            with open('db.json', 'r') as file:
                users = json.load(file)['users']
         except (FileNotFoundError, json.JSONDecodeError) as e:
            message.print(f"Error loading user data: {e}")
            return None
        
        for user in users:
            if user['name'] == username:
                if user['password'] == password:
                    accounts = {}
                    for account in user['accounts']:
                        accounts[account['accountNumber']] = Account(account['balance'])
                    return User(user['name'], accounts)
                else:
                    message.print("Invalid password")
                    retune None
          
        message.print("User not found")
        return None
