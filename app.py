import logging
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from flask_mysqldb import MySQL

from utility.error import ThrowError


logging.basicConfig(filename='record.log',
                level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(lineno)d | \n %(message)-20s')

def create_app():
    app = Flask(__name__)
    CORS(app)

    # MySQL configurations
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'dao_user'
    app.config['MYSQL_PASSWORD'] = 'dao_password_2024'
    app.config['MYSQL_DB'] = 'pipeline_dao'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor' 

    #Register blueprints


    return app

def init_db(app):
    db = MySQL()
    db.init_app(app)
    return db


app = create_app()
db = init_db(app)

@app.before_request
def handle_options():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

@app.errorhandler(ThrowError)
def handle_throw_error(error):
    response = jsonify({
        "message": str(error),
        "error_code": error.status_code
    })
    response.status_code = error.status_code
    return response