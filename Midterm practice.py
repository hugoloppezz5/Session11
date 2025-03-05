# Question 1
# Question 2
def divisors(number):
    for i in range(1, number + 1):
        if number / i != 0:
            print(number)


# Question 3
def multiple_of_6():
    while True:
        try:
            number = input("Please give me a multiple of 6: ")
            n = int(n)
            if n % 6 == 0:
                return n
            else:
                print("That is not a multiple of 6")
        except ValueError:
            print("That is not a valid number")


multiple_of_6()