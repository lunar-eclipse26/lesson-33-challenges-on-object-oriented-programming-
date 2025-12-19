class speed_paper:
    def __init__(self, name, idk):
        self.name = name
        self.idk = idk
    def __str__(self):
        return self.name + '(' + self.idk + ')'
speed = []
print("our next items are speed papers designed by jo king from the temu head office these cards are to help u remember thing")
while(True):
    name = input("enter your name:")
    idk = input("i didnt know what to put here so just write whatever u need to remember:")
    speed.append(speed_paper(name, idk))
    option = int(input("hi the speed paper team speaking if would like to create another speed paper please enter 1 for yes and 0 for no:"))
    if(option == 0):
        break
print("\n your speed papers are below")
for i in speed:
    print(">", i)
print("and that is a demonstration of he wonderful speed paper bidding starts at $40")