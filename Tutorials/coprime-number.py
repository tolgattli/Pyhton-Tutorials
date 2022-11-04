#   Girilen sayının asal olup olmadığını bulma uygulaması


number = int(input('Please enter the number:'))
isCoprime = True

if number == 1:
    isCoprime = False
    print('(1) is not coprime number.')

for i in range(2,number,1):
    if (number%i == 0):
        isCoprime = False
        break

if isCoprime:
    print('Number is coprime.')
else:
    print('Number is not coprime.')
