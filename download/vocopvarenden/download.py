import requests
from vlermv import cache

from . import (
    list as _list, exportcsv as _exportcsv,
    parse,
)

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
    return requests.post(_list.url, headers = _list.headers,
               cookies = search_response.cookies,
               data = _list.data(viewstate, viewstategenerator, year))

@cache(DIR, 'exportcsv')
def exportcsv(year, list_response = None):
    if not list_response:
        raise TypeError('You must pass a list_response.')
    return requests.get(_exportcsv.url, headers = _exportcsv.headers,
                        cookies = list_response.cookies)
