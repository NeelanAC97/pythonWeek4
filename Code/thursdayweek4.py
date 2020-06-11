def prime_no_checker(number):
    
    is_prime = False

    if number > 2:
        for i in range(2,number):
            if number % i == 0:
                return False
            else:
                return True
    elif number == 2:
        return True
    else:
        return False


