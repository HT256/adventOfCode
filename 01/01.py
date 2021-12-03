file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
n = 1

for line in Lines:
    print(int(line))

    if n < 2000 and int(Lines[n]) > int(Lines[n-1]) :
        count += 1

    n += 1
    

print(count)








