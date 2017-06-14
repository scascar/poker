#!/home/oscar/anaconda3/bin/python3
from card import Card
import logging

class Hand:
	def __init__(self,cards):
		self.cards = 0
		try:
			assert type(cards) is list
			assert len(cards) == 2
			assert type(cards[0]) is Card	
			assert type(cards[1]) is Card	
			assert cards[0].rank != cards[1].rank
			assert cards[0].suit != cards[1].suit

			self.cards = cards

		except AssertionError:
			logging.warning('Error in hand format for variable: '+str(cards))

