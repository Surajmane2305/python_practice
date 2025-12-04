# 1. Find all pairs in a list whose sum is equal to a given number.

num_list = [1,2,3,4,5,6,7]
matchNum = 5
pairs = []

for x in num_list:
    for y in num_list:
        matched = int((x + y)) == matchNum
        if matched:
            pairs.append((x,y,))
print("Matched paires....", pairs)            