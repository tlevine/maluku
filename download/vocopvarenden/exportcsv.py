def url():
    return 'http://vocopvarenden.nationaalarchief.nl/exportCSV.aspx'

def headers(cookie):
    return {
        'Host': 'vocopvarenden.nationaalarchief.nl',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'fr-FR,en;q=0.8,sv;q=0.5,en-US;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://vocopvarenden.nationaalarchief.nl/list.aspx',
        'Cookie': cookie,
        'Connection': 'keep-alive',
    }
