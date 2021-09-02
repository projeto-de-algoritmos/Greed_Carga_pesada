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
