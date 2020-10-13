import urllib.request
import json

def getValues(name:str):
    
    if name == 'dollar':
        webURL = urllib.request.urlopen("https://api.tinkoff.ru/v1/currency_rates?from=USD&to=RUB")
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        json_file = json.loads(data.decode(encoding))
        return (json_file['payload']['rates'][10]['buy'],json_file['payload']['rates'][10]['sell'])
    elif name == 'euro':
        webURL = urllib.request.urlopen("https://api.tinkoff.ru/v1/currency_rates?from=EUR&to=RUB")
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        json_file = json.loads(data.decode(encoding))
        return (json_file['payload']['rates'][10]['buy'],json_file['payload']['rates'][10]['sell'])
    else:
        return "Не найдена такая валюта!"