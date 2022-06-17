#Temperature Conversion from Fahrenheit to Celsius
temp = float(input("Enter temperature in fahrenheit: "))
celsius = (temp - 32) * 5 / 9
print(f"Temperature in celsius = {celsius}")


#Temperature Conversion from Celsius to Fahrenheit
temp = float(input("Enter temperature in celsius: "))
fahrenheit = (temp * 1.8) + 32
print(f"Temperature in fahrenheit = {fahrenheit}")
