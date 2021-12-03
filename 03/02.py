file1 = open('input.txt', 'r')
Lines = file1.readlines()

n = 0
i = 0

liste = []
sListe = []
dListe = []

ones = 0
nulls = 0

oxygen = ''
co2 = ''

for line in Lines:
    line.strip
    dListe.append(line[:-1])


while i <= 11:

    print('ANFANG: ', i);
    for line in dListe:
        liste.append(dListe[n][i])
        n += 1
   
    
    for x in liste:

        if x == '1':
            ones += 1

        if x == '0':
            nulls += 1


    if ones >= nulls:
        for line in dListe:
            if line[i] == '1':              #for oxygen: if line[i] == '1':
                sListe.append(line)         #for co2: if line[i] == '0':

                
    if nulls > ones:
        #print('nulls > ones')
        for line in dListe:
            if line[i] == '0':              #for oxygen: if line[i] == '0':
                sListe.append(line)         #for co2: if line[i] == '1':


    if len(sListe) == 1:
        print('jo')
        oxygen = sListe[0]
        i = 12

    n = 0
    i = i + 1
    dListe = sListe
    sListe = []
    liste = []
    ones = 0
    nulls = 0      

    
print('oxygen: ', oxygen)

#oxy = 001110100011 - 931
#co2 = 111000100010 - 3618

#2976108










