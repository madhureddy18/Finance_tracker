class Transaction:
    def __init__(self,amount,type,category):
        self.amount=float(amount)
        self.type=type.lower()
        self.category=category
    def get_amount(self):
        if self.type=="income":
            return float(self.amount)
        else:
            return -float(self.amount)
        
    def to_line(self):
        return f"{self.amount},{self.type},{self.category}\n"
    
    @staticmethod
    def from_line(line):
        amount, type, category = line.strip().split(",")
        return Transaction(amount,type, category)
    
        