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
