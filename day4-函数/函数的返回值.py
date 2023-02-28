# Date: 2023/2/28 上午9:52
def sum(a, b):
    sum = a + b
    return sum


print(sum(1, 20))


def calComputer(num):
    l = []
    result = 0
    i = 1
    while i <= num:
        result += i
        i += 1
        l.append(result)
    return l


print(calComputer(9))


