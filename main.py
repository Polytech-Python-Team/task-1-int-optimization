def bin_search(sign=1):
    l, r = 0, sign * 10 ** 100
    res = 0
    while l != r:
        res = (l + r) // 2
        y = (l + r) // 2

        if id(res) == id(y):
            l = res + sign
        else:
            r = res - sign

    return res


M = bin_search(-1)
N = bin_search()

print(f"Максимальный диапозон значений целых чисел для которых id(a) == id(a), где a - целое число - [{M}, {N}].")
