import random
import matplotlib.pyplot as plt

def lottoziehung(aufrufe, lottozahlen):
    i = 44 - aufrufe
    #print(i)
    index = random.randint(0, i)
        
    gezogenezahl = lottozahlen[index]
    lottozahlen[index] = lottozahlen[i]
    lottozahlen[i] = gezogenezahl
    
    return gezogenezahl

lottozahlen = []
for i in range(45):
    lottozahlen.append(i)

dict = {"Zahl":"Anzahl"}
for i in range(46):
    dict[i] = 0

x = input("Ziehungen?")
x = int(x)
for i in range(x):
    for i in range(6):
        gezogenezahl = lottoziehung(i, lottozahlen)
        dict[gezogenezahl] = dict[gezogenezahl] + 1

print(dict)

positionen = []
hoehe = []
for i in range(45):
    hoehe.append(dict[i])
    positionen.append(i+1)
    
plt.bar(positionen, hoehe, align = "center")
plt.title("Balkendiagramm")
plt.show()
