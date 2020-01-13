from itertools import combinations,permutations

redballs=[]
counter=1
while counter < 33:
    redballs.append(counter)
    counter += 1

c = list(combinations(redballs, 6))


