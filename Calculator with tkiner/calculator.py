# calculator

dict = {}


# addition
def add(num1, num2):
    sum = num1 + num2
    return sum


# subtraction
def sub(num1, num2):
    sub = num1 - num2
    return sub


# multiplication
def mul(num1, num2):
    mul = num1 * num2
    return mul


# Division
def divided(num1, num2):
    div = num1 / num2
    return div


def calculator():
    x = int(input("Enter a number \n"))
    y = int(input("Enter another number \n"))
    dict['add'] = add(x, y)
    dict['sub'] = sub(x, y)
    dict['mul'] = mul(x, y)
    dict['divided'] = divided(x, y)

    for operation in dict:
        print(operation)

    should_operation = True
    while should_operation:
        want_operation = input(" What do you want  ")
        operational_function = dict[want_operation]

        print(f"The {want_operation} of {x} and {y} answer is  {operational_function}")
        if input(
                f"Enter continue with the {operational_function} as for yes type 'y' or no as well exit type n \n ") == 'y':
            x = operational_function
        else:
            should_operation = False


calculator()
