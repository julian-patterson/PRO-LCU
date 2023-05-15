# 4

def count_numbers(text):
    list = text.split()
    count = 0
    for word in list:
        if word.isdigit():
            count += 1
    return count


# 5


def recursive_even_sum(x):
    if len(x) == 0:
        return 0
    elif x[0] % 2 == 0:
        return x[0] + recursive_even_sum(x[1:])
    else:
        return recursive_even_sum(x[1:])


# 6
def recursive_power(n, x):
    if x == 0:
        return 1
    else:
        return recursive_power(n, x-1) * n

# 7


def PrintCodes(L):
    L.sort()
    previous_code = None
    counter = 0
    for code in L:
        if code == previous_code:
            continue
        else:
            previous_code = code
            counter += 1
            product_code = "Product Code"
            print("{:15s} {:3d} x {:1d}".format(
                product_code, code, L.count(code)))
    return counter


codes = [101, 61, 55, 80, 61, 44, 101, 61, 80, 55, 80]

print("The number of different product codes is: ", PrintCodes(codes))
