
# Generate list from given numbers
num = 12345678
strList = list(map(int, str(num)))
print("Num to List...", strList)


#Revers String withut splice
str = 'suraj'
rev = ''
for s in str:
    rev = s + rev
print("Reversed string..", rev)


# Count Words in String
str = 'my name is suraj'
strls = str.split()
print("Count..", len(strls))