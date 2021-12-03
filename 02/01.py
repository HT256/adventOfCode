file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
n = 0

hpos = 0
depth = 0

for line in Lines:

    if Lines[n][0] == 'u':
        depth = depth - int(Lines[n][3])
        #print(int(Lines[n][3]))
        

    if Lines[n][0] == 'd':
        depth = depth + int(Lines[n][5])
        #print(int(Lines[n][5]))


    if Lines[n][0] == 'f':
        hpos = hpos + int(Lines[n][8])
        #print(int(Lines[n][8]))
   
    
    count += 1
    n += 1
    

print('hpos: ', hpos)
print('depth: ', depth)








