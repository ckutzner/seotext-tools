"""module for database setup"""

def db_setup(db):
    con = sqlite3.connect(db)
    curs = con.cursor()
    curs.execute('CREATE TABLE jobs (id INTEGER PRIMARY KEY, name TEXT, file TEXT, targetcount INTEGER, h1 TEXT, h1target INTEGER, h21 TEXT, h21target INTEGER, h22 TEXT, h22target INTEGER, body1 TEXT, body1taget INTEGER, body2 TEXT, body2target INTEGER, body3 TEXT, body3target INTEGER)')
    con.commit()
    con.close()
