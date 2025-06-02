def square_digits(num):
    num_str = str(num)
    result_str = ""
    for digit in num_str:
        squared = str(int(digit) ** 2)
        result_str += squared
    return int(result_str)
