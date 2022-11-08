import random 

should_continue = True 

while should_continue:
    x= input('Enter [r,p,s] ')
    
    gen= {1:'r', 2:'s', 3:'p'}
    
    choice=gen[random.randint(1,3)]
    
    print(f'comp_chice {choice}')
    
    win_comb = [('p','r'),('r','s'),('s','p')]
    if x == choice:
        print('A draw')
    elif (x, choice) in win_comb:
        print('You win')
    else:
        print('You lost')
        
        
    should_continue = input('Want to proceed? [y/n]').lower() == 'y'
