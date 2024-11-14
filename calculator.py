class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        negative = (a > 0) != (b > 0)
        a, b = abs(a), abs(b)
        for i in range(b):
            result = self.add(result, a)
        if negative:
            result = -result
        return result

    def divide(self, a, b):
        result = 0
        negative = (a > 0) != (b > 0)
        a, b = abs(a), abs(b)
        if (a == 0) or (b == 0):
            result = 0
        else:
            while a >= b:
                a = self.subtract(a, b)
                result = self.add(result, 1)
        if negative:
            result = self.multiply(result, -1)
        return result
    
    def modulo(self, a, b):
        result = abs(a)
        divisor = abs(b)
        while result >= divisor:
            result = self.subtract(result, divisor)
        if a < 0:
            result = -result
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            result = self.add(result, b)
        return result

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))