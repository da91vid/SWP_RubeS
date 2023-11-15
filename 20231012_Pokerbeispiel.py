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

def check_strase(pulled_cards):
    for i in range(len(pulled_cards)):
        pulled_cards[i] = worth(pulled_cards[i])
    sorted_cards = sorted(pulled_cards)
    if sorted_cards[4] == 13:
        if sorted_cards[0] == 1:
            i = 0
            while sorted_cards[i] + 1 == sorted_cards[i+1]:
                i = i+1 
            j = 4
            while sorted_cards[j] - 1 == sorted_cards[j-1]:
                j = j-1
            z = (i+1) + (5-j)
            if z == 5:
                return True
    for i in range(len(sorted_cards) - 1):
        if sorted_cards[i] + 1 != sorted_cards[i + 1]:
            return False
    return True

def check_flush(pulled_cards):
    for i in range(len(pulled_cards) - 1):
        if color(pulled_cards[i]) != color(pulled_cards[i + 1]):
            return False
    return True

def check_straight_flush(pulled_cards):
    return check_strase(pulled_cards) and check_flush(pulled_cards)

def check_royal_flush(pulled_cards):
    if check_straight_flush(pulled_cards):
        for i in range(len(pulled_cards)):
            pulled_cards[i] = worth(pulled_cards[i])
        if sorted(pulled_cards) == [0,10,11,12,13]:
            return True
    return False

# KOMBINATIONEN ÜBERPRÜFEN GESAMMELT

def check_combis(pulled_cards, dict):
    matches = [0,0,0,0,0]
    for i in range(len(pulled_cards)):
        for j in range(len(pulled_cards)):
            if worth(pulled_cards[i]) == worth(pulled_cards[j]):
                matches[i] = matches[i] + 1
    matches = sorted(matches)
    #print(matches)
    if check_flush(pulled_cards):
        if check_straight_flush(pulled_cards):
            if check_royal_flush(pulled_cards):
                dict["royal_flush"] = dict["royal_flush"] + 1
                return dict
            dict["straight_flush"] = dict["straight_flush"] + 1
            return dict
        dict["flush"] = dict["flush"] + 1
        return dict
    if matches == [1,4,4,4,4]:
            dict["vierling"] = dict["vierling"] + 1
            return dict
    if matches == [2,2,3,3,3]:
            dict["full_house"] = dict["full_house"] + 1
            return dict
    if check_strase(pulled_cards):
        dict["strase"] = dict["strase"] + 1
        return dict
    if matches == [1,1,3,3,3]:
        dict["drilling"] = dict["drilling"] + 1
        return dict
    if matches == [1,2,2,2,2]:
        dict["zwei_paar"] = dict["zwei_paar"] + 1
        return dict
    if matches == [1,1,1,2,2]:
        dict["paar"] = dict["paar"] + 1
        return dict
    dict["nix"] = dict["nix"] + 1
    return dict

# MAIN

def main():
    cards = []
    for i in range(1, 53):
        cards.append(i)

    dict_true = {"nix":50.1, "paar":42.3, "zwei_paar":4.75, "drilling":2.11, "strase":0.392, "flush":0.197, "full_house":0.144, "vierling":0.024, "straight_flush":0.00139, "royal_flush":0.000154}
    dict = {"nix":0, "paar":0, "zwei_paar":0, "drilling":0, "strase":0, "flush":0, "full_house":0, "vierling":0, "straight_flush":0, "royal_flush":0}
    ziehungen = 100000

    for i in range(0, ziehungen):
        pulled_cards = []
        random.shuffle(cards)
        pulled_cards = cards[:5]
        dict = check_combis(pulled_cards, dict)


    for i in dict:
        dict[i] = (dict[i]*100)/ziehungen

    print("meine Werte")
    print(dict)
    print("\nkorekte Werte:")
    print(dict_true)

if __name__ == '__main__':
    main()
    
# DIAGRAMM

# positionen = []
# hoehe = []
# for i in dict:
#     hoehe.append(dict[i])
#     positionen.append(i)
    
# plt.bar(positionen, hoehe, align = "center")
# #plt.show()