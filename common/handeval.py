#!/home/oscar/anaconda3/bin/python3

from card import Card

class HandEval:
	def __init__(self):
		pass

	#return 1 if h1>h2,-1 if h2>h1, 0 if draw
	def	compareHands(toEval):
		hands = [{},{}]
		duplicates = [{},{}]

		#get suits
		for i in range(0,2):
			for card in toEval[i]:
				if card.suit in hands[i]:
					hands[i][card.suit].append(card.rank)
				else:
					hands[i][card.suit] = [card.rank]

			
		#get duplicates
		for i in range(0,2):
			for suit in hands[i]:
				for rank in hands[i][suit]:
					if rank in duplicates[i]:
						duplicates[i][rank] += 1
					else:
						duplicates[i][rank] = 1



		print(hands)
	
	#gets the duplicates as arguments, return the card high straight
	def hasStraight(values):
		temp = []
	
		for k in values:
			temp.append(k)

		if 5 in temp or 10 in temp:
			temp = sorted(temp)
		if 13 in temp:
			pass

			return 0
		
		else:
			return 0
			
		
#USING PSTOVE INSTEAD	


h1 = [Card('As'),Card('Ah'),Card('Ac'),Card('2s'),Card('2h')]
h2 = [Card('Ks'),Card('Kh'),Card('Kc'),Card('Ks'),Card('2c')]

HandEval.compareHands([h1,h2])
		
