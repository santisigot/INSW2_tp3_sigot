class TaxCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calculate_taxes(self, base_amount):
        iva = base_amount * 0.21
        iibb = base_amount * 0.05
        municipal_contributions = base_amount * 0.012
        total_tax = iva + iibb + municipal_contributions
        return total_tax


calculator = TaxCalculator()
base_amount = 1000  

total_tax = calculator.calculate_taxes(base_amount)
print("precio de los impuestos:", total_tax)
