#   Girilen sayının asal olup olmadığını bulma uygulaması


number = int(input('Please enter the number:'))
isPrime = True

if number == 1:
    isPrime = False
    print('(1) is not prime number.')

for i in range(2,number,1):
    if (number%i == 0):
        isPrime = False
        break

if isPrime:
    print('Number is prime.')
else:
    print('Number is not prime.')
