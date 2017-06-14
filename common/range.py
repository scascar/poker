#!/home/oscar/anaconda3/bin/python3
import logging
from card import Card

class Range:

	def __init__(self,rangeStr):
		self.pairs = []
		self.offsuit = {}
		self.suited = {}
		self.parseRange(rangeStr)
		
	#gets pairs, offsuited and suited from like ATs+, 99+, AJs+
	def parseRange(self, rangeStr):
		rangeStr = rangeStr.replace(' ','').split(',')
		print(rangeStr)
		for expression in rangeStr:
			if len(expression) == 2: 
				if expression[0] == expression[1]:
					self.pairs.append(expression[0])
			elif len(expression) == 3:
				if expression[0] == expression[1] and expression[2] == '+':
					self.getPairs(expression)
					
		self.pairs = sorted(set(self.pairs)) #remove duplicates

	def getPairs(self,expression):
		try:
			treshhold = int(expression[0])
			for i in range(treshhold,9):
				self.pairs.append(str(i))
			self.pairs += ['T','J','Q','K','A']

		except:
			if expression[0] == 'T':
				self.pairs += ['T','J','Q','K','A']
			elif expression[0] == 'J':
				self.pairs += ['J','Q','K','A']
			elif expression[0] == 'Q':
				self.pairs += ['Q','K','A']
			elif expression[0] == 'K':
				self.pairs += ['K','A']
			elif expression[0] == 'A':
				self.pairs += ['A']

	#ATo+ 
	def getSuited(self,expression):
		if expression[0] not in self.suited:
			self.suited[expression[0]] = []

		for i in range(Card.getValue(expression[
		self.suited[expression[0]].append(expression[1])

	
		
	def print(self):
		pass	



				
			
r = Range('QQ+,22,88,99,TT,AA')	
print(r.pairs)	
