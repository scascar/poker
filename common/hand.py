#!/home/oscar/anaconda3/bin/python3
from common.card import Card
import logging

class Hand:
	def __init__(self,cards):
		self.cards = 0
		try:
			assert type(cards) is list
			assert len(cards) == 2
			assert isinstance(cards[0],Card)	
			assert isinstance(cards[1],Card)	
			assert cards[0].rank != cards[1].rank or cards[0].suit != cards[1].suit

			self.cards = cards

		except AssertionError:
			logging.warning('Error in hand format for variable: '+str(cards))

	def getStandardNotation(self):
		if type(self.cards) is list:
			if self.cards[0].rank > self.cards[1].rank:
				ret = Card.getStr(self.cards[0].rank)+Card.getStr(self.cards[1].rank)
				if self.cards[0].suit == self.cards[1].suit:
					ret += 's'
				else:
					ret += 'o'
			else:
				ret = Card.getStr(self.cards[1].rank)+Card.getStr(self.cards[0].rank)

			return ret
		else:
			return 'Error in Hand.getStandardNotation'


