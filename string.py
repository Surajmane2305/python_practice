
#1 Generate list from given numbers.
num = 12345678
strList = list(map(int, str(num)))
print("Num to List...", strList)


#2 Revers String without splice.
str = 'suraj'
rev = ''
for s in str:
    rev = s + rev
print("Reversed string..", rev)


#3 Count Words in String.
str = 'my name is suraj'
strls = str.split()
print("Count..", len(strls))

# 4 Count Characters in string and show cont
string = 'banana'
count_dict = {}

for y in string:
    count_dict[y] = count_dict.get(y,0) +1
print("Count Characters of string...",count_dict)    


#5 Print duplicate characters in a string and their counts.
string = "Banana"
count = {}
for x in string:
    count[x] = count.get(x, 0) + 1

for y in count:
    if count[y] > 1:
        print("Duplicate Count..", y, count[y])

