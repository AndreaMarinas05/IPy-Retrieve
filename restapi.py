from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')
# print('My public IP address is: {}'.format(ip))

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

#ip = '8.8.8.8'
api_key = '1188364'
api_url = 'https://geo.ipify.org/api/v2/country?apiKey=at_rNWRXy6wAp3xXWteZVqLtogmdPSn3&ipAddress=8.8.8.8'

url = api_url + 'apiKey=' + api_key + '&ipAddress=' + ip

print_url = urlopen(url).read().decode('utf8')

content = print_url.replace(",", "\n")
content2 = content.replace('"', " ")
content3 = content2.replace('{', " ")
content4 = content3.replace('}', " ")
print(content4)