def bin_search(sign=1):
    l = 0 if sign == 1 else -10**100
    r = 10*100 if sign == 1 else -1
    while l <= r:
        res = (l + r) // 2
        y = (l + r) // 2

        if id(res) == id(y):
            if sign == 1:
                l = res + 1
            else :
                r = res - 1
        else:
            if sign == 1:
                r = res - 1
            else:
                l = res + 1

    return r if sign == 1 else l


M = bin_search(-1)
N = bin_search()

print(f"Максимальный диапазон значений целых чисел для которых id(a) == id(b), где a == b - [{M}, {N}].")
