import unittest
from conversions import (
convertFahrenheitToCelsius, convertFahrenheitToKelvin,
convertKelvinToCelsius, convertKelvinToFahrenheit
)

class TestTemperatureConversions(unittest.TestCase):
 

 def test_fahrenheit_to_celsius(self):
        """Test conversion from Fahrenheit to Celsius."""
        test_cases = [
            (32, 0),
            (212, 100),
            (-40, -40),
            (572, 300),
            (-459.67, -273.15)
        ]
        for fahrenheit, expected in test_cases:
            result = convertFahrenheitToCelsius(fahrenheit)
            self.assertAlmostEqual(result, expected, places=2)
   
def test_fahrenheit_to_kelvin(self):
        """Test conversion from Fahrenheit to Kelvin."""
        test_cases = [
            (32, 273.15),
            (212, 373.15),
            (-40, 233.15),
            (572, 573.15),
            (-459.67, 0)
        ]
        for fahrenheit, expected in test_cases:
            result = convertFahrenheitToKelvin(fahrenheit)
            self.assertAlmostEqual(result, expected, places=2)

def test_kelvin_to_celsius(self):
        """Test conversion from Kelvin to Celsius."""
        test_cases = [
            (273.15, 0),
            (373.15, 100),
            (0, -273.15),
            (573.15, 300),
            (233.15, -40)
        ]
        for kelvin, expected in test_cases:
            result = convertKelvinToCelsius(kelvin)
            self.assertAlmostEqual(result, expected, places=2)
 

def test_kelvin_to_fahrenheit(self):
        """Test conversion from Kelvin to Fahrenheit."""
        test_cases = [
            (273.15, 32),
            (373.15, 212),
            (0, -459.67),
            (573.15, 572),
            (233.15, -40)
        ]
        for kelvin, expected in test_cases:
            result = convertKelvinToFahrenheit(kelvin)
            self.assertAlmostEqual(result, expected, places=2)

def test_celsius_to_kelvin(self):
        """Test conversion from Celsius to Kelvin."""
        test_cases = [
            (0, 273.15),
            (100, 373.15),
            (-273.15, 0),
            (300, 573.15),
            (-40, 233.15)
        ]
        for celsius, expected in test_cases:
            result = convertCelsiusToKelvin(celsius)
            self.assertAlmostEqual(result, expected, places=2)

def test_celsius_to_fahrenheit(self):
        """Test conversion from Celsius to Fahrenheit."""
        test_cases = [
            (0, 32),
            (100, 212),
            (-40, -40),
            (300, 572),
            (-273.15, -459.67)
        ]
        for celsius, expected in test_cases:
            result = convertCelsiusToFahrenheit(celsius)
            self.assertAlmostEqual(result, expected, places=2)

if __name__ == "__main__":
    unittest.main()