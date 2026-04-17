import json
import matplotlib.pyplot as plt

transactions = []

# -------- ADD TRANSACTION --------
def add_transaction(person_name):
    date = input("Enter Date (YYYY-MM-DD): ")
    amount = float(input("Enter Amount: "))
    ttype = input("Type (credit/debit): ")
    merchant = input("Merchant: ")
    category = input("Category: ")

    transaction = {
        "name": person_name,
        "date": date,
        "amount": amount,
        "type": ttype,
        "merchant": merchant,
        "category": category
    }

    transactions.append(transaction)
    print("Transaction Added Successfully")

# -------- VIEW TRANSACTIONS --------
def view_transactions():
    if not transactions:
        print("No Transactions Found")
        return

    print("\n---- TRANSACTION LIST ----")
    for t in transactions:
        print(
            "Name:", t["name"],
            "| Date:", t["date"],
            "| Amount:", t["amount"],
            "| Type:", t["type"],
            "| Merchant:", t["merchant"],
            "| Category:", t["category"]
        )

# -------- TOTAL SPENDING --------
def total_spending():
    total = 0
    for t in transactions:
        if t["type"] == "debit":
            total += t["amount"]

    print("Total Spending:", total)

# -------- CATEGORY ANALYSIS --------
def category_analysis():
    summary = {}
    for t in transactions:
        if t["type"] == "debit":   # only expenses
            cat = t["category"]
            summary[cat] = summary.get(cat, 0) + t["amount"]
    return summary

# -------- SHOW GRAPH --------
def show_graph():
    summary = category_analysis()

    if not summary:
        print("No Data to Show")
        return

    labels = list(summary.keys())
    values = list(summary.values())

    plt.bar(labels, values)
    plt.title("Expense Graph")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

# -------- SAVE DATA --------
def save_data():
    with open("transactions.json", "w") as f:
        json.dump(transactions, f)
    print("Data Saved")

# -------- LOAD DATA --------
def load_data():
    global transactions
    try:
        with open("transactions.json", "r") as f:
            transactions = json.load(f)
    except FileNotFoundError:
        transactions = []

# -------- MAIN PROGRAM --------
def main():
    load_data()
    person_name = input("Enter Person Name: ")

    while True:
        print("\n===== SMART FINANCE MANAGER =====")
        print("1 Add Transaction")
        print("2 View Transactions")
        print("3 Total Spending")
        print("4 Show Graph")
        print("5 Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_transaction(person_name)

        elif choice == "2":
            view_transactions()

        elif choice == "3":
            total_spending()

        elif choice == "4":
            show_graph()

        elif choice == "5":
            save_data()
            print("Program Closed")
            break

        else:
            print("Invalid Choice")

# -------- RUN PROGRAM --------
main()
