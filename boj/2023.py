n = int(input())

digit = [1,3,5,7,9]

def is_prime(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False
    return True

def find_prime(num):
    if len(str(num)) == n:
        print(num)
    else:
        for dig in digit:
            new_num = int(str(num) + str(dig))
            if is_prime(new_num):
                find_prime(new_num)
          
find_prime(2)
find_prime(3)
find_prime(5)
find_prime(7)