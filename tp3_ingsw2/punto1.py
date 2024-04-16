class FactorialCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._factorials = {0: 1, 1: 1}
        return cls._instance

    def factorial(self, n):
        if n in self._factorials:
            return self._factorials[n]
        else:
            result = n * self.factorial(n - 1)
            self._factorials[n] = result
            return result


calculator1 = FactorialCalculator()
calculator2 = FactorialCalculator()

print(calculator1 is calculator2)  
print(calculator1.factorial(15))  
print(calculator2.factorial(4))  
