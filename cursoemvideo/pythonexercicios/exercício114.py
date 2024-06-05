import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com')
except:
    print('Deu erro.')
else:
    print('Tudo ok.')