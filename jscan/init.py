from itertools import combinations

import mysql.t_base as tb
import common.arithmetics as arith
import historyfilter as hf

data = list()
arr = []
counter = 1
while counter < 34:
    arr.append(counter)
    counter += 1
reds = list(combinations(arr, 6))

# change rule
blues = list()
for i in range(17):
    if i > 0:
        blues.append(i)

dlist = hf.getDif()
for j in reds:
    for blue in blues:

        if blue in list(j):
            continue
        newOne = list(j + (int(blue),))

        if arith.oddCount(newOne) != 4:
            continue

        if len(set.intersection(set(newOne), set(dlist))) < 1:
            continue
        if arith.list_continue_count(list(j)) != 0:
            continue

        if hf.filterList(newOne):
            continue

        if arith.list_continue_maxlen(list(j)) > 2:
            continue
        byBlue = hf.getHistoryBlue(blue)

        if len(set.intersection(set(newOne), set(byBlue))) > 2:
            continue
        if arith.max_intersection(newOne, hf.history) > 4:
            continue
        data.append(j + (int(blue),))
tb.t_base_clear()
tb.t_base_insert(data)
