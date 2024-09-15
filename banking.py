import datetime
class Bank:
    def __init__(self):
        self.accounts={}
        self.operations=[]
    def create_account(self,account_id):
        if account_id in self.accounts:
            raise ValueError("account already exists")
        else:
            self.accounts[account_id]=account_id
            self.operations.append({
                'timestamp':datetime.datetime.now(),
                'operation':'create_account',
                'account_id':account_id            
                })
    
    def get_account(self, account_id):
        if account_id not in self.accounts:
            raise ValueError("account not found")
         
        self.operations.append({
                'timestamp': datetime.datetime.now(),
                'operation': 'get_account',
                'account_id': account_id
        })
        return self.accounts[account_id]

        
    def deposit(self, account_id, amount):
        try:
            account = self.get_account(account_id)
            print(type(account))
        except ValueError as e:
            # Account does not exist
            print(str(e))
            return None

        self.operations.append({
            'timestamp': datetime.datetime.now(),
            'operation': 'deposit',
            'account_id': account_id,
            'amount': amount,
        })

        # You may want to update the balance of the account here,
        # assuming the deposit method exists for the account object.
        # For this example, let's assume the deposit method exists.

    
    def withdraw(self,account_id,amount):
        account=self.get_account(account_id)
        if account:
            self.operations.append({
                'timestamp':datetime.datetime.now(),
                'operation':'withdraw',
                'account_id':account_id,
                'amount':amount,     
                })
   
   
    def get_operations(self):
        return self.operations