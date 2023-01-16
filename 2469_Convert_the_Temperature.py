class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        self.celsius = celsius

        Kelvin = "{0:.5f}".format(celsius + 273.15)
        Fahrenheit = "{0:.5f}".format(celsius * 1.80 + 32.00)
        return [Kelvin, Fahrenheit]

a  = Solution()
print(a.convertTemperature(36.50))