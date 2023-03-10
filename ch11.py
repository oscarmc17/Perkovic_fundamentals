# ------------------------------- 11.1 -------------------------------
from urllib.request import urlopen

# def getSource(url):
#     'returns the content of resource specified by url as a string'
#     response = urlopen(url)
#     html = response.read()
#     return html.decode()

# print(getSource('http://www.google.com'))

# PRACTICE PROBLEM 11.1
def news(url, topics):
    response = urlopen(url)
    html = response.read()
    content = html.decode().lower()

    for topic in topics:
        n = content.count(topic)
        print('{} appears {} times.'.format(topic, n))

print(news('http://bbc.co.uk', ['economy', 'climate', 'education']))