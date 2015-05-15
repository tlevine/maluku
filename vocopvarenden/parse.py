import re

import lxml.html

class forminputs:
    def __init__(self, html):
        self.html = html
    def __getitem__(self, name):
        return self.html.xpath('//input[@name="%s"]/@value' % name)[0]

def viewstate(response):
    html = lxml.html.fromstring(response.text)
    inputs = forminputs(html)
    return inputs['__VIEWSTATE'], inputs['__VIEWSTATEGENERATOR']

def exportcsv(response):
    html = lxml.html.fromstring(response.text)
    raw_head, *trs = (map(str, tr.xpath('td/text()')) for tr in html.xpath('//tr'))
    head = [re.sub(r'[ .]', '_', text.strip()).lower() for text in raw_head]
    return (dict(zip(head, tr)) for tr in trs)
