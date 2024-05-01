from calendar import calendar
import calendar
import datetime


class Expense:  # Defining a class named Expense to represent individual expenses.

    def __init__(self, name, category, amount) -> None:  # Constructor method to initialize an Expense object.
        self.name = name  # Assigning the provided 'name' parameter to the 'name' attribute of the Expense object.
        self.category = category  # Assigning the provided 'category' parameter to the 'category' attribute of the Expense object.
        self.amount = amount  # Assigning the provided 'amount' parameter to the 'amount' attribute of the Expense object.

    def __repr__(self):  # Special method to provide a string representation of the Expense object.
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

def summarize_expenses(expense_file_path, budget):  # Defining a function to summarize expenses.
    print(f"Summarizing user Expense")  # Printing a message indicating the start of summarizing expenses.
    expenses: list[Expense] = []  # Creating an empty list to store expenses.
    with open(expense_file_path, "r") as f:  # Opening the expense file in read mode.
        lines = f.readlines()  # Reading all lines from the file.
        for line in lines:  # Iterating through each line in the file.
            stripped_line = line.strip()  # Removing leading/trailing whitespaces from the line.
            expense_name, expense_category, expense_amount = line.strip().split(",")  # Splitting the line to get expense details.
            print(expense_name, expense_category, expense_amount)  # Printing expense details.
            line_expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))  # Creating an Expense object.
            expenses.append(line_expense)  # Appending the expense object to the list of expenses.

    amount_by_category = {}  # Creating a dictionary to store expenses by category.
    for expense in expenses:  # Iterating through each expense.
        key = expense.category  # Extracting the category of the expense.
        if key in amount_by_category:  # Checking if the category exists in the dictionary.
            amount_by_category[key] += expense.amount  # Adding the expense amount to the existing category total.
        else:
            amount_by_category[key] = expense.amount  # Creating a new category with the expense amount.

    print("Expenses by category")  # Printing a header for the expenses by category section.
    for key, amount in amount_by_category.items():  # Iterating through each category and its total amount.
        print(f"{key}: ₹{amount:.2f}")  # Printing category and its total amount.

    total_spent = sum([x.amount for x in expenses])  # Calculating the total amount spent by summing all expense amounts.
    print(f"you've spent ₹({total_spent:.2f}) this month!")  # Printing the total amount spent.

    remaining_budget = budget - total_spent  # Calculating the remaining budget.
    print(f"budget remaining: ₹{remaining_budget:.2f}")  # Printing the remaining budget.

    now = datetime.datetime.now()  # Getting the current date and time.
    days_in_month = calendar.monthrange(now.year, now.month)[1]  # Getting the number of days in the current month.
    remaining_days = days_in_month - now.day  # Calculating the remaining days in the current month.

    print("Remaining days in the current month:", remaining_days)  # Printing the remaining days in the current month.

    if remaining_days == 0:  # Checking if it's the last day of the month.
        print(f"daily budget == {remaining_budget}")  # Printing the daily budget.
    else:
        daily_budget = remaining_budget / remaining_days  # Calculating the daily budget.
        print(f"Budget per day: {daily_budget:.2f}")  # Printing the daily budget.

if __name__ == "__main__":  # Checking if the script is being run directly.
    main()  # Calling the main function.
