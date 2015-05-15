def url():
    return 'http://vocopvarenden.nationaalarchief.nl/Search.aspx'

def headers(cookie):
    return {
        'Host': 'vocopvarenden.nationaalarchief.nl',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'fr-FR,en;q=0.8,sv;q=0.5,en-US;q=0.3',,
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://vocopvarenden.nationaalarchief.nl/Search.aspx',
        'Cookie': cookie,
        'Connection: keep-alive',
    }

def data(viewstate, viewstategenerator, year):
    return {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': viewstate,
        'ctl00%24cphMain%24txtAchternaam': '',
        'ctl00%24cphMain%24txtVoornaam': '',
        'ctl00%24cphMain%24txtHerkomstplaats': '',
        'ctl00%24cphMain%24ddlKamer': '0',
        'ctl00%24cphMain%24ddlSchip': '0',
        'ctl00%24cphMain%24txtJaarVan': year,
        'ctl00%24cphMain%24txtJaarTot': year,
        'ctl00%24cphMain%24ddlRangGroep': '0',
        'ctl00%24cphMain%24ddlRang': '-1',
        'ctl00%24cphMain%24txtDasnr': '',
        'ctl00%24cphMain%24ddlManierEindeDienstverband': '-1',
        'ctl00%24cphMain%24ddlPlaatsEindeDienstverband': '-1',
        'ctl00%24cphMain%24txtJaarEindeDienstverband': '',
        'ctl00%24cphMain%24rbOpstappers': 'rbOpstappersWel',
        'ctl00%24cphMain%24rbRegimenten': 'rbRegimentenWel',
        'ctl00%24cphMain%24rbBegunstigden': 'rbBegunstigdenWel',
        'ctl00%24cphMain%24rbAbsenten': 'rbAbsentenWel',
        'ctl00%24cphMain%24btnSearch.x': '32',
        'ctl00%24cphMain%24btnSearch.y': '9',
        '__VIEWSTATEGENERATOR': viewstategenerator,
    }
