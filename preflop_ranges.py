#!/home/oscar/anaconda3/bin/python3
from common.range import Range
from common.hand import Hand
from common.card import Card
from pprint import pprint
import json

#with open('lightdump.json') as data_file:
with open('dump.json') as data_file:
	data = json.load(data_file)

values = []
for i in data:
	if 'infos' in i:
		if 'currency' in i['infos']:
			if i['infos']['currency'] not in values:
				values.append(i['infos']['currency'])
			if '0,' in i['infos']['currency'] :
				print(i['filename'])
		

print('Stakes parsed:',values)

	

ranges = [Range(''),Range(''),Range(''),Range('')]
probas = [{},{},{},{}]
parsedHands = 0
for hand in data:
	if 'players' in hand:
		parsedHands += 1
		for player in hand['players']:
			if player['name'] == 'daftReivaX' and player['seat'] in [4,5,6,1]:
				ind = (player['seat']-4)%6
				for action in hand['actions']['PREFLOP']:
					if action['name'] == 'daftReivaX' and action['type'] == 'raises':
						h = Hand([Card(hand['cards']['daftReivaX'][0]),Card(hand['cards']['daftReivaX'][1])])  
						h = h.getStandardNotation()
						if h not in probas[ind]:
							probas[ind][h] = 0
						probas[ind][h] += 1	
					elif action['name'] == 'daftReivaX' and action['type'] == 'fold':
						h = Hand([Card(hand['cards']['daftReivaX'][0]),Card(hand['cards']['daftReivaX'][1])])  
						h = h.getStandardNotation()
						if h not in probas[ind]:
							probas[ind][h] = 0
						probas[ind][h] -= 1	
						

for idx,proba in enumerate(probas):
	for hand in proba:
		if proba[hand] > 0:
			ranges[idx].addRange(hand)
print('\n\n\n',parsedHands,'hands parsed:')
print('\n\nEP range:')
ranges[0].print()
print('\n\nMP range:')
ranges[1].print()
print('\n\nCU range:')
ranges[2].print()
print('\n\nBU range:')
ranges[3].print()
