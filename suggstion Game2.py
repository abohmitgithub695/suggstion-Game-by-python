import random
random_num=random.randint(1,10)
tries=0
n=3
while tries<3:
      input_num=int(input('Enter  number from (1) to (10): '))
      while input_num not in range(1,11):
       input_num=int(input('The num must be between (1 to 10), Enter  number from (1) to (10): '))
      if random_num==input_num:
       print('...Great your num is EQUAL the random num you win...') 
       break
      else:
        n-=1
        print(f'(Your num is not EQUAL the random num,you have (\'{n}\') tries)')
        tries+=1
      if tries==3:
        print('\n...You tried three times and you are failed...')
        break
    
