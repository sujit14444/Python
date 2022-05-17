import random

#def guess(x):
#     guess=0
#     random_number = random.randint(1,x)

#     while guess != random_number:
#         guess =  int(input(f"Enter a number betwwen 1 and {x} :"))
#         if guess > random_number:
#             print("you guess is too  highhh !!!!!")
#         elif guess < random_number:
#             print("Your guessing is too low!!!")
#     print(f"Yayyyy!!! you guessed it correctly {random_number}! ")

def computer_guess(x):
    low=1
    high=x
    feedback = ''
    while feedback != 'c':
        if low!= high:
            guess =  random.randint(low,high)
        else:
            guess= low  #also high
        feedback = input(f"is{guess} too high(H), too low(L), or correctly(C)!!! :").lower()
        if feedback == 'h':
            high=guess-1
        elif feedback == 'l':
            low = guess+1
    print(f"yayy computer guessed it correctly and you have lossed it{guess} ")


if __name__=="__main__":
    computer_guess(10)