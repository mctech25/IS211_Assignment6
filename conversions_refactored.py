class ConversionNotPossible(Exception):
    """Exception raised when conversion is not possible."""
    pass

conversion_rates = {
    ('Celsius', 'Fahrenheit'): lambda x: (x * 9/5) + 32,
    ('Celsius', 'Kelvin'): lambda x: x + 273.15,
    ('Fahrenheit', 'Celsius'): lambda x: (x - 32) * 5/9,
    ('Fahrenheit', 'Kelvin'): lambda x: (x + 459.67) * 5/9,
    ('Kelvin', 'Celsius'): lambda x: x - 273.15,
    ('Kelvin', 'Fahrenheit'): lambda x: (x * 9/5) - 459.67,
    
    ('Miles', 'Yards'): lambda x: x * 1760,
    ('Miles', 'Meters'): lambda x: x * 1609.34,
    ('Yards', 'Miles'): lambda x: x / 1760,
    ('Yards', 'Meters'): lambda x: x * 0.9144,
    ('Meters', 'Miles'): lambda x: x / 1609.34,
    ('Meters', 'Yards'): lambda x: x / 0.9144
}

def convert(fromUnit, toUnit, value):
    """Converts between units if possible, else raises ConversionNotPossible."""
    if fromUnit == toUnit:
        return float(value)
    try:
        return float(conversion_rates[(fromUnit, toUnit)](value))
    except KeyError:
        raise ConversionNotPossible(f"Cannot convert {fromUnit} to {toUnit}")