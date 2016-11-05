#author: Florian Wolf
#date: 05.11.2016

# coding: utf8

import math

j = 0 #Zaehler fuer die Rechenschritte

#Obere und untere Grenze eingeben
for i in range(2,7):
    print("Die Zahl lautet: " + str(i)+ "\n")
    while i !=1:
        if math.fmod(i, 2) == 0:
            i = i/2
            print(i)
            j += 1
        else:
            i = (3*i+1) / 2
            print(i)
            j += 1
    else:
        print("Die Zahl ist geschafft!")
        print("Benötigte Schritte:"+  str(j) + "\n")
        j = 0
