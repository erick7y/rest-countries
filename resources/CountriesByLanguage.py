from flask_restful import Resource

from db import db

class CountriesByLanguage(Resource):
    def get(self, language):
        countries = []
        for country, info in db.items():
            if language == info['language']:
                countries.append(country)
        if countries:
            return countries
        return {'message': 'countries not found'}, 404
