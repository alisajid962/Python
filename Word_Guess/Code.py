import random
print("========***=========***========")
chance = 5
guess= False
number = random.randint(1,15)
while chance >= 0 and not guess:
    user_guess = int(input("Enter Your Lucky Number(1-15): "))
    if user_guess == number:
        print(f"You Win in { chance - 1} chance")
        guess = True 
        
    elif user_guess < number:
        print("Too Low")
        print(f"You have {chance} chance left")
        chance -= 1
        
     
    elif user_guess > number:
        print("Too High")
        chance -= 1
        print(f"You have  {chance}  chance left")
        
        
    else:
        print("Invalid Input")
if not guess:
     print("You Lose")
     print(f"The number was {number}")
     print("========***=========***========")
