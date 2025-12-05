"""
Initialisation de la base de données - Contient des vulnérabilités
"""
import sqlite3

# ⚠️ VULNÉRABILITÉ: Mot de passe en dur (CWE-259, B105)
ADMIN_PASSWORD = "admin@123"
DB_USER = "root"
DB_PASSWORD = "password123"

def init_database():
    """Initialize database with vulnerable configuration"""
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Créer table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    ''')
    
    # ⚠️ VULNÉRABILITÉ: Mots de passe en dur
    cursor.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'admin@123')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (2, 'user', 'user456')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (3, 'test', 'testpass789')")
    
    conn.commit()
    conn.close()
    print("✓ Base de données initialisée")

if __name__ == '__main__':
    init_database()
