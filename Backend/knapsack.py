class Charge:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
    
    def get_name(self) -> str:
        return self.name

    def get_weight(self) -> int:
        return self.weight
    
    def get_value(self) -> int:
        return self.value
    
    def get_value_per_weight(self) -> float:
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

def knapsack(charge_list, max_weight):
    bubbleSort_charge(charge_list)
    selected = []
    for charge in charge_list:
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
