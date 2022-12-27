import requests

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    pass
    # sending get request and saving the response as response object
    response = requests.get(url = IPINFO_URL.format(ip=ip_address))

    # extracting data in json format
    data = response.json()
    
    return data['country']
    

print(get_ip_country('8.8.8.8'))

