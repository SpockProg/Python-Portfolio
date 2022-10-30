import random

tries = 0 

y=random.randint(1, 50)

while tries<6:
    x=int(input('make a guess'))
    
    tries+=1 

    if x == y:
        print(f'You win in {tries} tries')
        break
    
    if x<y:
         print('Bigger')

    if x>y:
         print('Less') 

    if x != y and tries == 6:
        print(f'sorry,you lost. Number was {y}')
        break
