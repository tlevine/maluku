import datetime

import vlermv

from . import download

def main():
    today = datetime.date.today()
    db = vlermv.Vlermv('data/vocopvarenden', mutable = False)

    search_response = download.search(today)
    year = 1640
    if year not in db:
        download.list(year, search_response = search_response)
        exportcsv_response = download.exportcsv(year, search_response = search_response)
        db[year] = exportcsv_response.text
