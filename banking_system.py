import textwrap

# Function to display the menu and get user choice
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDeposit
    [w]\tWithdraw
    [s]\tStatement
    [na]\tNew account
    [la]\tList accounts
    [nu]\tNew user
    [q]\tQuit
    => """
    return input(textwrap.dedent(menu))

# Function to make a deposit
def deposit(balance, value, statement, /):
    if value > 0:
        balance += value
        statement += f"Deposit:\t$ {value:.2f}\n"
        print("\n=== Deposit successful! ===")
    else:
        print("\n@@@ Operation failed! The provided value is invalid. @@@")

    return balance, statement

# Function to make a withdrawal
def withdraw(*, balance, value, statement, limit, withdrawal_count, withdrawal_limit):
    exceeded_balance = value > balance   
    exceeded_limit = value > limit
    exceeded_withdrawals = withdrawal_count >= withdrawal_limit

    if exceeded_balance:
        print("\n@@@ Operation failed! You do not have sufficient balance. @@@")

    elif exceeded_limit:
        print("\n@@@ Operation failed! The withdrawal amount exceeds the limit. @@@")

    elif exceeded_withdrawals:
        print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")

    elif value > 0:
        balance -= value
        statement += f"Withdrawal:\t$ {value:.2f}\n"
        withdrawal_count += 1
        print("\n=== Withdrawal successful! ===")

    else:
        print("\n@@@ Operation failed! The provided value is invalid. @@@")

    return balance, statement, withdrawal_count

# Function to display the account statement
def display_statement(balance, /, *, statement):
    print("\n================ STATEMENT ================")
    print("No transactions have been made." if not statement else statement)
    print(f"\nBalance:\t$ {balance:.2f}")
    print("==========================================")

# Function to create a new user
def create_user(users):
    cpf = input("Enter the CPF (numbers only): ")
    user = filter_user(cpf, users)

    if user:
        print("\n@@@ User with this CPF already exists! @@@")
        return

    name = input("Enter the full name: ")
    birth_date = input("Enter the birth date (dd-mm-yyyy): ")
    address = input("Enter the address (street, number - neighborhood - city/state abbreviation): ")

    users.append({"name": name, "birth_date": birth_date,
                  "cpf": cpf, "address": address})

    print("=== User created successfully! ===")

# Function to filter a user by CPF
def filter_user(cpf, users):
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None

# Function to create a new account
def create_account(branch, account_number, users):
    cpf = input("Enter the user's CPF (numbers only): ")
    user = filter_user(cpf, users)

    if user:
        print("\n=== Account created successfully! ===")
        return {"branch": branch, "account_number": account_number, "user": user}

    print("\n@@@ User not found, account creation process terminated! @@@")

# Function to list all accounts
def list_accounts(accounts):
    for account in accounts:
        line = f"""\
            Branch:\t{account['branch']}
            A/C:\t\t{account['account_number']}
            Holder:\t{account['user']['name']}
        """
        print("=" * 100)
        print(textwrap.dedent(line))

# Main function
def main():
    WITHDRAWAL_LIMIT = 3
    BRANCH = "0001"

    balance = 0
    limit = 500
    statement = ""
    withdrawal_count = 0
    users = []
    accounts = []
    account_number = 1

    while True:
        option = menu()

        if option == "d":
            value = float(input("Enter the deposit amount: "))
            balance, statement = deposit(balance, value, statement)

        elif option == "w":
            value = float(input("Enter the withdrawal amount: "))
            balance, statement, withdrawal_count = withdraw(
                balance=balance,
                value=value,
                statement=statement,
                limit=limit,
                withdrawal_count=withdrawal_count,
                withdrawal_limit=WITHDRAWAL_LIMIT,
            )

        elif option == "s":
            display_statement(balance, statement=statement)

        elif option == "nu":
            create_user(users)

        elif option == "na":
            account = create_account(BRANCH, account_number, users)

            if account:
                accounts.append(account)
                account_number += 1

        elif option == "la":
            list_accounts(accounts)
            
        elif option == "q":
            break

        else:
            print("Invalid operation, please select the desired operation again.")

# Program execution
main()
