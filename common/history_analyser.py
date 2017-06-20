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
		self.filters['stakes'] = []
		self.filters['game'] = []
		self.filters['size'] = []
		self.filters['hand'] = []
		
		
	
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
			
			elif operands[0] == 'stakes':
				for i in range(1, len(operands)):
					self.filters['stakes'].append(operands[i])
			elif operands[0] == 'game':
				for i in range(1, len(operands)):
					self.filters['game'].append(operands[i])
			elif operands[0] == 'size':
				for i in range(1, len(operands)):
					self.filters['size'].append(operands[i])
			elif operands[0] == 'hand':
				pass #TODO
			else:
				logging.warning('Unknown filter for '+filterx)
					
			
	def removeFilter(self,filters):
		pass

	def filterHands(self):	
		for hand in self.data:
			self._filterHand(hand)			

	def _filterHand(self,hand):
			isFiltrate = True	

			# stakes eg. 0.05-0.10
			if self.filters['stakes']:
				if hand['infos']['stakes'] not in self.filters['stakes']:
					return
			# game type eg. NLHE
			if self.filters['game']:
				if hand['infos']['game'] not in self.filters['game']:
					return
			# table size eg. 6-max
			if self.filters['size']:
				if hand['infos']['size'] not in self.filters['size']:
					return
			# currency TODO
			
			# Starting hands
			if self.filters['hand'] and 'cards' in hand:
				if self.hero in hand['cards']:
					if hand['cards'][self.hero][0]+hand['cards'][self.hero][1] not in self.filters['hand']:
						return

		
			# filters on players info (position, name, stack)	
			if 'players' in hand:				
				for player in hand['players']:
				
					# position	
					if self.filters['position']:					
						if player['name'] == self.hero and player['seat'] not in self.filters['position']:
							return
					
												
			self.filtered_data.append(hand)

	def getPlayerStats(self,playerName):
		pass
	def getHeroStats(self):
		pass

if __name__ == '__main__':
	HA = HistoryAnalyser('dump.json')
	HA.setHero('daftReivaX')
	HA.filters['hand'].append('Ad6h')
	HA.filterHands()
	print(HA.filtered_data)
