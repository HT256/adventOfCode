
def main():
        
    file = open('input.txt', 'r')
    line = file.readline()
    file.close()

    positions = line.split(',')

    i = 0
    for position in positions:
        positions[i] = int(position)
        i = i + 1


    # positions are now integer

    listOfFuel = []

    fuel = 0
    i = 0

    max_pos = max(positions)
    min_pos = min(positions)

    addedUp = sum(positions)
    length = len(positions)
    average = addedUp / length

    print(average)

    n = min_pos

    i = 0
    first = True
    while(n <= max_pos):
        for position in positions:
            if(first):
                listOfFuel.append(moveTo(n, position))
                first = False
            else:
                listOfFuel[i] = listOfFuel[i] + moveTo(n, position)
            
        first = True
        i = i + 1
        n = n + 1
        print(n)

    print(min(listOfFuel))


def moveTo(goalPos, currPos): 
    num = abs(currPos - goalPos)
    i = 1
    n = 0

    while(i <= num):
        n = n + i
        i = i + 1

    return n


main()