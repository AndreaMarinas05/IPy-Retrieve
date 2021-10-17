from requests import get
import sys

def main():
    name = (input('Enter your first name: '))

    try:
        from urllib.request import urlopen
    except ImportError:
        from urllib2 import urlopen

    ip = get('https://api.ipify.org').content.decode('utf8')
    api_key = '1187709'
    api_url = 'https://geo.ipify.org/api/v2/country?apiKey=at_BKm9FLOgSF8SSbBYIwrPlHwlYLW8t&ipAddress=8.8.8.8'

    url = api_url + 'apiKey=' + api_key + '&ipAddress=' + ip

    print('\nHere are the IP details of', name, ':')
    print_url = urlopen(url).read().decode('utf8')

    content = print_url.replace(",", "\n")
    content2 = content.replace('"', " ")
    content3 = content2.replace('{', " ")
    content4 = content3.replace('}', " ")
    print(content4)

main()


while True:
    try_again = input('\nTry again? Y/N: ')
    try_again = try_again.lower()
    
    if try_again == 'y':
        main()
    elif try_again == 'n':
        print('Thank you for trying Triple Threat IP program.')
        print('Ferrer, Mariñas, Trazo | 4ITD')
        sys.exit()
    else:
        try_again