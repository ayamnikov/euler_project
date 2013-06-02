#from http://projecteuler.net/thread=54&page=2 AUTHOR norvig

rankvalues = dict((r,i) 
                   for i,r in enumerate('..23456789TJQKA'))

def poker(hand):
    hand = hand.split()
    
    suits = [s for r,s in hand]
    ranks = sorted([rankvalues[[i][/i]r] for r,s in hand])
    ranks.reverse()
    flush = len(set(suits)) == 1
    straight = (max(ranks)-min(ranks))==4 
                and len(set(ranks))==5

    def kind(n, butnot=None):
        return some(r for r in ranks
                    if ranks.count(r) == n and r != butnot)


    if straight and flush: return 9, ranks
    if kind(4): return 8, kind(4), kind(1)
    if kind(3) and kind(2): return 7, kind(3), kind(2)
    if flush: return 6, ranks
    if straight: return 5, ranks
    if kind(3): return 4, kind(3), ranks
    if kind(2) and kind(2, kind(2)): 
        return 3, kind(2), kind(2, kind(2)), ranks
    if kind(2): return 2, kind(2), ranks
    return 1, ranks

print sum(poker(line[0:14]) > poker(line[15:29])
                 for line in file("poker.txt"))