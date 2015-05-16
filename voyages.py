import csv

def fix(row):
    return {
        'Departure from Cape': '23-04-1663',
        'I': '41',
        'onbcategory': 'Seafarers',
        'III': '12',
        'Built': '1662',
        'IV': '2',
        'II': '',
        'Place of arrival': 'Batavia',
        'Tonnage': '212',
        'Number': '0983.1',
        'Master': 'Roelofsz.,
        Meindert',
        'Name of ship': 'HOOGKARSPEL',
        'Date of arrival at destination': '05-07-1663',
        'Chamber for which cargo is destined': '',
        'Date of departure': '29-11-1662',
        'Place of departure': 'Texel',
        'Yard': 'Enkhuizen',
        'Particulars': "At the Cape Meindert Roelofsz. became master on the MEES; master on the HOOGKARSPEL after the Cape was Andries Brant. One seafarer was thrown overboard because of 'sodomy'. The 'passengers' who embarked at the Cape were Portuguese prisoners. The ship was wrecked between Tonkin and Japan in 1670.",
        'V': '1',
        'Arrival at Cape': '10-04-1663',
        'VI': '30',
        'Type of ship': 'fluit',
        'Chamber': 'Enkhuizen'
    }


with open('data/voyages.csv') as fp:
    r = csv.DictReader(fp)
    for row in r:
        fix(row)
