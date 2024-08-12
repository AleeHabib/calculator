import time


def decorator(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        option = input("\nPress 'M' to go back: ")
        if option.upper() == "M":
            main()

    return wrapper


@decorator
def evaluate():

    while True:
        flag = True
        exp = input("\nEnter the expression you want to evaluate: ")
        print(f"\nYour given expression: {exp}")

        exp_list = exp.rstrip().split()

        valid_operators = {"+", "-", "/", "*", "(", ")"}

        for element in exp_list:
            if not (element.isnumeric() or element in valid_operators):
                print("\nInvalid expression, try again")
                flag = False
                break

        if flag:
            if "(" and ")" in exp_list:
                opening_br = exp_list.index("(")
                closing_br = exp_list.index(")")

                brackets = exp_list[opening_br : closing_br + 1]

                expression_in_brackets = " ".join(brackets)
                try:
                    exp = eval(expression_in_brackets)
                except ZeroDivisionError:
                    print("Can not divide by zero")
                    flag = False
                del exp_list[opening_br : closing_br + 1]
                exp_list.insert(opening_br, str(exp))

                simplified_expression = "".join(exp_list)
                try:
                    result = eval(simplified_expression)
                except ZeroDivisionError:
                    print("\nCan not divide by zero, try again")
                    flag = False
                if flag:
                    print(f"\nRESULT: {result}")
                    break
                else:
                    main()
            else:
                exp = " ".join(exp_list)

                try:
                    result = eval(exp)
                except ZeroDivisionError:
                    print("\nCan not divide by zero, try again")
                    flag = False

                if flag:
                    print(f"\nRESULT: {result}")
                    break
        else:
            evaluate()


def main():

    while True:
        print("\n----------------------------")
        print("\n1. Evaluate my expression.")
        print("2. Exit")
        print("\n----------------------------")

        try:
            option = int(input("What do you want to do?: "))
        except ValueError:
            print("\nOption should be a valid integer")
        if option == 1:
            evaluate()
        elif option == 2:
            print("Exiting..")
            time.sleep(1)
            exit
        else:
            print("\nInvalid option, try again")


if __name__ == "__main__":
    main()
