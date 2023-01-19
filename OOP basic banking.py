def create_account (name, balance):
    return name, balance


def deposit(account, amount):
    return account[0] ,account[1]+amount
def withdraw(account,amount):
    if account[1] >= amount:
        return account[0], account[1] - amount
    else:
        return account[0],account[1]

def check_balance(account):
    return account

rahim = create_account('Abdul', 500)
add = deposit(rahim,200)
money_back = f'After withdrawing{withdraw(add,100)}'
final = check_balance(account=money_back)
ad = f'Final balance is {final[26:30]}'
print(add,money_back,ad)