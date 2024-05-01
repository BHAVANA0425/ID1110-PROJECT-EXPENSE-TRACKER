from calendar import calendar
import calendar
import datetime


class Expense:  # Defining a class named Expense to represent individual expenses.

    def _init_(self, name, category, amount) -> None:  # Constructor method to initialize an Expense object.
        self.name = name  # Assigning the provided 'name' parameter to the 'name' attribute of the Expense object.
        self.category = category  # Assigning the provided 'category' parameter to the 'category' attribute of the Expense object.
        self.amount = amount  # Assigning the provided 'amount' parameter to the 'amount' attribute of the Expense object.

    def _repr_(self):  # Special method to provide a string representation of the Expense object.
        return f"<Expense: {self.name} {self.category} {self.amount:.2f} >"  # Returning a formatted string representing the Expense object with name, category, and amount.



def main():  # Defining the main function.
    print(f"Running Expense Tracker!")  # Printing a message indicating the start of the program.
    expense_file_path = "expenses.csv"  # Setting the file path for storing expenses.
    budget = int(input("Enter budget: "))  # Getting user input for the budget.

    # Function call to get user input for an expense.
    expense = get_user_expense()

    # Function call to save the user's expense to a file.
    save_expense_to_file(expense, expense_file_path)

    # Function call to read the file and summarize expenses.
    summarize_expenses(expense_file_path, budget)
