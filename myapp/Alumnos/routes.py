from flask import Blueprint

alumnos=Blueprint('alumnos',__name__)

@alumnos.route('/gealum',methods=['GET'])
def gealum():
    return {'key': 'Alumnos'}