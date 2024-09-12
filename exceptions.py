class BankingException(Exception):
    pass

class InsufficientFundsException(BankingExcpetion):
    def __str__(self):
        return 'An error occurred: Insufficent Funds'

class InvalidAccountNumberException(BankingExcpetion):
    def __str__(self):
        return "An error occurred: Invalid Account Number"
