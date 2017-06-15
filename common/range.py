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
					self.setPairs(expression)

				elif expression[2] == 's':
					if expression[0] not in self.suited:
						self.suited[expression[0]] = []
					self.suited[expression[0]].append(expression[1])

				elif expression[2] == 'o':
					if expression[0] not in self.offsuit:
						self.offsuit[expression[0]] = []
					self.offsuit[expression[0]].append(expression[1])

			elif len(expression) == 4:
				if expression[2:] == 's+':
					self.setSuited(expression)
				elif expression[2:] == 'o+':
					self.setOffsuit(expression)
					
		self.pairs = sorted(set(self.pairs)) #remove duplicates

	def setPairs(self,expression):
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

	#AT+ 
	def setSuited(self,expression):

		for i in range(Card.getValue(expression[0]),15):
			if Card.getStr(i) not in self.suited:
				self.suited[Card.getStr(i)] = []

			self.suited[Card.getStr(i)].append(Card.getStr(Card.getValue(expression[1])+(i-Card.getValue(expression[0]))))

	def setOffsuit(self,expression):
		for i in range(Card.getValue(expression[0]),15):
			if Card.getStr(i) not in self.offsuit:
				self.offsuit[Card.getStr(i)] = []

			self.offsuit[Card.getStr(i)].append(Card.getStr(Card.getValue(expression[1])+(i-Card.getValue(expression[0]))))
		
	def print(self):
		string = ''
		for i in reversed(range(1,15)):
			for j in reversed(range(1,15)):
				if i == j: #pairs
					if Card.getStr(i) in self.pairs:
						string += Card.getStr(i)+Card.getStr(i)+'  '
					else:
						string += '    '
				else:
				#TO CONTINUE WITH i>J and J<I
					if Card.getStr(i) in self.suited:
						if Card.getStr(j) in self.suited[Card.getStr(i)]:
							string += Card.getStr(i)+Card.getStr(j)+'s ' 
						else:
							string += '    '
					else:
						string += '    '
				else:
					if Card.getStr(i) in self.offsuit:
						if Card.getStr(j) in self.offsuit[Card.getStr(i)]:
							string += Card.getStr(i)+Card.getStr(j)+'o ' 
						else:
							string += '    '
					else:
						string += '    '
			string +='\n'			
		print(string)



				
			
r = Range('22,88,43o,34s')	
print('pairs:',r.pairs)	
print('suited:',r.suited)
print('offsuit',r.offsuit)
r.print()
