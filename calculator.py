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
            temp_result = 0
            for _ in range(abs(result)):
                temp_result = self.add(temp_result, -1)
            result = temp_result
        
        return result

    def divide(self, a, b):
        result = 0
        negative = (a > 0) != (b > 0)
        checkZero = (a == 0)
        a, b = abs(a), abs(b)
        if (a == 0) or (b == 0):
            result = 0
        else: 
            while a > b:
                a = self.subtract(a, b)
                result += 1
            result += 1
        if negative:
            temp_result = 0
            for _ in range(abs(result)):
                temp_result = self.add(temp_result, -1)
            result = temp_result
        return result
    
    def modulo(self, a, b):
        while abs(a) >= abs(b):
            a = a - b
        if a < 0 and b > 0:
            while a < 0:
                a = a + b
        elif a > 0 and b < 0:
            while a > 0:
                a = a + b
        return a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
    print("Example: modulo: ", calc.modulo(3, -2))