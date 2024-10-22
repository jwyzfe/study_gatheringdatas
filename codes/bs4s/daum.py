
#boxCommodities .box_contents div table tbody tr td.pR span.num


from bs4 import BeautifulSoupsoup
soup = BeautifulSoup(response.text, 'html.parser')

currency_prices = soup.select('boxCommodities .box_contents div table tbody tr td.pR span.num')
type(currency_prices)

for currency in currency_prices:
    print(f'Tag : {currency}, Currency Price : {currency.text}')
    pass
