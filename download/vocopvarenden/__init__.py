import datetime

import vlermv

from . import download

today = datetime.date.today()
db = vlermv.Vlermv('data/vocopvarenden', mutable = False)

search_response = download.search(today)
year = 1640
if year not in db:
    list_response = download.list(year, search_response = search_response)
    exportcsv_response = download.exportcsv(year, list_response = list_response)
    db[year] = exportcsv_response.text
