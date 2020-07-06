from itertools import combinations, permutations
import random
import Levenshtein
import mysql.t_facility as fc
import mysql.t_base as tb
import common.arithmetics as arith

data = list()
arr = []

counter = 1
while counter < 34:
    arr.append(counter)
    counter += 1
reds = list(combinations(arr, 6))
history = fc.t_facility_reds()


red1 = random.randint(1,5)
while red1 == history[0][0]:
    red1 = random.randint(1,5)

blue=12
for j in reds:
    # 最大的red1=3 red2=4
    if j[0] != red1:
        continue
    if j in history:
        continue
    total = sum(j)
    if total < 80 or total > 120:
        continue
    if arith.list_continue_maxlen(list(j)) > 2:
        continue
    if int(Levenshtein.distance(str(j), str(history[0]))) < 9:
        continue
    if int(Levenshtein.distance(str(j), str(history[1]))) < 9:
        continue
    if int(Levenshtein.distance(str(j), str(history[2]))) < 9:
        continue
    if len(set.intersection(set(j), set(history[0]))) > 1:
        continue
    if len(set.intersection(set(j), set(history[1]))) > 1:
        continue
    if int(j[5]) < 30:
        continue
    data.append(j + (blue,))
tb.t_base_clear()
tb.t_base_insert(data)


