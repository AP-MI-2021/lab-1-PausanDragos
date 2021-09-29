import math
'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  for divisor in range(2, int(math.sqrt(n))):
    if n%divisor==0:
      return False
  return True
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  prod=1
  for item in lst:
    prod*=item
  return prod
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while y:
    r=x%y
    x=y
    y=r
  return x
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  return
  
def main():
  n = input('introduceti un numr: ')

  if is_prime(int(n)):
    print(n + ' e prim')
  else:
    print(n + ' nu e prim')

  print(get_product([3,4,5]))

  print(get_cmmdc_v1(10,5))

if __name__ == '__main__':
  main()
