#!/home/oscar/anaconda3/bin/python3
import pprint
import os
import json

class Parser:
	def __init__(self,folder):
		self.folder = folder
	def parseHands(self):
		hands = []
		for filepath in os.listdir(self.folder):
			print('\nopening',filepath)
			with open(self.folder+filepath) as file:
				handText = []
				for line in file:
					if line == '\n':
						if len(handText) >10: 
							hands.append(self.parseHand(handText,filepath))
						handText = []

					else:
						handText.append(line)
		return hands
	def dumpJSON(self,hands,filename):
		with open(filename,'w') as outfile:
			json.dump(hands,outfile)

	def parseHand(self,handText,filename):
		hand = {}

		if '***** Hand History' in handText[0]:
			#hand = self.parseGeneric(handText)
			pass

		elif 'PokerStars' in handText[1]:
			hand = self.parsePokerstars(handText)
				
		elif 'Full Tilt' in handText[0]:
			pass
		else:
			print(handText[0],handText[1],' Implement parsing function :) ')
			
		hand['filename'] = filename
		return hand

	def parsePokerstars(self,handText):
		hand = {}
		hand['infos'] = self.getPokerstarsHandInfos(handText[0:3])
		hand['players'] = self.getPokerstarsHandPlayers(handText[3:])
		hand['actions'] = self.getPokerstarsHandActions(handText[3:])
		hand['board'] = self.getPokerstarsBoard(handText[10:])
		hand['cards'] = self.getPokerstarsPlayerHands(handText[5:])

		return hand
	def getPokerstarsHandActions(self,infos):
		stade = 'PREFLOP'
		actions = {}
		cards = {}
		actions['PREFLOP'] = []
		actions['FLOP'] = []
		actions['TURN'] = []
		actions['RIVER'] = []
		
		for string in infos:
			parsed = string.split(' ')
			if 'posts small' in string:
				action = {}
				action['name'] = parsed[0].replace(':','')
				action['type'] = 'call SB'
				action['amount'] = parsed[-1][1:].replace('\n','')
				actions[stade].append(action)
			elif 'posts big' in string:
				action = {}
				action['name'] = parsed[0].replace(':','')
				action['type'] = 'call BB'
				action['amount'] = parsed[-1][1:].replace('\n','')
				actions[stade].append(action)
			elif '*** HOLE' in string:
				stade = 'PREFLOP'
			elif '*** FLOP' in string:
				stade = 'FLOP'
			elif '*** TURN' in string:
				stade = 'TURN'
			elif '*** RIVER' in string:
				stade = 'RIVER'
			elif 'folds'in string:
				action = {}
				action['name'] = parsed[0].replace(':','')
				action['type'] = 'fold'
				actions[stade].append(action)
			elif 'raises' in string:
				action = {}
				action['name'] = parsed[0].replace(':','')
				action['type'] = 'raises'
				action['amount'] = parsed[-1][1:].replace('\n','')
				actions[stade].append(action)
			elif 'bets' in string:
				action = {}
				action['name'] = parsed[0].replace(':','')
				action['type'] = 'bet'
				action['amount'] = parsed[-1][1:].replace('\n','')
				actions[stade].append(action)
			elif 'checks' in string:
				action = {}
				action['name'] = parsed[0].replace(':','')
				action['type'] = 'check'
				actions[stade].append(action)
			elif 'calls' in string:
				action = {}
				action['name'] = parsed[0].replace(':','')	
				action['type'] = 'call'
				action['amount'] = parsed[-1][1:].replace('\n','')
				actions[stade].append(action)
				
				
				
		return actions

	def getPokerstarsBoard(self,infos):
		board = []	
		for i in infos:
			if 'Board [' in i:
				board+= i[i.index('[')+1:-2].split(' ')
			
		return board
				
	def getPokerstarsPlayerHands(self,infos):
		hands = {}
		for line in infos:
			if 'Dealt to' in line:
				split = line.split(' ')
				hands[split[2]] = [split[3][1:],split[4][:-2]]				
			if 'showed' in line:
				hands[line.split(' ')[2]] = line[line.index('[')+1:line.index(']')].split(' ')
		return hands

	def getPokerstarsHandPlayers(self,infos):
		players = []
		for player in infos:
			if 'Seat' in player:
				pl = {}
				parsed = player.split(' ')
				pl['seat'] = int( parsed[1].replace(':',''))
				pl['name'] = parsed[2]
				pl['stack'] = parsed[3].replace('(','').replace('€','').replace('$','') 
				players.append(pl)
			else:
				return players
		return players
		
	def getPokerstarsHandInfos(self,infos):
		ret = {}
		splitted = infos[0].split(' ')
		if len(splitted) > 5:
			ret['stakes'] = splitted[splitted.index('-')+1].replace('€','').replace('$','')
			ret['currency'] = splitted[splitted.index('-')+3]
			if 'Hold\'em No Limit' in infos[1]:
				ret['game'] = 'NLHE'
			elif 'Omaha' in infos[1]:
				ret['game'] = 'PLO'
			else:
				ret['game'] = 'unknown'

		infos[2] = infos[2].replace('New York','New-York')
		splitted = infos[2].split(' ')
		ret['table'] = splitted[1].replace('\'','')
		ret['size'] = splitted[2]
		ret['buttonSeat'] = splitted[4].replace('#','')
		return ret

	def parseFullTilt(self,handText):
		pass

	def parseGeneric(self,handText):
		hand = {}
		hand['infos'] = self.getGenericHandInfos(handText[1:4])
		return hand

	def getGenericHandInfos(self,infos):
		ret = {}
		stakes = infos[0].split(' ')
		ret['stakes'] = stakes[0]
		del stakes[0]
		ret['currency'] = stakes[1]
		del stakes[1]
		ret['game'] = stakes[2]
		del stakes[2]
		for i in stakes:
			if i != '-':
				ret['game'] += i

		return ret

parser = Parser('../history/')
hands = parser.parseHands()
print(len(hands),'parsed!')
pp = pprint.PrettyPrinter(depth=6)
#for i in range(1,40):
#	pp.pprint( hands[i])
#	print('\n\n')
parser.dumpJSON(hands,'dump.json')

