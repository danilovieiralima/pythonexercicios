import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[0;31mO Site Pudim não está acessível no momento\033[m')
else:
    print('\033[0;32mO Site Pudim está acessível no momento\033[m')
    print(site.read())
