'''
Julian Patterson 2131249
420-LCU Computer Programming
S. Hilal, instructor
Lab 9
'''

# Q1


def my_len(iterable):
    '''Returns the length of an interable'''
    length = 0
    for i in iterable:
        length += 1

    return str(length)


print(my_len([]))
print(my_len("Marianopolis"))
print(my_len((1, 5, 9, 2)))

# Q2


def my_sum(my_list):
    '''Returns the sum of all the items in a list'''
    if len(my_list) == 0:
        return 0

    else:
        total = 0
        for i in my_list:
            total = total + i
        return int(total)


# Test cases for Function my_sum
print(my_sum([1, 5, 9]))
print(my_sum([100, 200, 300.0]))
print(my_sum([]))  # returns 0

# Q3


def my_count(my_list, count):
    '''Mimics the behavior of the count function'''
    amount = 0
    for i in my_list:
        if i == count:
            amount += 1
            continue
        else:
            continue
    return amount


# Test cases for Function my_count
x = [1, 2, 3, 3]
print(my_count(x, 1))
print(my_count(x, 3))
print(my_count(x, 4))

# Q4


def my_find(my_list, value):
    '''Returns the index of a searched value'''
    index = -1
    for i in my_list:
        if i == value:
            index += 1
            return index
        else:
            i += 1
            index += 1
            continue
    return -1


# Test cases for Function my_find
print(my_find([1, 5, 9, 1], 0))  # returns -1
print(my_find([1, 5, 9, 1], 9))  # returns 2
print(my_find([1, 5, 9, 1], 1))  # returns 0

# Q5


def is_prime(n):
    '''Checks if a number is prime'''
    if n <= 1:
        return False
    if n == 3:
        return True
    else:
        for i in range(2, n//2):
            if n % i == 0:
                return False
            else:
                return True


# Test cases for Function is_prime
print(is_prime(0))  # prints False
print(is_prime(1))  # prints False
print(is_prime(3))  # prints True
print(is_prime(8))  # prints False
print(is_prime(19))  # prints True

# Q6


def my_product(my_list):
    '''Returns the product of all the numbers in a list'''
    if len(my_list) == 0:
        return 0

    else:
        product_total = 1
        for i in my_list:
            product_total *= i
        return product_total


# Test cases for Function my_product
print(my_product([1, 5, 9]))  # returns 45
print(my_product([100, 200, 0]))  # returns 0
print(my_product([]))  # returns 0


# Q7
def my_product_r(n):
    '''Returns the product of a list using a recursive function'''
    if len(n) == 0:
        return 0
    elif len(n) == 1:
        return n[0]
    return int(my_product_r(n[1:]))*n[0]


# Test cases for Function my_product_r
print(my_product_r([1, 5, 9]))  # returns 45
print(my_product_r([100, 200, 0]))  # returns 0
print(my_product_r([]))  # returns 0

# Q8


def sum_cubes_r(n):
    '''Returns the sum of cubes for a given integer. Ex. 3^3 + 2^3 + 1^3'''
    if n == 0:
        return 0
    else:
        return n**3 + sum_cubes_r(n-1)


# Test cases for Function sum_cubes_r
print(sum_cubes_r(4))  # returns 100
print(sum_cubes_r(5))  # returns 225

# Q9


def recursive_list_builder(n):
    '''Creates a list counting down from n- to the 0'''
    if n == 0:
        return [0]
    else:
        list = recursive_list_builder(n-1)
        list.insert(0, n)
        return list


print(recursive_list_builder(8))
print(recursive_list_builder(0))
