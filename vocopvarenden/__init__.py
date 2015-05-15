import datetime, csv, sys

from . import download, parse

FIELDNAMES = (
    'first_name',
    'family_name',
    'inv_nr',
    'folio',
    'year_departure',
    'ship',
    'name',
    'origin',
    'occupation',
    'month_certificate',
    'year_tenure_ended',
    'month_tenure_ended',
    'day_tenure_ended',
    'reason_tenure_ended',
    'place_tenure_ended',
    'type_person',
    'remarks',
)

def main():
    w = csv.DictWriter(sys.stdout, fieldnames = FIELDNAMES)
    w.writeheader()

    today = datetime.date.today()
    search_response = download.search(today)

    for year in range(1633, 1794 + 1):

        download.list(year, search_response = search_response)
        exportcsv_response = download.exportcsv(year, search_response = search_response)

        w.writerow(parse.exportcsv(exportcsv_response))
