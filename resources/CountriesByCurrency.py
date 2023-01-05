from flask_restful import Resource

from db import db

class CountriesByCurrency(Resource):
    def get(self, currency):
        countries = []
        for country, info in db.items():
            if currency == info['currency']:
                countries.append(country)
        if countries:
            return countries
        return {'message': 'countries not found'}, 404
