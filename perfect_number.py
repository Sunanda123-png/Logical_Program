import logging

logging.basicConfig(filename="perfect_number.py", filemode="w")


def perfect_number(number):
    """
    :param number:
    :return:
    """
    result = 0
    for i in range(1, number):
        if number % i == 0:
            result = result + i
    if result == number:
        print("Entered number is perfect")
    else:
        print("Entered number is not perfect")


if __name__ == "__main__":
    try:
        number = int(input("Enter number to check perfect or not"))
        perfect_number(number)
    except Exception as e:
        print("Please enter valid input")
