import random
import pyCardDeck as myDeck
from pyCardDeck.cards import PokerCard
cards=[]

player_1=[]

def Deck_initial_stage():
	shapes=['Clubs','Spades','Diamonds','Hearts']
	ranks={'1': 'one','2': 'Two','3': 'Three','4': 'Four','5': 'Five','6':'six','7': 'Seven','8': 'Eight','9': 'Nine','10': 'Ten','Jack': 'Jack','Q': 'Queen','K': 'King'}
	for shape in shapes:
		for i,j in ranks.items():
			cards.append((shape,j))
			#cards.append(i)
			#cards.append(j)
	return(cards)
deck=myDeck.Deck(Deck_initial_stage())


for i in range(5):
	player_1.append(deck.draw())
print(player_1)
