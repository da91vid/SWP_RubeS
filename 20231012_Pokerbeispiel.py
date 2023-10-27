cards = []
for i in range(1, 53):
    cards.append(i)

def find_color(card):
    return card // 13
def find_card_to_color(card, color):
    return (card % color) + 1

card = cards[38]
print(find_color(card))
print(find_card_to_color(card, find_color(card)))