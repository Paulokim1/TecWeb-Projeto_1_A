from os import error, replace
from utils import build_response, load_data, load_template
from database import *
import urllib

db = Database('database')

def index(request):
    
    if request.startswith('POST'):
        request = request.replace('\r', '') 
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}

        for chave_valor in corpo.split('&'):
            if chave_valor.startswith("id"):
                params["id"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
            if chave_valor.startswith("titulo"):
                params["titulo"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
            if chave_valor.startswith("detalhes"):
                params["detalhes"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")    
            if chave_valor.startswith("tipo_acao"):
                params["tipo_acao"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
        
        if params['tipo_acao'] == 'add':
           note = Note(title=params['titulo'], content=params['detalhes'])
           db.add(note)
        elif params['tipo_acao'] == 'delete':
            db.delete(params['id'])
        elif params['tipo_acao'] == 'update':
            updated_note = Note(id = params['id'], title=params['titulo'], content=params['detalhes'])
            db.update(updated_note)
    
    note_template = load_template('components/note.html')
    notes = [
        note_template.format(card_id = note.id, title=note.title, details=note.content)
        for note in load_data(db)
    ]
    notes = '\n'.join(notes)

    body = load_template('index.html').format(notes = notes)

    if request.startswith('POST'):
        response = (build_response(code=303, reason='See Other', headers='Location: /', body=body))
    else:
        response = (build_response(code=200, body=body))

    return response 