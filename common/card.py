#/home/oscar/anaconda3/bin/python3
import logging

class Card:


	def __init__(self,card=0):
		self.card = 0
		self.rank = 0
		self.suit = 0

		if card != 0:
			try:
				assert type(card) == str
				assert len(card) == 2
				assert self.isValidCard(card[0]) == True 
				assert self.isValidSuit(card[1]) == True
				self.card = card
				self.setValues()
				
			except AssertionError:
				logging.warning('error in Card format for variable: '+str(card))
					

	def isValidCard(self,char):
		if char in ['A','K','Q','J','T','9','8','7','6','5','4','3','2']:
			return True
		else:
			return False
	
	def isValidSuit(self,char):
		if char in ['s','h','d','c']:
			return True
		else:
			return False
	
	def setValues(self):
		try:
			self.rank = int(self.card[0])
		except:
			if self.card[0] == 'A':
				self.rank = 14
			elif self.card[0] == 'K':
				self.rank = 13
			elif self.card[0] == 'Q':
				self.rank = 12
			elif self.card[0] == 'J':
				self.rank = 11
			elif self.card[0] == 'T':
				self.rank = 10

		if self.card[1] == 's':
			self.suit = 1
		elif self.card[1] == 'h':
			self.suit = 2
		elif self.card[1] == 'c':
			self.suit = 3
		elif self.card[1] == 'd':
			self.suit = 4

	def getStr(value): #static method to get card character
		if value == 14:
			return 'A'
		elif value == 13:
			return 'K'
		elif value == 12:
			return 'Q'
		elif value == 11:
			return 'J'
		elif value == 10:
			return 'T'
		else:
			return str(value)

	def getValue(string):#static: get card value
		if string not in ['A','K','Q','J','T']:
			return int(string)
		elif string == 'A':
			return 14
		elif string == 'K':
			return 13
		elif string == 'Q':
			return 12
		elif string == 'J':
			return 11
		elif string == 'T':
			return 10



