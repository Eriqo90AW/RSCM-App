import sqlite3

class SetupDB:
    def __init__(self, db_file):
        self.db_file = db_file
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS patient
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama VARCHAR(20) NOT NULL,
                    usia INTEGER NOT NULL,
                    jenis_kelamin VARCHAR(10))''')
        conn.commit()

        conn.close()

    def register(self, nama, usia, jenis_kelamin):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        
        try:
            c.execute("INSERT INTO patient (nama, usia, jenis_kelamin) VALUES (?, ?, ?)",
                (nama, usia, jenis_kelamin))
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            # Registration failed due to a duplicate username
            conn.close()
            return False

    def login(self, id):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        c.execute("SELECT * FROM patient WHERE id=?",
                (id))
        result = c.fetchone()

        conn.close()

        if result:
            return {'id': result[0], 'nama': result[1], 'usia': result[2], 'jenis_kelamin': result[3]}
        else:
            return None
    
    def getLastId(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        # Fetch the latest ID from the users table
        latest_id = c.execute("SELECT MAX(id) FROM patient").fetchone()[0]
        # Close the database connection
        conn.close()

        return latest_id