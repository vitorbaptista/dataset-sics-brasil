import urllib.request
import re

URL = 'http://www.acessoainformacao.gov.br/lai-para-sic/sic-apoio-orientacoes/lista-de-sics'
REGEXP = r'(http[^ ]+lai-para-sic\/[^ ]+\.xlsx)'
EXPECTED_DATA_FILE = 'lista-sics-maio-de-2018.xlsx'

html = urllib.request.urlopen(URL).read().decode('utf-8')

page_search = re.search(REGEXP, html)
if page_search:
    url = page_search.group(1)
    if not url:
        print(
            'ERROR! Could not find data URL with "%s" in URL "%s"' %
            (EXPECTED_DATA_FILE, URL)
        )
        exit(1)

    if not EXPECTED_DATA_FILE in url:
        print(
            'ERROR! Found URL "%s" that does not contain file "%s"' %
            (URL, EXPECTED_DATA_FILE)
        )
        print('ERROR! Maybe there is new data available?')
        exit(1)
