import requests
import json

# classe de serviço responsável por buscar as apis de endPoint ;
class ServiceStarWarsApi:

    def __init__(self):
        self = self

    # consumir a api e retornar um json;
    def consumirapi(self, url):
        requisicao = requests.get(url)
        dados = requisicao.json()
        return dados
