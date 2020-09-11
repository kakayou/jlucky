import mysql.t_facility as fc

odd_dict = fc.t_facility_odd()

def list_continue_maxlen(list):
    sublist = set()
    dict = {}
    for i in range(len(list)):
        if i < len(list) - 1 and int(list[i]) + 1 == int(list[i + 1]):
            sublist.add(list[i])
            sublist.add(list[i + 1])
        else:
            dict.setdefault(str(sublist), len(sublist))
            sublist.clear()
    values = dict.values()
    return max(values)


def list_continue_count(list):
    count = 0
    sublist = set()
    dict = {}
    for i in range(len(list)):
        if i < len(list) - 1 and int(list[i]) + 1 == int(list[i + 1]):
            sublist.add(list[i])
            sublist.add(list[i + 1])
        else:
            dict.setdefault(str(sublist), len(sublist))
            sublist.clear()
    values = dict.values()
    for i in values:
        if i > 1:
            count = count + 1
    return count


def max_intersection(list, history):
    values = []
    for i in range(8):
        values.append(len(set.intersection(set(list), set(history[i]))))
    return max(values)


def random_Rate(name):
    sql = "select {0}, count(*) as v_count from t_facility GROUP by {1} order by v_count DESC".format(name, name)
    rates = fc.t_facility_sql(sql)
    dict = {}
    for i, val in enumerate(rates):
        dict[val[0]] = val[1]
    total = sum(dict.values())
    for key, value in dict.items():
        dict[key] = value / total
    return dict

def odd_Rate():
    rates = {}
    total = sum(odd_dict.values())
    for key, value in odd_dict.items():
        rates[key] = value / total
    return rates

def continue_location(list):
    location = 0
    if list_continue_count(list) == 0:
        location = 0
    if list_continue_count(list) == 1:
        if list[1] == list[0] + 1:
            location = 1
        if list[2] == list[1] + 1:
            location = 2
        if list[3] == list[2] + 1:
            location = 3
        if list[4] == list[3] + 1:
            location = 4
        if list[5] == list[4] + 1:
            location = 5
    return location


def history_location(history):
    locations = set()
    for i in range(3):
        item = continue_location(history[i])
        locations.add(item)
    return locations


def isArithmeticProgression(arr) -> bool:
    for i in range(len(arr) - 2):
        if arr[i + 1] - arr[i] != arr[i + 2] - arr[i + 1]:
            return False
    else:
        return True

def oddCount(arr):
    result = 0
    for i in range(len(arr)):
        if arr[i] % 2 is 0:
            result = result + 1
    return result
