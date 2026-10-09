import requests

def get_delhi_temperature():
    """Fetch current temperature of Mumbai"""
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={           
            "latitude": 19.0760,     
            "longitude": 72.8777,
            "current": "temperature_2m",
            "timezone": "auto"
        }
    )
    return response.json()['current']['temperature_2m']

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

# Get temperature
temp_celsius = get_delhi_temperature()
temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)

print(f"Delhi Temperature: {temp_celsius}°C")
print(f"Delhi Temperature: {temp_fahrenheit}°F")
