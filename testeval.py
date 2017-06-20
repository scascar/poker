#!/home/oscar/anaconda3/bin/python3


import eval7
from pprint import pprint

deck = eval7.Deck()
deck.shuffle()
hand = deck.deal(5)
pprint(hand)
print(eval7.evaluate(hand))

