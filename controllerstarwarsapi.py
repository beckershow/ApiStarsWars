#Classe de controle para manipular as ações

from servicestarwarsapi import ServiceStarWarsApi
from people import People
import json
from collections import namedtuple


try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace


class ControllerStartWarsApi:

    def __init__(self):
        self = self
        self.totalPaginas = 0
        self.list_pessoas = []

    # busca todas as pessoas de um filme do starwars, todos os atores.
    def buscarPessoasDoFilme(self):
        self = self
        serviceapi = ServiceStarWarsApi()
        reponse = serviceapi.consumirapi('https://swapi.dev/api/people')
        #print(reponse)
        self.totalPaginas = reponse['count']
        self.buscarPessoas(self.totalPaginas)

    # para o total de pessoas, busca a informação individual de cada uma
    def buscarPessoas(self, total):
        self = self
        #print(total)
        i = 1
        # limitado até 10 para testes somente, futuramente por numa thread para buscar as info.
        while i <= 10:
            #print('https://swapi.dev/api/people/?page =' + str(i))
            self.buscarPessoaEspecifica('https://swapi.dev/api/people/?page =' + str(i))
            i += 1

    # colhendo as informações das pessoas;
    def buscarPessoaEspecifica(self, urlpessoa):
        self = self
        serviceapi = ServiceStarWarsApi()
        reponse = serviceapi.consumirapi(urlpessoa)
        #print(reponse)
        self.criarObjectoPessoa(reponse)

    # criando o objecto de pessoa e guardando numa lista
    def criarObjectoPessoa(self, jsonobject):
        self = self

        for pessoa_lista in jsonobject['results']:
            pessoa = People()
            pessoa.name = pessoa_lista['name']
            pessoa.height = pessoa_lista['height']
            pessoa.mass = pessoa_lista['mass']
            pessoa.hair_color = pessoa_lista['hair_color']
            pessoa.skin_color = pessoa_lista['skin_color']
            pessoa.eye_color = pessoa_lista['eye_color']
            pessoa.birth_year = pessoa_lista['birth_year']
            pessoa.gender = pessoa_lista['gender']
            self.list_pessoas.append(pessoa)

    # imprimir todos os participantes de um filme;
    def imprimirListaPessoaFilme(self):
        pessoas = ''
        for pessoa in self.list_pessoas:
            pessoas += ' ' + pessoa.name + '\n'
        print(pessoas)
