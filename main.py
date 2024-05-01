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
def get_user_expense():  # Defining a function to get user's expense details.
    print(f"Getting User Expense")  # Printing a message indicating the start of getting user's expense.
    expense_name = input("Enter your Expense Name: ")  # Getting user input for expense name.
    expense_amount = float(input("Enter your Expense Amount: "))  # Getting user input for expense amount.
    expense_categories = ["Food", "Home", "Work", "Sport", "Fun", "misc"]  # Predefined expense categories.

    while True:  # Looping until valid input is received.
        print("select a category: ")  # Prompting user to select a category.
        for i, category_name in enumerate(expense_categories):  # Iterating through categories.
            print(f"{i+1}.{category_name}")  # Printing category options.
        value_range = f"[1-{len(expense_categories)}]"  # Determining the range of valid choices.

        selected_index = int(input(f"Enter a category number {value_range}:")) - 1  # Getting user's choice.

        if i in range(len(expense_categories)):  # Validating user's choice.
            selected_category = expense_categories[selected_index]  # Selecting the chosen category.
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)  # Creating a new Expense object.
            return new_expense  # Returning the created expense object.
        else:
            print("invalid choice. please try again")  # Informing the user about invalid input.

def save_expense_to_file(expense: Expense, expense_file_path):  # Defining a function to save an expense to a file.
    print(f"saving user Expense:{expense} to {expense_file_path}")  # Printing a message indicating saving expense details.
    with open(expense_file_path, "a") as f:  # Opening the file in append mode.
        f.write(f"{expense.name},{expense.category}, {expense.amount}\n")  # Writing expense details to the file.
