import sqlite3
from sqlite3.dbapi2 import Cursor

class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content

class Database:
    def __init__(self, database):
        self.conn = sqlite3.connect(database + '.db')
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)"
        )

    def add (self, note):
        self.conn.execute(
            "INSERT INTO note (title, content) VALUES ('{}', '{}');".format(note.title, note.content)
        )
        self.conn.commit()

    def get_all(self):
        Cursor = self.conn.execute("SELECT id, title, content FROM note")
        notes = [Note(id = linha[0], title=linha[1], content=linha[2]) for linha in Cursor]
        return notes

    def update(self, entry):
        self.conn.execute(
            "UPDATE note SET title = '{}' WHERE id = {}".format(entry.title, entry.id)
        )
        self.conn.execute(
            "UPDATE note SET content = '{}' WHERE id = {}".format(entry.content, entry.id)
        )
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute(
            "DELETE FROM note WHERE id = {}".format(note_id)
        )
        self.conn.commit()






