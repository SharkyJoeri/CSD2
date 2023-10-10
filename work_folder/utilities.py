def get_integer_input(msg = False):
    while True:
        try:
            if msg != False:
                print(msg)
            user_input = input()
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("Entered number is not an integer")

def get_float_input(msg = False):
    while True:
        try:
            if msg != False:
                print(msg)
            user_input = input()
            integer_value = float(user_input)
            return integer_value
        except ValueError:
            print("Entered number is not a float")
