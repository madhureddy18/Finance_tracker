from tracker.tracker import Tracker
# from tracker.transaction import Transaction

def main():
    tracker=Tracker()
    while True:
        print("\n--- Finance Tracker ---")
        print("1. Add Transaction")
        print("2. View Financial Report")
        print("3. Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            amount=float(input("Enter your amount : "))
            type=input("Enter your type (income or expense) : ")
            category=input("Enter your category : ")
            tracker.add_transaction(amount,type,category)
        elif choice == 2:
            tracker.show_report()
        elif choice == 3:
            print("Goodbye")
        else:
            print("Invalid Choice. Please try again ")
if __name__=="__main__":
    main()

    
    


