#author: Florian Wolf
#date: 05.11.2016

# coding: utf8

import math

j = 0 #Zaehler fuer die Rechenschritte
k = 0 #Zahler um die hoechste Anzahl an Schritten festzustellen

#Obere und untere Grenze eingeben
for i in range(1,20):
    l = i #Zaehler fuer den Index der Zahl, relevant fuer die untere if-Bedingung
    print("Die Zahl lautet: " + str(l)+ "\n")
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
        n = j
        print("Die Zahl ist geschafft!")
        print("Benoetigte Schritte: "+  str(j) + "\n")
        if n > k:
            k = n
            q = l #Zaehler fuer den Index der hoechsten Schrittanzahl
        else:
            print("")
        j = 0
print("Die hoechste Anzahl an Schritten lautet " + str(k) + " bei Zahl mit der Nummer " + str(q) + ".")
