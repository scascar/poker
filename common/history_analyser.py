#!/home/oscar/anaconda3/bin/python3

import logging
import json

#can filter hands by hero position, actions, range,...
class HistoryAnalyser:

	def __init__(self,filename):
		try:
			fjsondump = open(filename)
		except:	
			logging.critical('Can\'t open '+filename+'. Bye Bye !')
			quit()
		self.data = json.loads(fjsondump.read())
		self.filtered_data = []
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
		for hand in self.data:
			isFiltrate = True			
			if 'players' in hand:				
				
				# position	
				if self.filters['position']:					
					for player in hand['players']:
						if player['name'] == self.hero and player['seat'] not in self.filters['position']:
							isFiltrate = False
												
			if isFiltrate:
				self.filtered_data.append(hand)

	def getPlayerStats(self,playerName):
		pass
	def getHeroStats(self):
		pass

if __name__ == '__main__':
	HA = HistoryAnalyser('dump.json')
	HA.setHero('daftReivaX')
	HA.addFilter('position SB BB')
	HA.filterHands()
	#print(HA.filtered_data)
