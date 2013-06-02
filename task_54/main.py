str2val = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, 'T':8, 'J':9, 'Q':10, 'K':11, 'A':12}
str2suit = {'S':0, 'D':1, 'H':3, 'C':4}

class HandRank:
	hand = []
	score = []
	
	def __init__(self, str):
		self.hand = self._str2hand(str)

	def _str2hand(self, str):
		hand = [(str2val[card[0]], str2suit[card[1]]) for card in str.split(' ')]
		hand.sort(key=lambda x: x[0])
		return hand

	def _testflush(self):
		h = self.hand
		suit = h[0][1]
		for card in h[1:]:
			if suit != card[1]:
				return False
		self.score = [x[0] for x in h[::-1]]
		return True
		
	def _teststraight(self):
		h = self.hand
		lastval = h[0][0]
		for card in h[1:-1]:
			if card[0] - lastval != 1:
				return False
			lastval = card[0]
		if h[-1][0] - lastval == 1:
			self.score = [h[-1][0],]
			return True
		if h[0][0] == 0 and h[-1][0] == 12:
			self.score = [h[-2][0],]
			return True
		
	def _testquad(self):
		h = self.hand
		if h[1][0] == h[4][0]:
			self.score = [h[1][0], h[0][0]]
			return True
		if h[0][0] == h[3][0]:
			self.score = [h[0][0], h[4][0]]
			return True
		return False
		
	def _testfullhouse(self):
		h = self.hand
		if h[0][0] == h[1][0] and h[3][0] == h[4][0]:
			if h[2][0] == h[0][0]:
				self.score = [h[0][0], h[3][0]]
				return True
			if h[2][0] == h[3][0]:
				self.score = [h[3][0], h[0][0]]
				return True
		return False

	def _test3oak(self):
		h = self.hand
		s = 0
		for i in range(1, 5):
			if h[i][0] == h[s][0]:
				if i - s + 1 == 3:
					if i == 2:
						self.score = [h[2][0], h[4][0], h[3][0]]
					elif i == 3:
						self.score = [h[3][0], h[4][0], h[0][0]]
					elif i == 4:
						self.score = [h[4][0], h[1][0], h[0][0]]
					return True
			else:
				s = i
		return False
	
	def _test2pair(self):
		h = self.hand
		vals = [0] * 14
		for card in h:
			vals[card[0] + 1] += 1
		p1, p2, k = 0, 0, 0
		for i in range(1, 14):
			if vals[i] == 2:
				if not p1:
					p1 = i
				else:
					p2 = i
			if vals[i] == 1:
				k = i
		if p1 and p2:
			self.score = [p2 - 1, p1 - 1, k - 1]
			return True
		return False
		
	def _testpair(self):
		h = self.hand
		vals = [0] * 14
		for card in h:
			vals[card[0] + 1] += 1
		p, k1, k2, k3 = 0, 0, 0, 0
		for i in range(1, 14):
			if vals[i] == 2:
				p = i
			if vals[i] == 1:
				if not k1:
					k1 = i
				elif not k2:
					k2 = i
				elif not k3:
					k3 = i
		if p and k1 and k2 and k3:
			self.score = [p - 1, k3 - 1, k2 - 1, k1 - 1]
			return True
		return False
	
	def _testother(self):
		self.score = [x[0] for x in self.hand[::-1]]
		return True
	
	def comb(self):
		isflush = self._testflush()
		isstraight = self._teststraight()
		res = 0;
		
		if isflush and isstraight:
			res = 9
		elif self._testquad():
			res = 8
		elif self._testfullhouse():
			res = 7
		elif isflush:
			res = 6
		elif isstraight:
			res = 5
		elif self._test3oak():
			res = 4
		elif self._test2pair():
			res = 3
		elif self._testpair():
			res = 2
		elif self._testother():
			res = 1
		return [res] + self.score
	
def cmphands(h1, h2):
	s1, s2 = HandRank(h1).comb(), HandRank(h2).comb()
	for s in zip(s1, s2):
		if s[0] < s[1]:
			return -1
		elif s[0] > s[1]:
			return 1
	return 0
	
def test():
	handrank = HandRank('AH KD 2S 3S 6S')
	isquad = handrank._testquad()
	print isquad, handrank.score
	
	handrank = HandRank('AH AD 2S AS AC')
	isquad = handrank._testquad()
	print isquad, handrank.score
	
	handrank = HandRank('2H 2D AS 2S 2C')
	isquad = handrank._testquad()
	print isquad, handrank.score
	
	handrank = HandRank('2S 6D 4S 5S 3C')
	isstraight = handrank._teststraight()
	print isstraight, handrank.score
	
	handrank = HandRank('2S 6D 4S 5S 3C')
	isstraight = handrank._teststraight()
	print isstraight, handrank.score
	
	handrank = HandRank('2S AD 4S 5S 3C')
	isstraight = handrank._teststraight()
	print isstraight, handrank.score
	
	handrank = HandRank('2S AD 4S 6S 3C')
	isstraight = handrank._teststraight()
	print isstraight, handrank.score
	
	handrank = HandRank('2H AH 4H 6H 3H')
	isflush = handrank._testflush()
	print isflush, handrank.score
	
	handrank = HandRank('2H 2S 4S 4D 4C')
	isfullhouse = handrank._testfullhouse()
	print isfullhouse, handrank.score
	
	handrank = HandRank('2H 4S 2C 4D 2C')
	isfullhouse = handrank._testfullhouse()
	print isfullhouse, handrank.score
	
	handrank = HandRank('2H 4S 2C 4D 3C')
	isfullhouse = handrank._testfullhouse()
	print isfullhouse, handrank.score
	
	handrank = HandRank('2H 4S 2C 4D AC')
	isfullhouse = handrank._testfullhouse()
	print isfullhouse, handrank.score
	
	handrank = HandRank('2H 4S 2C 2D AC')
	is3oak = handrank._test3oak()
	print is3oak, handrank.score
	
	handrank = HandRank('5H 4S 5C 5D AC')
	is3oak = handrank._test3oak()
	print is3oak, handrank.score
	
	handrank = HandRank('AH 4S AC AD KC')
	is3oak = handrank._test3oak()
	print is3oak, handrank.score
	
	handrank = HandRank('AH AS KC KD 2C')
	is2pair = handrank._test2pair()
	print is2pair, handrank.score
	
	handrank = HandRank('2H AS KC KD 2C')
	is2pair = handrank._test2pair()
	print is2pair, handrank.score
	
	handrank = HandRank('2H QS KC JD 2C')
	is2pair = handrank._test2pair()
	print is2pair, handrank.score
	
	handrank = HandRank('2H QS KC JD 2C')
	ispair = handrank._testpair()
	print ispair, handrank.score
	
	handrank = HandRank('2H QS 2C JD 2C')
	ispair = handrank._testpair()
	print ispair, handrank.score
	
	handrank = HandRank('TH QS 3C JD 2C')
	ispair = handrank._testpair()
	print ispair, handrank.score
	
	print cmphands('AH KS QD JD TD', '2D 5D 6D JD 7D')
	print cmphands('AS KS QS JS TS', '2D 5D 6D JD 7D')
	print cmphands('AS AD AH JS JD', 'AS JH AD AH JD')
	
test()

p1count = 0
for line in open('poker.txt', 'r'):
	if 1 == cmphands(line[:14], line[15:]):
		p1count += 1
print p1count
	
	
	