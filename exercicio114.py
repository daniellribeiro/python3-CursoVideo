import urllib.request

url = 'https://www.google.com'
try:
    response = urllib.request.urlopen(url)
    print('Site acessivel')
    print(response.read())
except:
    print('Site fora do ar')