def high_and_low(numbers):
    num_str_list = numbers.split()

    num_list = []
    for num_str in num_str_list:
        num_list.append(int(num_str))

    max_num = max(num_list)
    min_num = min(num_list)

    return f"{max_num} {min_num}"
