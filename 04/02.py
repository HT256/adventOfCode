file1 = open('numbers_input.txt', 'r')
lNumbers = file1.readlines()

file2 = open('boards_input.txt', 'r')
preBoards = file2.readlines()


numbers = ''
numbers = numbers.join(lNumbers)
numbers = list(numbers.split(","))


# multidimensional arrays in python = hunde
boards = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

n = 0
x = 0
y = 0

for line in preBoards:
    x += 1
    
    if (x % 6) != 0:
        line = " ".join(line.split())
        line = line.replace(" ", ",")
        line = list(line.split(","))
        boards[n].append(line)

    else:
        n += 1

# :^)



x = 0
y = 0
z = 0


gameover = False

while gameover == False:

    for x in numbers:
              
        while y < len(boards):


            for i in range(5):
                for z in range(5):
                    if boards[y][i][z] == x:
                        boards[y][i][z] = '*'
            y += 1


        y = 0
        i = 0
        z = 0

        while y < len(boards):
        
            for i in range(5):
                    if boards[y][i][z] == '*' and boards[y][i][z+1] == '*' and boards[y][i][z+2] == '*' and boards[y][i][z+3] == '*' and boards[y][i][z+4] == '*':
                        if len(boards) != 1:
                            del boards[y]
                            i = 0
                            z = 0
                            y = 0
                        if len(boards) == 1:
                            print(boards)
                            print(x)

            i = 0
            z = 0

            for z in range(5):
                    if boards[y][i][z] == '*' and boards[y][i+1][z] == '*' and boards[y][i+2][z] == '*' and boards[y][i+3][z] == '*' and boards[y][i+4][z] == '*':
                        if len(boards) != 1:
                            del boards[y]
                            i = 0
                            z = 0
                            y = 0
                        if len(boards) == 1:
                            print(boards)
                            print(x)

            i = 0
            z = 0
            y += 1
        
        y = 0

        

                
    
        
        
        


    


