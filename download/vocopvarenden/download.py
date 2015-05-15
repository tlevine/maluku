import requests
from vlermv import cache

from . import list, exportcsv, parse

DIR = '~/.maluku/vocopvarenden'

@cache(DIR, 'search')
def search(_):
    url = 'http://vocopvarenden.nationaalarchief.nl/Search.aspx'
    return requests.get(url)

@cache(DIR, 'list')
def list(year, search_response = None):
    if not search_response:
        raise TypeError('You must pass a search_response.')
    viewstate, viewstategenerator = parse.viewstate(search_response)
    return requests.post(list.url, headers = list.headers,
               cookies = search_response.cookies
               data = list.data(viewstate, viewstategenerator, year))
