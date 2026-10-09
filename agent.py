import requests

def get_delhi_temperature():
    """Get current temperature of Delhi in Celsius"""
    try:
        # Using Open-Meteo API (free, no API key required)
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": 28.6139,
                "longitude": 77.2090,
                "current": "temperature_2m",
                "timezone": "auto"
            },
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        temp_celsius = data['current']['temperature_2m']
        return temp_celsius
    except Exception as e:
        print(f"Error fetching temperature: {str(e)}")
        return None

def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit"""
    if celsius is None:
        return None
    return (celsius * 9/5) + 32

# Get temperature
print("Fetching Delhi temperature...")
temp_celsius = get_delhi_temperature()

if temp_celsius is not None:
    temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
    print(f"\n{'='*50}")
    print(f"Current Temperature in Delhi:")
    print(f"  Celsius: {temp_celsius}°C")
    print(f"  Fahrenheit: {temp_fahrenheit:.2f}°F")
    print(f"{'='*50}")
else:
    print("Failed to retrieve temperature")
