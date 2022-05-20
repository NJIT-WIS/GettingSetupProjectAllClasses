"""This is the main startup of the app"""


def main():
    """This is the main function that is run"""
    print_hello_name()


def print_hello_name(name='world'):
    """This function prints Hello Some Name"""
    print("Hello {}".format(name))


if __name__ == '__main__':
    """This causes the hello world function to be called if this is the __main__ top level of code"""
    main()
