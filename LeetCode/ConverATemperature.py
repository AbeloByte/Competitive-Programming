class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Listo = []
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        Listo.append(Kelvin)
        Listo.append(Fahrenheit)
        return Listo
