import datetime, csv, sys

from . import download, parse

FIELDNAMES = (
    'voornaam',
    'achternaam',
    'inv_nr',
    'folio',
    'jaarvertrek',
    'schip',
    'naam',
    'herkomst',
    'beroep',
    'maandbrief',
    'eindejaar',
    'eindemaand',
    'eindedag',
    'eindeomschrijving',
    'eindeplaats',
    'typepersoon',
    'opmerkingen',
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
