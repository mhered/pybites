def positive_divide(numerator, denominator):
    try: 
        result = numerator/denominator
        if result < 0:
            raise ValueError
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise TypeError("I caught a TypeError")
    except ValueError:
        raise ValueError("I caught a negative result")
    
    return result

# print(positive_divide(-1,2))
# print(positive_divide(2,-1))
# print(positive_divide(1, 's'))
# print(positive_divide([], 2))
# print(positive_divide(1,"two"))