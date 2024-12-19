import traceback
from flask import Blueprint, current_app, json, request

from dao.dao import DAO
from utility.error import ThrowError
from utility.utils import Utils

crud_api = Blueprint('crud_api', __name__)


class ICreate:
    table_name: str
    service: str
    payload: dict
    request_id: str

# Get API Health Check
@crud_api.route('/health', methods=['GET'])
def health():
    return {"status": "ok"}, 200

@crud_api.route('/create', methods=['POST'])
def create():
    print(f"request.data: {request.data}")
    data: ICreate = json.loads(request.data)
    table_name = data['table_name']
    service = data['service']
    payload = data['payload']
    request_id = data['request_id']
    current_app.logger.info(f"{request_id} --- {__name__} --- SERVICE: {service}")
    try:
        dao = DAO()
        response = dao.insert(service, table_name, data=payload)
        return response, 200
    except Exception as e:
        current_app.logger.error(f"{request_id} --- {__name__} --- {traceback.format_exc()} --- ERROR: {e}")
        raise ThrowError("Failed to create record", 500)
    
class IRead:
    table_name: str
    service: str
    filters: dict
    request_id: str

@crud_api.route('/read', methods=['POST'])
def read():
    data: IRead = json.loads(request.data)
    table_name = data['table_name']
    filters = data['filters']
    request_id = data['request_id']
    service = data['service']
    current_app.logger.info(f"{request_id} --- {__name__} --- SERVICE: {service}")

    try:
        dao = DAO()
        response = dao.read(table_name, filters)
        return response, 200
    except Exception as e:
        current_app.logger.error(f"{request_id} --- {__name__} --- {traceback.format_exc()} --- ERROR: {e}")
        raise ThrowError("Failed to read record", 500)
    
class IReadList:
    table_name: str
    service: str
    field: str
    value: str
    request_id: str

@crud_api.route('/read_list', methods=['POST'])
def read_list():
    data: IReadList = json.loads(request.data)
    table_name = data['table_name']
    field = data['field']
    value = data['value']
    request_id = data['request_id']
    service = data['service']
    current_app.logger.info(f"{request_id} --- {__name__} --- SERVICE: {service}")

    try:
        dao = DAO()
        response = dao.read_list(table_name, field, value)
        return response, 200
    except Exception as e:
        current_app.logger.error(f"{request_id} --- {__name__} --- {traceback.format_exc()} --- ERROR: {e}")
        raise ThrowError("Failed to read list", 500)
    


class IUpdate:
    table_name: str
    service: str
    key: str
    value: str
    data: dict
    request_id: str

@crud_api.route('/update', methods=['POST'])
def update():
    data: IUpdate = json.loads(request.data)
    table_name = data['table_name']
    key = data['key']
    value = data['value']
    data = data['data']
    request_id = data['request_id']
    service = data['service']
    current_app.logger.info(f"{request_id} --- {__name__} --- SERVICE: {service}")

    try:
        dao = DAO()
        response = dao.update(table_name, key, value, data)
        return response, 200
    except Exception as e:
        current_app.logger.error(f"{request_id} --- {__name__} --- {traceback.format_exc()} --- ERROR: {e}")
        raise ThrowError("Failed to update record", 500)



class IDelete:
    table_name: str
    service: str
    id: str
    request_id: str

@crud_api.route('/delete', methods=['POST'])
def delete():
    data: IDelete = json.loads(request.data)
    table_name = data['table_name']
    id = data['id']
    request_id = data['request_id']
    service = data['service']
    current_app.logger.info(f"{request_id} --- {__name__} --- SERVICE: {service}")

    try:
        dao = DAO()
        response = dao.delete(table_name, Utils.get_id_field(service), id)
        return response, 200
    except Exception as e:
        current_app.logger.error(f"{request_id} --- {__name__} --- {traceback.format_exc()} --- ERROR: {e}")
        raise ThrowError("Failed to delete record", 500)




