import numpy


file = open('input.txt')
lines = file.readlines()
file.close()


tempList = []
inputLine = np.array()

i = 0
summedUp = 0

for line in lines:
    pos = line.find('|')
    tempList[i] = line[:pos - 1]
    print(tempList[i])
    input()
    i = i + 1

    
# 1, 4, 7 or 8
# ------------composition:
# 1 uses 2
# 4 usese 4
# 7 uses 3
# 8 uses 7

        



print('Solution part 2: ', summedUp)
        
        
    
