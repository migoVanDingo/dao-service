from datetime import datetime
import os
import random
import string
from dotenv import load_dotenv

from utility.constant import Constant
load_dotenv()


class Utils:

    @staticmethod
    def generate_id(service_id: str) -> str:
        prefix = Constant.get_service_prefix(service_id)
        N = int(os.environ['ID_LENGTH'])
        id = prefix + ''.join(random.choices(string.digits, k= N - len(prefix) - 20)) +''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
        return id
    
    @staticmethod
    def get_id_field(service_id: str) -> str:
        return Constant.get_service_id(service_id)
    
    @staticmethod
    def date_time():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def date_time_epoch():
        return datetime.now().timestamp()
    

    
