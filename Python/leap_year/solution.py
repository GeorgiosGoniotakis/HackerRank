def is_leap(year):
    if not 1990 <= year <= 10**5:
        return False
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


