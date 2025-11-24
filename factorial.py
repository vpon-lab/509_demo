def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    user_input = int(input("Enter a non-negative integer to compute its factorial: "))
    return factorial(user_input)

if __name__ == "__main__": #make sure the instructions below only executed if run by python script, otherwise not be executed
    print(main())
