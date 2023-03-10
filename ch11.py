# ------------------------------- 11.1 -------------------------------
from urllib.request import urlopen


def getSource(url):
    'returns the content of resource specified by url as a string'
    response = urlopen(url)
    html = response.read()
    return html.decode()

print(getSource('http://www.google.com'))
