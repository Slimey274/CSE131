import math
# Check to see if a number is a prime number.

def is_number_prime(number):
    '''Return true if a number is Prime.
    Only have to test up to the square root of a number.'''
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:            
        is_prime = True

        end_condition = math.ceil(math.sqrt(number))
        #print(end_condition)

        for counter in range(2, end_condition + 1, 1):
            is_prime = is_prime and number % counter != 0
    return is_prime

def test_is_number_prime():

    assert is_number_prime(1) == False
    assert is_number_prime(2) == True
    assert is_number_prime(0) == False
    assert is_number_prime(-1) == False

    print('all tests pass')

def test_all_numbers(limit):

    for i in range(limit):
        if is_number_prime(i):
            print(f"{i} is prime")

def main():

    test_is_number_prime()

    test_all_numbers()
# if __debug__:
#     print(is_number_prime(101))
#     while 24:
#         number = int(input("Please input a number to test"))
#         print(f"{number} is Prime: {is_number_prime(number)}")
main()