import urllib.request
import json

def getValues(name:str):
    if name == 'dollar':
        webURL = urllib.request.urlopen("https://www.sberbank.ru/portalserver/proxy/?pipe=shortCachePipe&url=http%3A%2F%2Flocalhost%2Frates-web%2FrateService%2Frate%2Fcurrent%3FregionId%3D77%26rateCategory%3Dbase%26currencyCode%3D840")
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        json_file = json.loads(data.decode(encoding))
        return (json_file['base']['840']['0']['buyValue'], json_file['base']['840']['0']['sellValue'])
    elif name == 'euro':
        webURL = urllib.request.urlopen("https://www.sberbank.ru/portalserver/proxy/?pipe=shortCachePipe&url=http%3A%2F%2Flocalhost%2Frates-web%2FrateService%2Frate%2Fcurrent%3FregionId%3D77%26rateCategory%3Dbase%26currencyCode%3D978")
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        json_file = json.loads(data.decode(encoding))
        return (json_file['base']['978']['0']['buyValue'], json_file['base']['978']['0']['sellValue'])
    else:
        return "Не найдена такая валюта!"

# https://www.vtb.ru/api/currency-exchange/currency-converter-info?changeSummaType=1&contextItemId=%7BC5471052-2291-4AFD-9C2D-1DBC40A4769D%7D&conversionPlace=0&conversionType=0&currencyFromCode=RUR&currencyToCode=EUR&fromSumma=0&toSumma=0
# https://www.vtb.ru/api/currency-exchange/currency-converter-info?changeSummaType=1&contextItemId=%7BC5471052-2291-4AFD-9C2D-1DBC40A4769D%7D&conversionPlace=0&conversionType=0&currencyFromCode=RUR&currencyToCode=USD&fromSumma=0&toSumma=0