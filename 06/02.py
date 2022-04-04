# i hope u have some time :)

file = open('input.txt', 'r')
line = file.readline()
file.close()


list = line.split(',')
tempList = [1]
tempList.clear()
day = 1


i = 0
for word in list:
    list[i] = int(list[i])
    i = i +1

#all items in list are now int

i = 0
while(day <= 256):

    for element in list:
        if(list[i] == 0):
            tempList.append(8)
            list[i] = 6
        else:
            list[i] = list[i] - 1

        i = i + 1

    i = 0
    list = list + tempList
    tempList.clear()
    day = day + 1

print(len(list))