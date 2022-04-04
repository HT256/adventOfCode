file = open('input.txt')
lines = file.readlines()
file.close()


tempList = []

i = 0
counter = 0
for line in lines:
    pos = line.find('|')
    lines[i] = line[(pos + 2):]
    tempList = tempList + lines[i].split()
    i = i + 1

    
# 1, 4, 7 or 8
# ------------composition:
# 1 uses 2
# 4 usese 4
# 7 uses 3
# 8 uses 7

for item in tempList:
    if((len(item) == 2) or (len(item) == 4) or (len(item) == 3) or (len(item) == 7)):
        counter = counter + 1

print('Solution part 1: ', counter)
        
        
    
