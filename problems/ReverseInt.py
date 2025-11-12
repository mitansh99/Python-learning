# given x as a signed 32-bit integer, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1  # gettig the sign of the num
    x = abs(x)


    rev = int(str(x)[::-1]) * sign # str(x) - convert to the string [::-1] - reverse the string and int() convert to the number * sign give the sign

    if rev <= -2**31 or rev >= 2*31: # overflow checking of 32 bit int 
        return 0

    return rev 
