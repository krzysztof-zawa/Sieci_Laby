class Calculator:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y
    
    def get(self):
        return self.x, self.y
    
    def add(self):
        return self.x +self.y
    
    def multiply(self):
        return self.x * self.y
    
    def devide(self):
        try:
            return self.x/self.y
        except ZeroDivisionError:
            print("Błąd: dzielenie przez zero")
            
        
if __name__ == "__main__":
    calc = Calculator()

    calc.set(10, 0)
    print(calc.get())
    print(calc.add())
    print(calc.multiply())
    print(calc.devide())