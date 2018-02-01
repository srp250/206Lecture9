#ny-simple.py
import requests
import secrets

nyt_key = "7a4d814ee4074a948987047e52edd3bf"

# gets stories from a particular section of NY times
def get_stories(section):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + section + '.json'
    params={'api-key': nyt_key}
    return requests.get(extendedurl, params).json()

section = 'science'
stories = get_stories(section)
print(stories)
