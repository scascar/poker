#!/home/oscar/anaconda3/bin/python3

from card import Card

class HandEval:
	def __init__(self):
		pass

	#return 1 if h1>h2,-1 if h2>h1, 0 if draw
	def	compareHands(h1,h2):
		hand1 = {}
		hand2 = {}

		for card in h1:
			if card.suit in hand1:
				hand1[card.suit].append(card.rank)
			else:
				hand1[card.suit] = [card.rank]
		for card in h2:
			if card.suit in hand2:
				hand2[card.suit].append(card.rank)
			else:
				hand2[card.suit] = [card.rank]
		print(hand1)


h1 = [Card('As'),Card('Ah'),Card('Ac'),Card('2s'),Card('2h')]
h2 = [Card('Ks'),Card('Kh'),Card('Kc'),Card('Ks'),Card('2c')]

HandEval.compareHands(h1,h2)
		
