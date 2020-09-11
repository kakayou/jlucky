import Levenshtein

def max_distance(list, history):
    values = []
    for i in range(6):
        dis=Levenshtein.distance(str(list), str(history[i]))
        values.append(dis)
    return max(values)