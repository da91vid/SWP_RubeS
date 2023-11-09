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

# def check_paar(pulled_cards):
#     for i in range(len(pulled_cards)):
#         for j in range(len(pulled_cards)):
#             if worth(pulled_cards[i]) == worth(pulled_cards[j]) and i != j:
#                 return True
#     return False

# def check_zwei_paar(pulled_cards):
#     count_paar = 0
#     for i in range(len(pulled_cards)):
#         for j in range(len(pulled_cards)):
#             if worth(pulled_cards[i]) == worth(pulled_cards[j]) and i != j:
#                 count_paar += 1 
#     if count_paar == 4: # weil zb 1 und 13, 13 und 1, 2 und 14, 14 und 2
#         return True
#     return False

# def check_drilling(pulled_cards):
#     for i in range(len(pulled_cards)):
#         matches = 0
#         for j in range(len(pulled_cards)):
#             if worth(pulled_cards[i]) == worth(pulled_cards[j]) and i != j:
#                 matches += 1
#         if matches == 2:
#             return True
#     return False

def check_strase(pulled_cards):
    sorted_cards = sorted(pulled_cards)
    for i in range(len(sorted_cards) - 1):
        if worth(sorted_cards[i]) + 1 != worth(sorted_cards[i + 1]):
            if worth(sorted_cards[4]) == 13 and worth(sorted_cards[0]) == 1:
                ###HIER WEITER
                return False
            return False
    return True

def check_flush(pulled_cards):
    for i in range(len(pulled_cards) - 1):
        if color(pulled_cards[i]) != color(pulled_cards[i + 1]):
            return False
    return True

# def check_full_house(pulled_cards):
#     #return check_drilling(pulled_cards) and check_paar(pulled_cards)
#     #funktioniert nicht weil ein drillig automatisch ein paar ist
#     #return check_drilling(pulled_cards) and check_zwei_paar(pulled_cards)
#     #funktioniert auch nicht weil ein drilling und ein paar nicht als zwei paare gelten
#     if check_drilling(pulled_cards):
#         for i in range(len(pulled_cards)):
#             matches = 0
#             for j in range(len(pulled_cards)):
#                 if worth(pulled_cards[i]) == worth(pulled_cards[j]):
#                     matches += 1
#             if matches == 2:
#                 return True
#     return False

# def check_vierling(pulled_cards):
#     for i in range(len(pulled_cards)):
#         matches = 0
#         for j in range(len(pulled_cards)):
#             if worth(pulled_cards[i]) == worth(pulled_cards[j]) and i != j:
#                 matches += 1
#         if matches == 3:
#             return True
#     return False

def check_straight_flush(pulled_cards):
    return check_strase(pulled_cards) and check_flush(pulled_cards)

def check_royal_flush(pulled_cards):
    return check_straight_flush(pulled_cards) and max(pulled_cards) == 13

# KOMBINATIONEN ÜBERPRÜFEN GESAMMELT

# def check_combination(pulled_cards, dict):
#     if check_paar(pulled_cards):
#         if check_drilling(pulled_cards):
#             dict["drilling"] = dict["drilling"] + 1
#             return dict
#         if check_vierling(pulled_cards):
#             dict["vierling"] = dict["vierling"] + 1
#             return dict
#         if check_full_house(pulled_cards):
#             dict["full_house"] = dict["full_house"] + 1
#             return dict
#         if check_zwei_paar(pulled_cards):
#             dict["zwei_paar"] = dict["zwei_paar"] + 1
#             return dict
#         dict["paar"] = dict["paar"] + 1
#         return dict
#     if check_flush(pulled_cards):
#         if check_straight_flush(pulled_cards):
#             if check_royal_flush(pulled_cards):
#                 dict["royal_flush"] = dict["royal_flush"] + 1
#                 return dict
#             dict["straight_flush"] = dict["straight_flush"] + 1
#             return dict
#         dict["flush"] = dict["flush"] + 1
#         return dict
#     if check_strase(pulled_cards):
#         dict["strase"] = dict["strase"] + 1
#         return dict
#     dict["nix"] = dict["nix"] + 1
#     return dict

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

cards = []
for i in range(1, 53):
    cards.append(i)

dict_true = {"nix":50.1, "paar":42.3, "zwei_paar":4.75, "drilling":2.11, "strase":0.392, "flush":0.197, "full_house":0.144, "vierling":0.24, "straight_flush":0.00139, "royal_flush":0.000154}
dict = {"nix":0, "paar":0, "zwei_paar":0, "drilling":0, "strase":0, "flush":0, "full_house":0, "vierling":0, "straight_flush":0, "royal_flush":0}
ziehungen = 100000

for i in range(0, ziehungen):
    pulled_cards = []
    random.shuffle(cards)
    pulled_cards = cards[:5]
    # for j in range(0, 5):
    #     pulled_cards.append(cards[random.randint(0, 51)])
    dict = check_combis(pulled_cards, dict)
    #print(pulled_cards)


for i in dict:
    dict[i] = (dict[i]*100)/ziehungen

print(dict)
print(dict_true)

# DIAGRAMM

# positionen = []
# hoehe = []
# for i in dict:
#     hoehe.append(dict[i])
#     positionen.append(i)
    
# plt.bar(positionen, hoehe, align = "center")
# #plt.show()