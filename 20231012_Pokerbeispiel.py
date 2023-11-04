import random
import matplotlib.pyplot as plt

# FARBE UND KARTE FINDEN

def color(card):
    if card % 13 == 0:
        return card // 14 #stimmt nicht immer aber in unserem fall schun
    return card // 13
         
def worth(card):
    if card % 13 == 0:
        return 13
    return card % 13

# KOMBINATIONEN ÜBERPRÜFEN

def check_paar(pulled_cards):
    for i in range(len(pulled_cards)):
        for j in range(len(pulled_cards)):
            if worth(pulled_cards[i]) == worth(pulled_cards[j]) and i != j:
                return True
    return False

def check_zwei_paar(pulled_cards):
    count_paar = 0
    for i in range(len(pulled_cards)):
        for j in range(len(pulled_cards)):
            if worth(pulled_cards[i]) == worth(pulled_cards[j]) and i != j:
                count_paar += 1 
    if count_paar == 4: # weil zb 1 und 13, 13 und 1, 2 und 14, 14 und 2
        return True
    return False

def check_drilling(pulled_cards):
    for i in range(len(pulled_cards)):
        matches = 0
        for j in range(len(pulled_cards)):
            if worth(pulled_cards[i]) == worth(pulled_cards[j]) and i != j:
                matches += 1
        if matches == 2:
            return True
    return False

def check_strase(pulled_cards):
    sorted_cards = sorted(pulled_cards)
    for i in range(len(sorted_cards) - 1):
        if worth(sorted_cards[i]) + 1 != worth(sorted_cards[i + 1]):
            return False
    return True

def check_flush(pulled_cards):
    for i in range(len(pulled_cards) - 1):
        if color(pulled_cards[i]) != color(pulled_cards[i + 1]):
            return False
    return True

def check_full_house(pulled_cards):
    #return check_drilling(pulled_cards) and check_paar(pulled_cards)
    #funktioniert nicht weil ein drillig automatisch ein paar ist
    #return check_drilling(pulled_cards) and check_zwei_paar(pulled_cards)
    #funktioniert auch nicht weil ein drilling und ein paar nicht als zwei paare gelten
    if check_drilling(pulled_cards):
        for i in range(len(pulled_cards)):
            matches = 0
            for j in range(len(pulled_cards)):
                if worth(pulled_cards[i]) == worth(pulled_cards[j]) and i != j:
                    matches += 1
            if matches == 2:
                return True
    return False

def check_vierling(pulled_cards):
    for i in range(len(pulled_cards)):
        matches = 0
        for j in range(len(pulled_cards)):
            if worth(pulled_cards[i]) == worth(pulled_cards[j]) and i != j:
                matches += 1
        if matches == 3:
            return True
    return False

def check_straight_flush(pulled_cards):
    return check_strase(pulled_cards) and check_flush(pulled_cards)

def check_royal_flush(pulled_cards):
    return check_straight_flush(pulled_cards) and max(pulled_cards) == 13

# KOMBINATIONEN ÜBERPRÜFEN GESAMMELT

def check_combination(pulled_cards, dict):
    if check_paar(pulled_cards):
        if check_drilling(pulled_cards):
            if check_vierling(pulled_cards):
                dict["vierling"] = dict["vierling"] + 1
                return dict
            if check_full_house(pulled_cards):
                dict["full_house"] = dict["full_house"] + 1
                return dict
            dict["drilling"] = dict["drilling"] + 1
            return dict
        if check_zwei_paar(pulled_cards):
            dict["zwei_paar"] = dict["zwei_paar"] + 1
            return dict
        dict["paar"] = dict["paar"] + 1
        return dict
    if check_flush(pulled_cards):
        if check_straight_flush(pulled_cards):
            if check_royal_flush(pulled_cards):
                dict["royal_flush"] = dict["royal_flush"] + 1
                return dict
            dict["straight_flush"] = dict["straight_flush"] + 1
            return dict
        dict["flush"] = dict["flush"] + 1
        return dict
    if check_strase(pulled_cards):
        dict["strase"] = dict["strase"] + 1
        return dict
    dict["nix"] = dict["nix"] + 1
    return dict

# MAIN

cards = []
for i in range(1, 53):
    cards.append(i)

dict = {"nix":0, "paar":0, "zwei_paar":0, "drilling":0, "strase":0, "flush":0, "full_house":0, "vierling":0, "straight_flush":0, "royal_flush":0,}
ziehungen = 100000

for i in range(0, ziehungen-1):
    pulled_cards = []
    for j in range(0, 5):
        pulled_cards.append(cards[random.randint(0, 51)])
    dict = check_combination(pulled_cards, dict)

for i in dict:
    dict[i] = (dict[i]*100)/ziehungen

print(dict)

# DIAGRAMM

positionen = []
hoehe = []
for i in dict:
    hoehe.append(dict[i])
    positionen.append(i)
    
plt.bar(positionen, hoehe, align = "center")
plt.show()