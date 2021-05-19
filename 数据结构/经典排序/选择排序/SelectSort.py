def select_sort(alist):
    for j in range(len(alist) - 1):
        min_num = j
        for i in range(j,len(alist)):
            if alist[i] < alist[min_num]:
                min_num = i
        alist[j], alist[min_num] = alist[min_num], alist[j]

