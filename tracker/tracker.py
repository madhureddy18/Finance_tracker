from .transaction import Transaction
import os
class Tracker:
    def __init__(self,filepath="transaction.txt"):
        self.filepath=filepath
        self.transactions=self.load_transaction()
        
    def load_transaction(self):
        transactions=[]
        if os.path.exists(self.filepath):
            with open(self.filepath,"r") as file:
                for line in file:
                    transactions.append(Transaction.from_line(line))
        return transactions
    
    def save_transactions(self,transaction):
        with open(self.filepath,"a") as f:
            f.write(transaction.to_line())

    def add_transaction(self,amount,type,category):
        tx=Transaction(amount,type,category)
        self.transactions.append(tx)
        self.save_transactions(tx)
        print("Transaction Added")
        print(f"Total savings : {self.total_savings()}")

    def total_savings(self):
        return sum(i.get_amount() for i in self.transactions)

    def show_report(self):
        report = {}
        for tx in self.transactions:
            report[tx.category] = report.get(tx.category, 0) + tx.get_amount()
        
        print("Financial Report")
        for category,total in report.items():
            print(f"{category}:${total}")