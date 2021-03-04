i = int(input("Number:"))


def type_of_card(i):
    first = str(i)[:2]
    first_visa = str(i)[:1]

    if (first == "34" or first == "37") and (len(str(i)) == 15):
        return "AMEX"
    if (first == "51" or first == "52" or first == "53" or first == "54" or first == "55") and (len(str(i)) == 16):
        return "MASTERCARD"
    if first_visa == 4 and len(str(i)) == 13 or 16:
        return "VISA"
    else:
        print("INVALID")
        return False


def validate_card(i):
    second = False
    sum_odd = 0
    sum_round = 0
    while i != 0:
        number = i % 10
        if second == False:
            sum_odd += number
            second = True
        else:
            number *= 2
            for x in str(number):
                sum_round += int(x)
            second = False
        i = i / 10
        i = int(i)
    if (sum_odd + sum_round) % 10 == 0:
        return True
    else:
        return False


if validate_card(i):
    print(type_of_card(i))
else:
    print("Invalid")
