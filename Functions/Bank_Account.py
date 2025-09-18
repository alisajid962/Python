def bank_account(balance):
    charge = int(balance)
    
    # deposit function
    def deposit(money):
        nonlocal charge 
        if money > 0:
            charge += money
        return charge

    def withdraw(amount):
        nonlocal charge
        if amount <= charge:
            charge -= amount
        else:
            print("Insufficient balance!")
        return charge

 
    return deposit, withdraw



deposit, withdraw = bank_account(122000)  
print(deposit(5000))   
print(withdraw(2000))  
print(withdraw(130000))
