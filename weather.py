import sys
import requests
def display_help():
    '''This  function prints out the  help yext for tethe user '''
    print("How to use: python3 weather.py <latitude> <longitude>")
    print("Example: python weather.py 44.1004 -70.2148")
    print("Fetches current weather data for given coordinates.")
    
def fetchWeather(latitude: float, longitude: float):
    api_url = "https://api.open-meteo.com/v1/forecast"
    ''' This function  uses the Open Metro Get requests to accept the Latitude, Longitude,
    current weather nad temperature
    '''
    param = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true",
        "temperature_unit": "fahrenheit"
    }
    
    try: 
        res = requests.get(api_url, params=param, timeout=10) #Pass the arguments  to requesrs,get
        res.raise_for_status() #Raise  incase for HTTPS errors
        new_data = res.json()
        current_status = new_data.get("current_weather", {})
        print(" Weather Results ")
        print(f"Latitude:    {new_data.get('latitude')}°")
        print(f"Longitude:   {new_data.get('longitude')}°")
        print(f"Wind Speed:  {current_status.get('windspeed')} mph")
        print(f"Temperature: {current_status.get('temperature')} °F")
        
    except requests.exceptions.RequestException as e:
        print (f"Could not access API")
        
def main():
    if len(sys.argv) < 3 or sys.argv[1] in ['help']:
        #Check for the command line arguments
        display_help()
        sys.exit(0 if len(sys.argv) >1 in  ['help'] else 1)
        
    try:
        latitude = float(sys.argv[1])
        long = float(sys.argv[2])
        print(f'You entered: Latitude: {latitude}, Longitude: {long}')
    except ValueError:
        print("[Error] Please check your  latitude and longitude values")
        display_help()
        sys.exit(1)
            
if __name__ == "__main__":
    main()