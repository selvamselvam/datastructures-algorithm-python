def sum1(n):
    final_sum = 0
    for i in range(n + 1):
        final_sum += i
    return final_sum


x = 10
print(" Sum {} of is {}".format(x, sum1(x)))
