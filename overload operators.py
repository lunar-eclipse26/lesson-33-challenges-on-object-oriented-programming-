class o:
    def __init__(self, o):
        self.o = o
    def __lt__(self, other):
        if(self.o<other.o):
            return "the first item in this auction is worth less than the second bidding starts at $0.3"
        else:
            return "the second item in this auction is worth less than the the first bidding starts at $0.03"
    def __eq__(self, other):
        if(self.o == other.o):
            return "both item one and item two are of equal value bidding starts at $0.3 for both"
        else:
            return "both items are not of equal value and therefore shall not be bidded at the same price"
item1 = o(2)
item2 = o(3)
print("items of extreme value being auctioned today:", item1.o, item2.o)
print(item1 < item2)
item3 = o(4)
item4 = o(4)
print("the other items of not as much value being auctioned today:", item3.o, item4.o)
print(item3 == item4)