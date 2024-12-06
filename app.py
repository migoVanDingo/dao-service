import logging
import os
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
import mysql.connector  # Import mysql.connector
from dotenv import load_dotenv
load_dotenv()

from api.CRUD.crud_api import crud_api
from utility.error import ThrowError


logging.basicConfig(filename='record.log',
                level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(lineno)d | \n %(message)-20s')

def create_app():
    app = Flask(__name__)
    CORS(app)

    # MySQL configurations
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost') 
    app.config['MYSQL_USER'] = 'dao_user'
    app.config['MYSQL_PASSWORD'] = 'dao_password_2024'
    app.config['MYSQL_DB'] = 'pipeline_dao'
    app.config['MYSQL_PORT'] = int(os.environ.get('MYSQL_PORT', 3306))

    # Register blueprints (if any)
    app.register_blueprint(crud_api, url_prefix='/api')

    return app

# Function to get database connection using mysql.connector
def get_db_connection():
    conn = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        port=app.config['MYSQL_PORT']
    )
    return conn


app = create_app()

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
