import csv, logging, sys

logger = logging.getLogger(__name__)

STRANGE_TONNAGES = {
    '': None,
    '± 90': 90,
}

def fix(row):
    fixed = dict(row)

    fixed['Type of ship'] = row['Type of ship'].replace('?', '')

    if row['Tonnage'] in STRANGE_TONNAGES:
        fixed['Tonnage'] = STRANGE_TONNAGES[row['Tonnage']]
    else:
        try:
            fixed['Tonnage'] = int(row['Tonnage'])
        except ValueError:
            logger.warning('Could not parse "%s" as a tonnage' % row['Tonnage'])
            fixed['Tonnage'] = None

    return fixed

with open('sources/voyages.csv') as fp:
    header = next(csv.reader(fp))
    fp.seek(0)

    r = csv.DictReader(fp)

    w = csv.DictWriter(sys.stdout, fieldnames = header)
    w.writeheader()
    for row in r:
        w.writerow(fix(row))
