import requests, pyfiglet, os

g = "\033[32m"
c = "\033[36m"
r = "\033[30m"
re = "\033[31m"

def clear():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Linux and macOS
    else:
        _ = os.system('clear')


def get_location_from_ip(ip_address):
    url = f"https://ipapi.co/{ip_address}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        return latitude, longitude
    else:
        return None

clear()
print(g + pyfiglet.figlet_format("Ray-locate", font = "small"))
print(f"{g}For more tools:{r} {c}https://github.com/Rayan6608{r}")
print("")
print("")
ip_address = input(f"{g}Enter the IP address: {r}")
print("")
location = get_location_from_ip(ip_address)

if location:
    latitude, longitude = location
    print(f"{g}[+]{r} {c}Latitude: {latitude}{r}")
    print("")
    print(f"{g}[+]{r} {c}Longitude: {longitude}{r}")
    print("")
  
else:
    print(f"{re}[+] Unable to fetch location data for the given IP address.{r}")
