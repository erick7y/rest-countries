# Projeto Flask

Este projeto tem como objetivo criar uma API RESTful utilizando o microframework Flask.

## Requisitos

* Flask
* Flask-RESTful

## Configuração

O projeto deve ser configurado como segue:

1. Clone este repositório.
2. Instale as dependências do projeto: `pip3 install -r requirements.txt`
4. Execute o arquivo api.py para iniciar a aplicação: `python3 api.py`

## Utilização

O projeto pode ser usado para buscar informações sobre países utilizando as seguintes rotas:

* `/country/capital/<string:capital>` - busca informações sobre um país pelo nome da sua capital.
* `/country/language/<string:language>` - busca informações sobre os países que falam uma determinada língua.
* `/country/currency/<string:currency>` - busca informações sobre os países que usam uma determinada moeda.
