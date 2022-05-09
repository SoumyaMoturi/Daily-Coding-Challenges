'''
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?

'''

import random
import string


def url_shortener(url):
    short  = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(6)])
    if short not in mapper.keys() and url not in mapper.values():
        mapper[short] = url
        return short + " : "+url
    elif short in mapper.keys():
        return url_shortener(url)
    elif url in mapper.values():
        return "This url is already mapped to : "+getKeyValue(url)
        
def restore_url(short_url):
    for key, value in mapper.items():
         if short_url == key:
            return "The value for "+url +"is : " +value
    return "This short url doesn't have any value mapped."
    
def getKeyValue(url):
    for key, value in mapper.items():
         if url == value:
            return key
    
        

mapper = {}
url = input()
print(url_shortener(url))
url = input()
print(url_shortener(url))
short_url = input()
print(restore_url(short_url))
