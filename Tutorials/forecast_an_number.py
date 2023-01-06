import random
number = random.randint(1,100)


right = 5

while right > 0:
    right -= 1
    forecast = int(input('Please enter a number: '))


    if number == forecast:
        print('Congratulations, value is correct.')
        break
    elif number > forecast:
        print('Please enter an upper number.')
    else:
        print('Please enter a lower number.')

    if right == 0:
        print(f"Sorry, you don't have any right. Also the correct number is : {number}")
        
        
