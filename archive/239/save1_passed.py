from fizzbuzz import fizzbuzz

# write one or more pytest functions below, they need to start with test_
def test_for_fizz():
    for num in [3, 6, 9, 12]:
        assert fizzbuzz(num) == "Fizz"

def test_for_buzz():
    for num in [5, 10, 20, 25]:
        assert fizzbuzz(num) == "Buzz"
    
def test_for_fizzbuzz():
    for num in [15, 45, 75, 225]:
        assert fizzbuzz(num) == "Fizz Buzz"

def test_for_other():
    for num in [1, 2, 4, 7, 8, 11, 13, 14, 16]:
        assert fizzbuzz(num) == num