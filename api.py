from flask import Flask
from flask_restful import Api, Resource

from resources.CountryByCapital import CountryByCapital
from resources.CountriesByLanguage import CountriesByLanguage
from resources.CountriesByCurrency import CountriesByCurrency

app = Flask(__name__)
api = Api(app)

api.add_resource(CountryByCapital, '/country/capital/<string:capital>')
api.add_resource(CountriesByLanguage, '/country/language/<string:language>')
api.add_resource(CountriesByCurrency, '/country/currency/<string:currency>')

if __name__ == '__main__':
    app.run(debug=True)
