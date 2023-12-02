# Banking System

[![License](https://img.shields.io/npm/l/react)](https://github.com/JadesonBruno/banking_sytem/blob/main/LICENSE)

## About the Project

This project consists of a simple bank account management system developed in Python. The code offers basic functionalities such as deposit, withdrawal, statement display, user creation, and account creation. The program uses a modular approach, dividing functions into distinct logical blocks to make the code easier to understand and maintain.

The project was a prerequisite for approval in the "Mastering Python for Data Science" module of the "Bootcamp Power Tech powered by [Ifood](https://www.ifood.com.br/) | Data Science" from the educational institution [DIO](https://www.dio.me/).

## Code Overview:

Here are the main components of the code:

1. `menu()` function:
   
- The `menu()` function displays an interactive menu for the user, allowing the selection of various operations, such as deposit, withdrawal, statement display, user creation, account creation and exiting the program. User input is validated to ensure valid choices.

2. `Deposit(balance, value, statement)` function:

- Responsible for making deposits into a bank account. Checks whether the deposit amount is valid and, if so, updates the balance and account statement.

3. Function `withdraw(balance, value, statement, limit, withdrawal_count, withdrawal_limit)`:
   
- Make withdrawals respecting balance limits, withdrawal limits and maximum number of withdrawals allowed. Provides detailed feedback in case of transaction failure.

4. `display_statement(balance, statement)` function:
   
- Displays the account statement, detailing all transactions carried out and the current balance.

5. `create_user(users)` function:

- Allows the creation of new users, collecting information such as CPF, name, date of birth and address. Checks if the user already exists to avoid duplicates.

6. `filter_user(cpf, users)` function:

- Filters users based on CPF, helping to verify the existence of a specific user.

7. `create_account(branch, account_number, users)` function:
   
- Creates new accounts associated with existing users, providing a relationship between users and bank accounts.

7. `create_account(branch, account_number, users) function`:

- Creates new accounts associated with existing users, providing a relationship between users and bank accounts.

8. `list_accounts(accounts)` function:
   
- Displays a list of all created accounts, including information such as branch, account number, and owner.

9. `main()` function:
    
- The main function `main()` starts executing the program, managing a continuous loop that allows the user to perform operations until they choose to exit the system.

## Technologies Used

- Python 3.10.9

## How to execute the project

To run the Python program, you need to have Python installed on your system. After installing the Python Environment, follow the steps below:

1. Open a terminal or command prompt.

2. Navigate to the directory where the file.py file is located. You can do this using the cd command in the terminal:

```bash
cd path/to/your/file/directory
```
3. Once you are in the correct directory, execute the Python script with the following command:

```bash
python file.py
```
or
```bash
python3 file.py
```
(The exact command depends on your environment and operating system. In some systems, you might need to use `python3` instead of `python`.)

4. The program will start, and you will see the interactive menu in the terminal, allowing you to choose different operations.

Please note that you need to have Python installed on your system. If you don't have Python installed, you can download it from [python.org](https://www.python.org/).

## Contributions

The system is a basic, modular implementation that can be extended and improved as needed. Contributions are welcome! Feel free to suggest improvements or corrections to the project.

## Author

Jadeson Bruno Albuquerque da Silva

[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jadeson-bruno-228450101/)


