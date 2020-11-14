import random  
i =random.randint(1,9)
print('number guessing game')
chances = 0 
print('guess a no. between 1-9')
while chances < 5 :
    guess=int(input('Enter your guess - '))
    if guess== i : 
        print('congratulations ,your guess is correct ')
        break 
    elif guess < i :
        print('your guess is too low,guess a higher no.')
    else:
        print('your guess is too high guess a lower no ].')
    chances +=1 

if not chances<5:
    print('you have lost the game')
