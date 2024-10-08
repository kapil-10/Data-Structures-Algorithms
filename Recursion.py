import time
# example -1 Factorial using recursion and iteration
def factorial_recursion(number):
    if number == 0: # base condition required for factoril
        return 1
    elif number == 1: # base condition required for factoril
        return 1
    else:
        return number * factorial_recursion (number - 1)
         
def factorial_iter(number):
    result = 1
    if number < 0 or number == 0:
            raise Exception('Invalid number')
    else:
        for value in range(1,number+1):
            result = value * result
    return print(result)


# example 2 Fibonacci sequence

def fibonacci_rec(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return number + fibonacci_rec(number - 1)
        
def fibonacci_iter(number):
    result = 0
    for value in range(0,number+1):
        result = result + value
    return print(result)


if __name__ == '__main__':

    start_time_itr = time.time()
    number = int(input('enter a number to perform factorial: ' ))
    print(factorial_recursion(number))
    end_time_itr = time.time()
    print('The time it took to perform factorial using iteration is: ',(start_time_itr - end_time_itr))

    print('')
    start_time_rec = time.time()
    number = int(input('enter a number to perform factorial: ' ))
    print(factorial_iter(number))
    end_time_rec = time.time()
    print('The time it took to perform factorial using recursion is: ',(start_time_rec - end_time_rec))

    print('')
    number = int(input('enter a number to perform finonacci iteration sequence: ' ))
    fibonacci_iter(number)

    print('')
    number = int(input('enter a number to perform finonacci recursion sequence: ' ))
    print(fibonacci_rec(number))
    print('')
