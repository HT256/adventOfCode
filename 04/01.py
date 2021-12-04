file1 = open('numbers_input.txt', 'r')
lNumbers = file1.readlines()

file2 = open('boards_input.txt', 'r')
preBoards = file2.readlines()


numbers = ''
numbers = numbers.join(lNumbers)
numbers = list(numbers.split(","))

#######VORBEREITUNG DER SPIELFELDER

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


n = 0
x = 0
y = 0
z = 0

a = 0
b = 0
c = 0
d = 'Test'
    

for x in numbers:
    
    while y <= 99:


        for i in range(5):
            for z in range(5):
                
                if boards[y][i][z] == x:
                    boards[y][i][z] = '*'

        y += 1


    #check if won
    y = 0
    i = 0
    z = 0

    while y <= 99:
        
        for i in range(5):
                if boards[y][i][z] == '*' and boards[y][i][z+1] == '*' and boards[y][i][z+2] == '*' and boards[y][i][z+3] == '*' and boards[y][i][z+4] == '*':
                    print('WINNER: ', boards[y])
                    print(x)
                    print('y: ', y)
                    d = input()

        i = 0
        z = 0

        for z in range(5):
                if boards[y][i][z] == '*' and boards[y][i+1][z] == '*' and boards[y][i+2][z] == '*' and boards[y][i+3][z] == '*' and boards[y][i+4][z] == '*':
                    print('WINNER: ', boards[y])
                    print(x)
                    print('y: ', y)
                    d = input()

        i = 0
        z = 0
        y += 1
        
    y = 0

                
    
        
        
        


    


