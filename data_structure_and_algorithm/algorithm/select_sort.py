def select_sort(slist):
    for i in range(len(slist)):
        x = i
        for j in range(i, len(slist)):
            if slist[j] < slist[x]:
                x = j
        slist[i], slist[x] = slist[x], slist[i]
    return slist


slist = select_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
print(slist)