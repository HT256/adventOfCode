file = open('input.txt', 'r')
lines = file.readlines()
file.close()

counter = 0
coordsList = []
doubleList = []
lineCounter = 0

for line in lines:
    lineCounter = lineCounter + 1
    print( 'IN LINE: ____________________________-', lineCounter)
    pos = line.find(',')
    x1 = line[:pos]
    #print(x1)

    line = line[pos+1:]
    pos = line.find(' ')

    y1 = line[:pos]
    #print(y1)

    pos = line.find('>')
    line = line[pos + 2:]
    
    pos = line.find(',')
    x2 = line[:pos]

    line = line[pos+1:]
    y2 = line

    x1 = int(x1)
    x2 = int(x2)

    y1 = int(y1)
    y2 = int(y2)
    
    #print('x1:' + x1 + 'y1:' + y1 + 'x2:' + x2 + 'y2:' + y2)   

    if((x1 == x2) or (y1 == y2)):

        if(x1 == x2):
            if(y1 > y2):
                while(y2 <= y1):
                    tempString = x1,',',y2
                    if(not (tempString in coordsList)):
                        coordsList.append(tempString)
                    else:
                        if(not (tempString in doubleList)):
                            counter = counter + 1
                            doubleList.append(tempString)

                    y2 = y2 + 1


            else:
                while(y1 <= y2):
                    tempString = x1,',',y1
                    if(not (tempString in coordsList)):
                        coordsList.append(tempString)
                    else:
                        if(not (tempString in doubleList)):
                            counter = counter + 1
                            doubleList.append(tempString)

                    y1 = y1 + 1

            
            
        else:
            if(y1 == y2):
                if(x1 > x2):
                    while(x2 <= x1):
                        tempString = x2,',',y1
                        if(not (tempString in coordsList)):
                            coordsList.append(tempString)
                        else:
                            if(not (tempString in doubleList)):
                                counter = counter + 1
                                doubleList.append(tempString)

                        x2 = x2 +1

                else:
                    while(x1 <= x2):
                        tempString = x1,',',y1
                        if(not (tempString in coordsList)):
                            coordsList.append(tempString)
                        else:
                            if(not (tempString in doubleList)):
                                counter = counter + 1
                                doubleList.append(tempString)

                        x1 = x1 +1

    #part 2
    else:            
        if( (x1 == y1) and (x2 == y2) ):
            print('found!!!!',lineCounter)
            if(x1 > x2):
                while(x2 <= x1):
                    tempString = x2,',',y2
                    if(not (tempString in coordsList)):
                        coordsList.append(tempString)
                    else:
                        if(not (tempString in doubleList)):
                            counter = counter + 1
                            doubleList.append(tempString)
                    
                    x2 = x2 + 1
                    y2 = y2 + 1
            else:
                while(x1 <= x2):
                    tempString = x1,',',y1
                    if(not (tempString in coordsList)):
                        coordsList.append(tempString)
                    else:
                        if(not (tempString in doubleList)):
                            counter = counter + 1
                            doubleList.append(tempString)
                    
                    x1 = x1 + 1
                    y1 = y1 + 1
            
            
        else:
            #print('FOUND!!', lineCounter)
            if(y1 > y2):
                y1Temp = y1
                y1 = y2
                y2 = y1Temp

                x1Temp = x1
                x1 = x2
                x2  = x1Temp

                if(x1 < x2):
                    while(x1 <= x2):
                        tempString = x1,',',y1
                        if(not (tempString in coordsList)):
                            coordsList.append(tempString)
                        else:
                            if(not (tempString in doubleList)):
                                counter = counter + 1
                                doubleList.append(tempString)

                        x1 = x1 + 1
                        y1 = y1 + 1
                else:
                    while(x2 <= x1):
                        tempString = x2,',',y2
                        if(not (tempString in coordsList)):
                            coordsList.append(tempString)
                        else:
                            if(not (tempString in doubleList)):
                                counter = counter + 1
                                doubleList.append(tempString)

                        x2 = x2 + 1
                        y2 = y2 - 1

            else:
                if(x1 < x2):
                    while(x1 <= x2):
                        tempString = x1,',',y1
                        if(not (tempString in coordsList)):
                            coordsList.append(tempString)
                        else:
                            if(not (tempString in doubleList)):
                                counter = counter + 1
                                doubleList.append(tempString)

                        x1 = x1 + 1
                        y1 = y1 + 1
                else:
                    while(x2 <= x1):
                        tempString = x2,',',y2
                        if(not (tempString in coordsList)):
                            coordsList.append(tempString)
                        else:
                            if(not (tempString in doubleList)):
                                counter = counter + 1
                                doubleList.append(tempString)

                        x2 = x2 + 1
                        y2 = y2 - 1


   

print(counter)