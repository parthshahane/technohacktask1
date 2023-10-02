class ATM:
    def __init__(self, balance=1000):
        self.balance = balance
        self.transaction_history = []

    def display_balance(self):
        return f"Your account balance is ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. {self.display_balance()}"
        else:
            return "Invalid amount for deposit."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. {self.display_balance()}"
        else:
            return "Invalid amount for withdrawal or insufficient funds."

    def transfer(self, amount, target_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            self.transaction_history.append(f"Transferred ${amount} to another account")
            return f"Transferred ${amount} to the target account. {self.display_balance()}"
        else:
            return "Invalid amount for transfer or insufficient funds."

    def get_transaction_history(self):
        return "\n".join(self.transaction_history)


def main():
    atm = ATM()
    while True:
        print("\nATM Menu:")
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. View Transaction History")
        print("6. Quite")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            print(atm.display_balance())
        elif choice == '2':
            amount = float(input("Enter the deposit amount: $"))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter the withdrawal amount: $"))
            print(atm.withdraw(amount))
        elif choice == '4':
            amount = float(input("Enter the transfer amount: $"))
            target_account = ATM()  # Create a target account (for simplicity, you can enhance this part)
            print(atm.transfer(amount, target_account))
        elif choice == '5':
            print("Transaction History:")
            print(atm.get_transaction_history())
        elif choice == '6':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

