class Charge:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
    
    def get_weight(self):
        return self.weight
    
    def get_value(self):
        return self.value
    
    def get_value_per_weight(self):
        return self.value/self.weight
    
    def __str__(self):
        return f"Charge(Weight: {self.get_weight()} Value: {self.get_value()})"

def bubbleSort_charge(charge_list):
    for passnum in range(len(charge_list)-1,0,-1):
        for i in range(passnum):
            if charge_list[i].get_value_per_weight() < charge_list[i+1].get_value_per_weight():
                temp = charge_list[i]
                charge_list[i] = charge_list[i+1]
                charge_list[i+1] = temp

def knapsack(charger_list, max_weight):
    bubbleSort_charge(charger_list)
    selected = []
    for charge in charger_list:
        if max_weight == 0:
            return selected
        elif charge.get_weight() <= max_weight:
            selected.append((charge, 1))
            max_weight -= charge.get_weight()
        elif max_weight > 0:
            variable = max_weight/charge.get_weight()
            selected.append((charge, variable))
            max_weight = 0
    if max_weight >= 0:
        return selected



box1 = Charge(10,60)
box2 = Charge(20,100)
box3 = Charge(30,120)

alist = [box3, box2, box1]
for i in knapsack(alist, 100):
    print(i[0], ", ", i[1])