def exhaustive_enumeration(target):
    answer = 0

    # While loop: Exhaustive enumeration
    # Increments `answer` by 1 until it finds an exact square root or surpasses the target.
    while answer**2 < target:
        answer += 1

    if answer**2 == target:
        print(f'The square root of {target} is {answer}')
    else:
        print(f'{target} does not have an exact square root')

def approximation(target):
    epsilon = 0.01  # Desired precision
    step = epsilon**2
    answer = 0.0

    # While loop: Approximation
    # Increments `answer` in small steps until the difference between `answer` squared and the target is less than `epsilon`.
    while abs(answer**2 - target) >= epsilon and answer <= target:
        answer += step
        print(f'Difference: {abs(answer**2 - target)}, Answer: {answer}')

    if abs(answer**2 - target) >= epsilon:
        print(f'Could not find the square root of {target}')
    else:
        print(f'The square root of {target} is {answer}')

def binary_search(target):
    epsilon = 0.01  # Desired precision
    low = 0.0
    high = max(1.0, target)
    answer = (high + low) / 2  # Initial midpoint

    # While loop: Binary search
    # Reduces the search range by half in each iteration until finding an approximation of the square root with the desired precision.
    while abs(answer**2 - target) >= epsilon:
        print(f'low={low}, high={high}, answer={answer}')
        if answer**2 < target:
            low = answer  # Adjusts the lower bound
        else:
            high = answer  # Adjusts the upper bound
        answer = (high + low) / 2  # Recalculates the midpoint

    print(f'The square root of {target} is {answer}')

def run():
    # Menu to select the method
    method_type = int(input('''
        1. Exhaustive Enumeration
        2. Approximation
        3. Binary Search
        Select the method: '''))

    num = int(input('Enter the number to find its square root: '))

    if method_type == 1:
        exhaustive_enumeration(num)
    elif method_type == 2:
        approximation(num)
    elif method_type == 3:
        binary_search(num)
    else:
        print('Please enter a valid option')

if __name__ == "__main__":
    run()
