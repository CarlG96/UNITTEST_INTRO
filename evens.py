def even_number_of_evens(numbers):
    """ 
    Should raise a TypeError is numbers not a list.
    if numbers is empty return False.
    If number of evens is odd, return False.
    If number of evens is 0, return False.
    If number of evens is even, return True.
    """
    if isinstance(numbers, list):
        if numbers == []:
            return False
        else:
            evens = 0
        
        for number in numbers:
            if number % 2 == 0:
                evens += 1
            else:
                return False
        return evens % 2 == 0
    else: 
        raise TypeError('A list was not passed into the function')
    

if __name__ == '__main__':
    print(even_number_of_evens(5))