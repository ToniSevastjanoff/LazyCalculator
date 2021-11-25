# write your code here
operations = ("+", "-", "*", "/")
memory = 0.0
cont = "y"


def checksave(in_result):
    ch_answer = input("Do you want to store the result? (y / n):")

    if is_one_digit(in_result):

        if ch_answer == "y":
            ch_answer = input("Are you sure? It is only one digit! (y / n)")

            if ch_answer == "y":
                ch_answer = input("Don't be silly! It's just one number! Add to the memory? (y / n)")

                if ch_answer == "y":
                    ch_answer = input("Last chance! Do you really want to embarrass yourself? (y / n)")

    return ch_answer


def is_one_digit(v):
    print("V", v)
    if type(v) != int and type(v) != float:
        return False

    if int(v) == v:
        v = int(v)

    if -10 < v < 10 and type(v) == int:
        return True
    else:
        return False


def lazytest(v1, v2, v3):
    print("X", v1, "Y", v2, "Oper", v3)
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg += " ... lazy"

    if v1 == 1 or v2 == 1 and v3 == "*":
        msg += " ... very lazy"

    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += " ... very, very lazy"

    if msg != "":
        print("You are" + msg)


while cont == "y":

    x = None
    y = None
    oper = None

    while (x is None and x != "M") or (y is None and y != "M") or (oper not in operations) or (y == 0 and oper == "/"):
        print("Enter an equation")
        calc = input()

        a = calc.split()
        x = a[0]
        oper = a[1]
        y = a[2]

        if x == "M":  # read from memory
            x = memory
        else:
            try:
                # Convert it into integer
                x = int(x)
            except ValueError:
                try:
                    # Convert it into float
                    x = float(x)
                except ValueError:
                    pass

        if y == "M":
            y = memory
        else:
            try:
                # Convert it into integer
                y = int(y)
            except ValueError:
                try:
                    # Convert it into float
                    y = float(y)
                except ValueError:
                    pass

        lazytest(x, y, oper)

        if x is None or y is None or type(x) == str or type(y) == str:
            print("Do you even know what numbers are? Stay focused!")
        if oper not in operations:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        if y == 0 and oper == "/":
            print("Yeah... division by zero. Smart move...")

    if x is None or y is None or type(x) == str or type(y) == str:
        continue

    result = "Something went wrong."
    if oper == "+":
        result = float(x + y)
    elif oper == "-":
        result = float(x - y)
    elif oper == "*":
        result = float(x * y)
    elif oper == "/":
        result = float(x / y)

    print(result)

    answer = checksave(result)
    if answer == "y":
        memory = result

    cont = input("Do you want to continue calculations? (y / n):")
