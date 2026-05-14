expenses = []


def show_menu():
    print()
    print("Expense Tracker")
    print("1. Add expense")
    print("2. List expenses")
    print("3. Show total")
    print("4. Quit")


def add_expense():
    name = input("Expense name: ")
    amount_text = input("Amount: ")

    try:
        amount = float(amount_text)
    except ValueError:
        print("That amount was not a number.")
        return

    expenses.append({"name": name, "amount": amount})
    print(f"Added {name}: ${amount:.2f}")


def list_expenses():
    if not expenses:
        print("No expenses yet.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']} - ${expense['amount']:.2f}")


def calculate_total():
    return sum(expense["amount"] for expense in expenses)


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            print(f"Total: ${calculate_total():.2f}")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

