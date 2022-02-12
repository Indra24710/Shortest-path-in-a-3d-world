class newNode:

    def __init__(self,coords):
        self.neighbors=[]
        self.val=coords[0:3]
        self.checked=False
        self.action=coords[3:]
        self.visited=False
        self.cost=0
        self.parent=None
        self.trav_cost=1000000000