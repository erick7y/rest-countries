from flask_restful import Resource

from db import db

class CountryByCapital(Resource):
    def get(self, capital):
        for country, info in db.items():
            if capital == info['capital']:
                return info
        return {'message': 'country not found'}, 404
