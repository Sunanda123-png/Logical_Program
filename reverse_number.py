import logging

logging.basicConfig(filename="reverse_number.py", filemode="w")


def reverse_number(num):
    """
    :param num:
    :return:
    """
    reversed_num = 0

    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    print("Reversed Number: " + str(reversed_num))


if __name__ == "__main__":
    try:
        num = int(input("Enter the numbers"))
        reverse_number(num)
    except:
        print("Enter valid input")
