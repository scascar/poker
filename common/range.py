#!/home/oscar/anaconda3/bin/python3
import logging
from common.card import Card

class Range:

	def __init__(self,rangeStr):
		self.pairs = []
		self.offsuit = {}
		self.suited = {}
		self.addRange(rangeStr)
		
	#gets pairs, offsuited and suited from like ATs+, 99+, AJs+
	def addRange(self, rangeStr):
		rangeStr = rangeStr.replace(' ','').split(',')
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
					if expression[1] not in self.suited[expression[0]]:
						self.suited[expression[0]].append(expression[1])

				elif expression[2] == 'o':
					if expression[0] not in self.offsuit:
						self.offsuit[expression[0]] = []
					if expression[1] not in self.offsuit[expression[0]]:
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
			for i in range(treshhold,10):
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
		if expression[0] == 'A':
			if 'A' not in self.suited:
				self.suited['A'] = []
			for j in range(Card.getValue(expression[1]),14):
				if Card.getStr(j) not in self.suited['A']:
					self.suited['A'].append(Card.getStr(j))
				
		else:

			for i in range(Card.getValue(expression[0]),15):
				if Card.getStr(i) not in self.suited:
					self.suited[Card.getStr(i)] = []

				if (Card.getStr(Card.getValue(expression[1])+(i-Card.getValue(expression[0])))) not in self.suited[Card.getStr(i)]:
					self.suited[Card.getStr(i)].append(Card.getStr(Card.getValue(expression[1])+(i-Card.getValue(expression[0]))))


	def setOffsuit(self,expression):
		if expression[0] == 'A':
			if 'A' not in self.offsuit:
				self.offsuit['A'] = []
			for j in range(Card.getValue(expression[1]),14):
				if Card.getStr(j) not in self.offsuit['A']:
					self.offsuit['A'].append(Card.getStr(j))
				
		else:

			for i in range(Card.getValue(expression[0]),15):
				if Card.getStr(i) not in self.offsuit:
					self.offsuit[Card.getStr(i)] = []

				if (Card.getStr(Card.getValue(expression[1])+(i-Card.getValue(expression[0])))) not in self.offsuit[Card.getStr(i)]:
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
				elif j < i: #suited 
					if Card.getStr(i) in self.suited:
						if Card.getStr(j) in self.suited[Card.getStr(i)]:
							string += Card.getStr(i)+Card.getStr(j)+'s ' 
						else:
							string += '    '
					else:
						string += '    '
				else:
					if Card.getStr(j) in self.offsuit:
						if Card.getStr(i) in self.offsuit[Card.getStr(j)]:
							string += Card.getStr(j)+Card.getStr(i)+'o ' 
						else:
							string += '    '
					else:
						string += '    '
			string +='\n'			
		print(string)
	
	#MEMO 2652 combos
	# XX 6 combos ( 3 if 1 blocker)
	# XYo 12 combos
	# XYs 4 combos
	# CURRENTLY RETTURNING 1/2x pokerstoves percentage
	def getRangePercentage(self):

		combos = 6*len(self.pairs)
		nb= 0
		for i in self.suited:
			nb+= len(self.suited[i])

		combos += 4*nb

		nb = 0

		for i in self.offsuit:
			nb+= len(self.offsuit[i])
		combos += 12*nb

		print(combos)
		return combos*2/26.52

				
			
#r = Range('22+,AQs+,AKo')
#r.addRange('A2s+')
#r.print()
#print('Range:',r.getRangePercentage())
