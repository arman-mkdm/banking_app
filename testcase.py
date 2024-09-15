from banking import Bank
def run_single_test(name):
    bank=Bank()
    try:
        if name=='create_account':
            bank.create_account("account1")
            print("acc created successfully")
            print("Operations")
            print(bank.get_operations())
        elif name=='deposit':
            bank.create_account("account2")
            bank.deposit("account2",100)
            print("deposited successfully")
            print("Operations")
            print(bank.get_operations())
        elif name=="withdraw":
            bank.create_account("account2")
            bank.deposit("account2",100)
            bank.withdraw("account2",50)
            print("Operations")
            print(bank.get_operations())
        elif name=='acc_not_found':
            try:
                bank.get_account("account5")
            except ValueError as e:
                print(str(e))
                print("Operations")
                print(bank.get_operations())

        elif name=='insuff_fund':
            bank.create_account("account4")
            print(f'This is our bank:{bank}')
            amount_deposit=input("enter an amount to deposit")
            bank.deposit("account4",amount_deposit)
            try:
                amount_withdrawl=input("enter an amount to withdraw")
                bank.withdraw("account4",amount_withdrawl)
          
                print(type(bank.withdraw))
          
                if amount_deposit<amount_withdrawl:
                    raise ValueError("Cant make a withdrawal, insufficient balance")
            except ValueError as e:
                print(e)
        
                print(bank.get_operations())
        else:
            print("invalid test case")
    except Exception as e:
        print(str(e))



run_single_test("create_account")
run_single_test("deposit")
run_single_test("withdraw")
run_single_test("acc_not_found")
run_single_test("insuff_fund")