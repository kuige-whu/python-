def bubble_sort(blist):
    count = len(blist)
    for i in range(0, count):
        for j in range(i + 1, count):
            if blist[i] > blist[j]:
                blist[i], blist[j] = blist[j], blist[i]
    return blist


blist = bubble_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
print(blist)