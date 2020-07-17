from SavingsAccount import SavingsAccount

savings_account = SavingsAccount()

while True:
    print()

    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")

    user_choice = int(input())

    print()

    if user_choice is 1:
        print()

        print("Enter your name: ")
        name = input()

        print("Enter the initial deposit: ")
        deposit = int(input())

        savings_account.create_account(name, deposit)
        print()

    elif user_choice is 2:
        print()

        print("Enter your name: ")
        name = input()

        print("Enter your account number: ")
        accountNumber = int(input())

        authentication_status = savings_account.authenticate(name, accountNumber)

        print()

        if authentication_status is True:

            while True:
                print()

                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display avialable balance")
                print("Enter 4 to go back to the previous menu")
                user_choice = int(input())

                print()

                if user_choice is 1:
                    print()

                    print("Enter a withdrawal amount")
                    withdrawalAmount = int(input())

                    savings_account.withdraw(withdrawalAmount)

                    print()

                elif user_choice is 2:
                    print()

                    print("Enter an amount to be deposited")
                    depositAmount = int(input())

                    savings_account.deposit(depositAmount)

                    print()

                elif user_choice is 3:
                    print()

                    savings_account.display_balance()

                    print()

                elif user_choice is 4:
                    break

    elif user_choice is 3:
        quit()
