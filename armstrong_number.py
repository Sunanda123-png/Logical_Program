import logging

logging.basicConfig(filename="armstrong_number.py", filemode="w")


def armstrong_number(number):
    """
    :param number:
    :return:
    """
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if number == sum:
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")


if __name__ == "__main__":
    try:
        number = int(input("Enter the numbers"))
        armstrong_number(number)
    except:
        print("Enter the valid input")
