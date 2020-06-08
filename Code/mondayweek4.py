def func(number):

    if number <0:
        return "Bad input"

    else:

        number2 = str(number)*2
        number3 = str(number)*3
        number4 = str(number)*4

        answer = int(number) + int(number2) + int(number3) + int(number4)

        return answer
