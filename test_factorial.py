# from factorial import factorial 

# x = 1

# assert factorial(x) == 1

# x = 3

# assert factorial(x) == 6

# try:
#     assert factorial(-1) == None
# except AssertionError:
#     print("Test failed for input 1")


# # print(factorial(1))
# # print(factorial(2))
# # print(factorial(3))
# # print(factorial(4))
# # print(factorial(5))

from factorial import factorial


def test_factorial():
    assert factorial(-1) == None
    assert factorial(0) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6

# Test by category (a.k.a different use cases)

def test_factorial_positive():
    assert

def test_factorial_negative():

def test_factorial_zero():



