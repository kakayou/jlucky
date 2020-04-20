from itertools import combinations, permutations
import mysql.luckydb as luckydb

data = list()
arr = []

counter = 1
while counter < 34:
    arr.append(counter)
    counter += 1
reds = list(combinations(arr, 6))

# set blue 12

blue = 15
history = luckydb.t_facility_reds()

for j in reds:
    # 最大的red1=3 red2=4
    if j[0] !=3:
        continue
    if j[1] != 4:
        continue
    if j[2] < 12:
        continue

    if j[5] != 26:
        continue
    if j[4] == 25:
        continue
    if 21 in j:
        continue
    if j[3] > 15:
        continue

    #过滤等差数列
    if j[2]-j[1]==j[3]-j[2] & j[3]-j[2]== j[4]-j[3]:
        continue

    if j[1]-j[0]==j[2]-j[1] & j[2]-j[1]== j[3]-j[2] :
        continue

    if j[3] - j[2] == j[4] - j[3] & j[4] - j[3] == j[5] - j[4]:
        continue



    # 过滤掉已经出现的
    if j in history:
        continue
    row = (j + (blue,))
    data.append(j + (blue,))

luckydb.t_base_insert(data)


