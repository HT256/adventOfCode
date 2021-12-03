file1 = open('input.txt', 'r')
Lines = file1.readlines()

n = 0
i = 0

liste = []

ones = 0
nulls = 0

gamma = ''
epsilon = ''


while i <= 11:
    
    for line in Lines:

        liste.append(Lines[n][i])
        n += 1


    for x in liste:

        if x == '1':
            ones += 1

        if x == '0':
            nulls += 1

    if ones > nulls:
        gamma = gamma + '1'
        epsilon = epsilon + '0'

    if nulls > ones:
        gamma = gamma + '0'
        epsilon = epsilon + '1'

        
    n = 0
    i += 1
    liste = []
    ones = 0
    nulls = 0
    

print('gamma: ', gamma)
print('epsilon: ', epsilon)

#943 -> gamma
#3152 -> epsilon








