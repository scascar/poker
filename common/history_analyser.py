#!/home/oscar/anaconda3/bin/python3
import logging

#can filter hands by hero position, actions, range,...
class HistoryAnalyser:

	def __init__(self,filename):
		self.data = 0
		self.filtered_data = self.data
		self.filters = {}
		self.filters['position'] = []
	
	def setHero(self,heroName):
		self.hero = heroName

	# example: 'position CU BU CO', 'position CU'
	def addFilter(self,filters):
		parsed = filters.split(',')
		for filterx in parsed:
			operands = filterx.split(' ')
			if operands[0] == 'position':
				for i in range(1,len(operands)):
					if operands[i] == 'EP':
						if 4 not in self.filters['position']:
							self.filters['position'].append(4)
					elif operands[i] == 'MP':
						if 5 not in self.filters['position']:
							self.filters['position'].append(5)
					elif operands[i] == 'CU':
						if 6 not in self.filters['position']:
							self.filters['position'].append(6)
					elif operands[i] == 'BU':
						if 1 not in self.filters['position']:
							self.filters['position'].append(1)
					elif operands[i] == 'SB':
						if 2 not in self.filters['position']:
							self.filters['position'].append(2)
					elif operands[i] == 'BB':
						if 3 not in self.filters['position']:
							self.filters['position'].append(3)
			else:
				logging.warning('Unknown filter for '+filterx)
					
			
	def removeFilter(self,filters):
		pass

	def filterHands(self):
		pass
	def getPlayerStats(self,playerName):
		pass
	def getHeroStats(self):
		pass
