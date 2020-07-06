
def list_continue_maxlen(list):
    sublist=set()
    dict={}
    for i in range(len(list)):
        if i < len(list)-1 and int(list[i])+1 == int(list[i+1]):
            sublist.add(list[i])
            sublist.add(list[i+1])
        else:
            dict.setdefault(str(sublist), len(sublist))
            sublist.clear()
    values=dict.values()
    return max(values)


