'''
No description needed at this point. Fill in the functions below
according to the description provided. 

'''


# --------------------------------------------------------------
# 1) Numeric string sum
# --------------------------------------------------------------

def sum_words(items):
    '''
    Assume that items is a list of strings, which may or may not
    contain valid integers. For example, one such list might be:
    
    [ '1', '8', 'hello', '3', '5ive', '42'  ] (sum = 54)
    
    This function should return the sum of the integers, without
    crashing on non-digit strings. That is, 'hello' and '5ive'
    in the above example should not cause your function to crash.

    You can use the int() function to parse integer values from
    the strings, but you'll have to use a try/except block to 
    avoid runtime errors when parsing non-integer strings.

    Do NOT use if/else logic to test the strings. Use try/except 
    to catch runtime errors if they happen.

    '''
    res = 0
    for item in items:
        try:
            num = int(item)
            res += num
        except ValueError:
            continue
    return res

    
# --------------------------------------------------------------
# 2) Maximum population
# --------------------------------------------------------------

def max_pop(items):
    '''
    Assume that items is a list of tuples (country, population).
    Return the country with the largest population.
    Use exception handling to deal with a bad tuple, in which 
    case you return None.

    For example:
    
    max_pop([('China', 1389618778), ('India', 1311559204), ('US', 331883986)])
    would return 'China'

    max_pop([('China'), ('India', 1311559204), ('US', 331883986)])
    would return None, because ('China') is missing the population

    max_pop([('China', 1389618778), ('India', 'lots'), ('US', 331883986)])
    would return None, because 'lots' is not a valid integer

    Do NOT use if/else logic to test the tuple. Use try/except to 
    catch runtime errors if they happen.

    HINT: you do not need to say the type of exception, just say except

    '''
    cur = 0
    res = ''
    for item in items:
        try:
            cur = max(item[1], cur)
            if cur == item[1]:
                res = item[0]
        except:
            return None
    return res


# --------------------------------------------------------------
# 3) Product by index
# --------------------------------------------------------------

def product_by_index(items, ids) :
    '''
    Assume items is a list of numbers.
    Assume ids is a list of integers.
    This function should return the product of the elements of 
    items at every index in ids
    If either items or ids is empty, return None.

    For example:
    product_by_index([5, 2, 9], [1, 0, 1, 1]) would return 40, 
    since 2 * 5 * 2 * 2 = 40.

    Use exception handling to handle IndexError exceptions
    when the index is out of bounds. In this case, return None.

    For example: 
    productindex([5, 2, 9], [1, 0, 1, 1, 5]) would return None.

    Do NOT use if/else to test index ranges. You should use
    a try/except block.    

    '''
    res = 1
    for i in ids:
        try:
            x = items[i]
            res *= x
        except:
            return None
    return res


# --------------------------------------------------------------
# 4) Coin counter
# --------------------------------------------------------------

def coins(s) :
    '''
    Assume s is a string representing coins, where q is for 
    quarter, p is for penny, d is for dime, and n is for nickel.

    Return the total amount of money that the string represents.
    
    If the string contains characters that cannot be converted 
    to coins, you should raise a ValueError exception.

    For example, 
    money('ppp') returns 3
    money('pnqqqnd') returns 96
    money('43') raises ValueError

    '''
    res = 0
    coins = {
        'q': 25,
        'p': 1, 
        'd': 10,
        'n': 5
    }
    for char in s:
        try:
            val = coins[char]
            res += val
        except KeyError:
            raise ValueError
    return res


# --------------------------------------------------------------
# 5) Name checker
# --------------------------------------------------------------

def check_name(first, last):

    '''
    Assume first and last are strings. This function should
    check if first and last are valid names. A valid name begins
    with a capital letter, and the rest of the characters are 
    lowercase. 
    
    If the names are valid, return their concatenation in the 
    following form: 'last, first'. For example, if first is
    'Alex' and last is 'Ufkes', return 'Ufkes, Alex'

    If either name is not valid, raise a ValueError exception.
    '''
    def verify_name(name):
        for i in range(len(name)):
            if not name[i].isalpha():
                raise ValueError
            if i == 0 and name[i].islower():
                raise ValueError
            elif i != 0 and name[i].isupper():
                raise ValueError
        return name
    return f'{verify_name(last)}, {verify_name(first)}'


# --------------------------------------------------------------
# 6) Integers from iterators
# --------------------------------------------------------------

def get_next_int(it):

    ''' 
    Assume that 'it' is an iterator, NOT a list/sequence. Given
    the iterator, this function returns the next integer value
    produced by the iterator.

    If the iterator runs out of elements, and cannot produce 
    another integer, return None.

    Hint: Use the next() function to get elements, and be sure 
    to catch the StopIteration error when it occurs. 

    '''
    try:
        cur = next(it)
        while type(cur) != int:
            cur = next(it)
        return cur
    except StopIteration:
        return None

