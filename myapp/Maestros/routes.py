from flask import Blueprint

maestros=Blueprint('Maestros',__name__)

@maestros.route('/geMaestros',methods=['GET'])
def geMaestros():
    return {'key': 'Maestros'}