''' Write an object oriented program to create a precious stone.
Not more than 5 precious stones can be held in possession at a given point of time.
If there are more than 5 precious stones, delete the first stone and store the new one. '''

class PreciousStone:

    def __init__(self):
        self.__ps = []

    def preciousStoneList(self, pstone):

        if len(self.__ps) > 4:
             del self.__ps[0]
             self.__ps.append(pstone)
             print(self.__ps)
        else:
             self.__ps.append(pstone)
             print(self.__ps)



prestone = PreciousStone()

prestone.preciousStoneList("Pearl")
prestone.preciousStoneList("Diamond")
prestone.preciousStoneList("Diamond1")
prestone.preciousStoneList("Diamond2")
prestone.preciousStoneList("Diamond3")
prestone.preciousStoneList("Diamond4")
prestone.preciousStoneList("Diamond5")
prestone.preciousStoneList("Diamond6")



