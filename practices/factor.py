
class factor():

    def __init__(self, factor_name, neighbor):
        self.name = factor_name
        self.neighbor_list = neighbor

    def operate(self, neighbor_list):
        if neighbor_list[0].color != neighbor_list[1].color:
            value = 1
        else:
            value = 0
        return value
    
class state():
    def __init__(self, name, color):
        self.name = name
        self.color = color

WA = state("WA", "red")
NT = state("NT", "red")
neighbor= [WA,NT]
f1 = factor("f1", [WA, NT])
print(f1.operate(neighbor))
