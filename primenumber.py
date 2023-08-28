prime_number = int(input("Check this number: "))

def prime_checker(number):
  is_prime = True
  for i in range(2,number):
      if number % i == 0:
          is_prime = False
  if is_prime:        
      print(f"{number}: It is a prime number")
  else:
      print(f"{number}: NOT a prime number")

prime_checker(number=prime_number)
    
