import sys
import requests
def display_help():
    '''This  function prints out the  help yext for tethe user '''
    print("How to use: python3 weather.py <latitude> <longitude>")
    print("Example: python weather.py 44.1004 -70.2148")
    print("Fetches current weather data for given coordinates.")
    
def main():
    if len(sys.argv) < 3 or sys.argv[1] in ['help']:
        #Check for the comman line arguments
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