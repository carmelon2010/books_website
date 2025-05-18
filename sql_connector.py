import psycopg2
import psycopg2.extras

con = psycopg2.connect("postgresql://books_db_5wl5_user:6CM4lBX5PWlsZ77Rccx9IRPRIDDcjUH4@dpg-d0kahmje5dus73bkbvc0-a.oregon-postgres.render.com/books_db_5wl5")
cur = con.cursor()

def add_book(name):
    global con, cur
    cur.execute("CREATE TABLE IF NOT EXISTS books (name text, url text, user text);")
    psycopg2.extras.execute_batch(cur, "INSERT INTO books (name, url, user) VALUES (%s, %s, %s)", [name])
    con.commit()

def load_books():
    global con, cur
    cur.execute("CREATE TABLE IF NOT EXISTS books (name text, url text, user text);")
    cur.execute("SELECT * FROM books;")
    rows = cur.fetchall()
    con.commit()
    return rows

def delete_book(name):
    global con, cur
    cur.execute("DELETE FROM books WHERE name = %s", [name])
    con.commit()
