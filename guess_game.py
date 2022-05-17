import random

def guess(x):
    
    guess_number = random.randint(1,x)  # Generates random number.
    guess=0

    while guess!= guess_number:
        guess = int(input(f"enter a number betweenn 1 and {x}:"))
        print(guess)
        
        if guess > guess_number:
            print("Ooops!!! you guessed it bit high!! ")
        elif guess < guess_number:
            print("Opppss!!! You guessed bit lower number!!")

    print(f"Yayyy you made it You guessed it right!!! its :{guess_number}")



if __name__=="__main__":
	guess(10)