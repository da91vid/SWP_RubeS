import random
import matplotlib.pyplot as plt

zahlen = 45
ziehungen = 6

def lottoziehung(aufrufe, lottozahlen):
    i = zahlen - 1 - aufrufe
    #print(i)
    index = random.randint(0, i)
        
    lottozahlen[index], lottozahlen[i] = lottozahlen[i], lottozahlen[index]
    
    return lottozahlen[i]

lottozahlen = []
for i in range(zahlen):
    lottozahlen.append(i)

dict = {"Zahl":"Anzahl"}
for i in range(zahlen):
    dict[i+1] = 0

x = input("Ziehungen?")
x = int(x)
for i in range(x):
    for i in range(ziehungen):
        gezogenezahl = lottoziehung(i, lottozahlen)
        dict[gezogenezahl+1] = dict[gezogenezahl+1] + 1

print(dict)

positionen = []
hoehe = []
for i in range(zahlen):
    hoehe.append(dict[i+1])
    positionen.append(i+1)
    
plt.bar(positionen, hoehe, align = "center")
plt.title("Balkendiagramm")
plt.show()
