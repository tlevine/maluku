url = 'http://vocopvarenden.nationaalarchief.nl/Search.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'fr-FR,en;q=0.8,sv;q=0.5,en-US;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://vocopvarenden.nationaalarchief.nl/Search.aspx',
}

def data(viewstate, viewstategenerator, year):
    return {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': viewstate,
        'ctl00$cphMain$txtAchternaam': '',
        'ctl00$cphMain$txtVoornaam': '',
        'ctl00$cphMain$txtHerkomstplaats': '',
        'ctl00$cphMain$ddlKamer': '0',
        'ctl00$cphMain$ddlSchip': '0',
        'ctl00$cphMain$txtJaarVan': year,
        'ctl00$cphMain$txtJaarTot': year,
        'ctl00$cphMain$ddlRangGroep': '0',
        'ctl00$cphMain$ddlRang': '-1',
        'ctl00$cphMain$txtDasnr': '',
        'ctl00$cphMain$ddlManierEindeDienstverband': '-1',
        'ctl00$cphMain$ddlPlaatsEindeDienstverband': '-1',
        'ctl00$cphMain$txtJaarEindeDienstverband': '',
        'ctl00$cphMain$rbOpstappers': 'rbOpstappersWel',
        'ctl00$cphMain$rbRegimenten': 'rbRegimentenWel',
        'ctl00$cphMain$rbBegunstigden': 'rbBegunstigdenWel',
        'ctl00$cphMain$rbAbsenten': 'rbAbsentenWel',
        'ctl00$cphMain$btnSearch.x': '32',
        'ctl00$cphMain$btnSearch.y': '9',
        '__VIEWSTATEGENERATOR': viewstategenerator,
    }
