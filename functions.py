
number = int(input("Enter an integer: "))
def fact(num):
    count = 1
    factorial = 1
    while count <= num:
            factorial = factorial * count
            count += 1
    return factorial
print(fact(number))
