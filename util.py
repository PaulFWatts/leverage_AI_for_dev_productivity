def convert_temperature(value, unit):
    """
    Convert temperature between Celsius and Fahrenheit.

    Parameters:
    value (float): The temperature value to be converted.
    unit (str): The unit of the input temperature value. 
                'C' for Celsius, 'F' for Fahrenheit.

    Returns:
    float: The converted temperature value.

    Raises:
    ValueError: If the unit is not 'C' or 'F'.
    """
    if unit.lower() == 'c':
        return (value * 9/5) + 32  # Convert Celsius to Fahrenheit
    elif unit.lower() == 'f':
        return (value - 32) * 5/9  # Convert Fahrenheit to Celsius
    else:
        raise ValueError("Unit must be 'C' or 'F'")


