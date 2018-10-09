import random
import pyCardDeck as myDeck
from pyCardDeck.cards import PokerCard
cards=[] #stores the deck created
player_lst=[] #list of total no of players is stored
x=int(input("enter no of player:")) #total input of people playing
class myException:
	def __init__(self,msg):
		print(msg)
if x <=9:
	for i in range(x):
		player_lst.append([])
else:
	""" As per standard rule 9 players are allowed except some private poker tables """

	raise myException("___MAX 9 PLAYERS CAN PLAY___") 
def Deck_initial_stage():

	""" Deck is Created  """

	shapes=['Clubs','Spades','Diamonds','Hearts']
	ranks={'1': 'one','2': 'Two','3': 'Three','4': 'Four','5': 'Five','6':'six','7': 'Seven','8': 'Eight','9': 'Nine','10': 'Ten','Jack': 'Jack','Q': 'Queen','K': 'King'}
	for shape in shapes:
		for i,j in ranks.items():
			cards.append((shape,j))
			#cards.append(i)
			#cards.append(j)
	return(cards)
deck=myDeck.Deck(Deck_initial_stage())

def Draw():

	""" cards are drawn to the players one at a time  """

	for i in range(5):
		for players in player_lst:
			deck.shuffle()
			players.append(deck.draw())
	print(player_lst)
Draw()

player1=player_lst[0]
player2=player_lst[1]
print(player1)
print(player2)

def remove_card(temp,index):

	""" removes the card that player wishes  """
	del temp[index]


def card_took(player_no):

	""" add a random card to the hand """
	deck.shuffle()
	player_no.append(deck.draw())

def add_and_remove(player_lst):

	""" players drawing new card from deck max 20 draws allowed  """

	counter=0
	
	for i in range(0,20):
		condition=input("DO YOU WANNA DRAW CARDS FROM DECK:Y/N??")
		if condition=="y":


			for players in player_lst:
				counter+=1
				print("PLAYER",counter%2)
				temp=input("Do you want to choose new card?y/n")
				#var1=int(input("enter the index of card you wanna remove: "))
				if temp == 'y':
					var1=int(input("Enter the index of card you wanna remove: "))
					remove_card(players,var1)
					card_took(players)
					print(players)
				else:
					return
	
		else:
			return None
add_and_remove(player_lst)
