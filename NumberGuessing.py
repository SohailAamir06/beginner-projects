import random
def numgues(num):
    unknownnum=random.randint(1,10)
    print("The random number is #")
    guess=0
    print("Guess the number \nyou got",num,"chances")
    for i in range(0,num):
        userguess=int(input("Enter your integer guess: "))
        guess+=1
        if userguess==unknownnum:
            print("GREAT!!! \nYou guessed the number right in",guess,"chances")
            break
        elif userguess<unknownnum:
            print("Wrong guess,guess a larger digit")
        elif userguess>unknownnum:
            print("Wrong guess,guess a smaller digit")
            
num=int(input("Enter the number of chances : "))
numgues(num)    
