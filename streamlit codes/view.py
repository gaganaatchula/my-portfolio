import sqlite3

def view_messages():
    conn = sqlite3.connect('contact_form.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contact_messages')
    rows = cursor.fetchall()
    conn.close()
    return rows

print(view_messages())