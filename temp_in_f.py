def convert_c_to_f(temp_c):
    """
    Convert Celsius to Fahrenheit.
    
    :param temp_c: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    farenheit_temp = (temp_c * 9/5) + 32
    return farenheit_temp

temp_in_f = convert_c_to_f(25)
print(temp_in_f)  # Should print 77.0