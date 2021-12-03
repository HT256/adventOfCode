file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
n = 0

for line in Lines:
    if n < 1997 :
        print(int(line))
        sum1 = int(Lines[n]) + int(Lines[n+1]) + int(Lines[n+2])
        sum2 = int(Lines[n+1]) + int(Lines[n+2]) + int(Lines[n+3])
        
        if sum1 < sum2 :
            count += 1

    n += 1
    

print(count)








