import json
import codecs
from database import *

def extract_route(request):
    return request.split()[1][1:]

def read_file(path):
    with open (path, 'rb') as arq:
        file = arq.read()
    return file

# def load_data(json_file_path):
#     with open ('data/{}'.format(json_file_path), "r", encoding="utf-8") as arq:
#         note = json.load(arq)
#     return note

def load_data(database):
    return database.get_all()

def load_template(hmtl_file_path):
    with open ('templates/{}'.format(hmtl_file_path), "r", encoding="utf-8") as arq:
        file = arq.read()
    return str(file)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers:
        headers=f"\n{headers}"
    response = f"HTTP/1.1 {code} {reason}{headers}\n\n{body}"
    return response.encode()

