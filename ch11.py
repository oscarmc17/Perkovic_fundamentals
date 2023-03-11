# ------------------------------- 11.1 -------------------------------
from html.parser import HTMLParser
from urllib.request import urlopen
from re import findall

# def getSource(url):
#     'returns the content of resource specified by url as a string'
#     response = urlopen(url)
#     html = response.read()
#     return html.decode()

# print(getSource('http://www.google.com'))

# PRACTICE PROBLEM 11.1
# def news(url, topics):
#     response = urlopen(url)
#     html = response.read()
#     content = html.decode().lower()

#     for topic in topics:
#         n = content.count(topic)
#         print('{} appears {} times.'.format(topic, n))

# print(news('http://bbc.co.uk', ['economy', 'climate', 'education']))


# infile = open('w3c.html')
# content = infile.read()
# infile.close()
# parser = HTMLParser()
# parser.feed(content)

# class LinkParser(HTMLParser):
#     '''HTML doc parser that prints values of href attributes in anchor start tags'''
#     def handle_starttag(self, tag, attrs):
#         'print value of href attribute if any'
#         if tag == 'a':  # if anchor tag
#             # search for href attribute and print its value
#             for attr in attrs:
#                 if attr[0] == 'href':
#                     print(attr[1])


# rsrce = urlopen('http://www.w3.org/Consortium/mission.html')
# content = rsrce.read().decode()
# linkparser = LinkParser()
# linkparser.feed(content)

# print(findall('best', 'beetbtbelt?bet, best'))
# print(findall('be.t', 'beetbtbelt?bet, best'))
# print(findall('be?t', 'beetbtbelt?bet, best'))
# print(findall('be*t', 'beetbtbelt?bet, best'))
# print(findall('be+t', 'beetbtbelt?bet, best'))

# # Matching the longer substring only
# print(findall('e+', 'beeeetbet bt'))

# Practice Problem 11.6
def frequency(content):
    pattern = '[a-zA-Z]+'
    words = findall(pattern, content)
    dictionary = {}
    for w in words:
        if w in dictionary:
            dictionary[w] += 1
        else:
            dictionary[w] = 1
    return dictionary

content = 'The pure and simple truth is rarely pure and never\ simple.'

print(frequency(content))
