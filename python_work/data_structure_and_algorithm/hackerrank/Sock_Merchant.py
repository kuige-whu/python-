from collections import Counter


def sockMerchant(n, ar):
    sum = 0
    for values in Counter(ar).values():
        sum += values // 2

    # for keys in Counter(ar).keys():
    #     print(keys)
    return sum


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)