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

