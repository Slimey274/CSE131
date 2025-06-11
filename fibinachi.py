import time
count = 0
def fibonacci(number):
    numbers = [0, 1]
    for i in range(number):
        numbers[i % 1] = numbers[0] + numbers[1]
    return numbers[number % 2]

def fibonacci_recursion(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci_recursion(number - 1) + fibonacci_recursion(number - 2)


def main():
    number = int(input('Please enter in a number: '))
    fibonacci(number)
    fibonacci_recursion(number)

main()