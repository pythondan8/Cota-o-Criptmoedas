import requests
def moeda(a):
    a = a+'USDT'
    link = requests.get('https://api.binance.com/api/v3/ticker/price')
    if link.status_code == 200:
        data = link.json()
        for lista in data:
            if lista['symbol'] == a:
                a = (f"Criptmoeda: {lista['symbol']} | Preço {lista['price']} ")
                return a
a = input('Digite a sigla da criptomoeda: ').upper()
print(moeda(a))






