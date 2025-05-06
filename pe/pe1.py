

def find_sum():
    sum_three = sum([3 * number for number in range(333+1)])
    sum_five = sum([5 * number for number in range(199+1)])
    sum_fifteen = sum([15 * number for number in range(66+1)])

    return sum_three + sum_five - sum_fifteen


print(find_sum())