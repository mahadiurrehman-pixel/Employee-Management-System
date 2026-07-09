import sqlite3
import re

class log_register:
    def __init__(self):
        self.con = sqlite3.connect("LOGIN.db")
        self.cursor = self.con.cursor()
        self.construct_table()
    def construct_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        self.con.commit() 
    def insert_value(self, name, email, password):
        try:
            self.cursor.execute('''
                INSERT INTO logs(name, email, password)
                VALUES (?, ?, ?)
            ''', (name, email, password))
            self.con.commit()
            return True   
        except sqlite3.IntegrityError:
            print(" Email already exists!")
            return False  
    def register(self):
        self.name = input("ENTER YOUR NAME: ").strip()
        while True:
            self.email = input("ENTER YOUR EMAIL: ").strip().lower()
            if self.valid_email(self.email):
                break
            print("Invalid email! Please enter a valid email.")
        while True:
            self.password = input("ENTER PASSWORD: ").strip()
            if self.strong_password(self.password):
                break
            print("Weak password!")
            print("Password must have:")
            print("  - at least 8 characters")
            print("  - 1 uppercase letter")
            print("  - 1 lowercase letter")
            print("  - 1 digit")
            print("  - 1 special character (!@#$%^&*...)")
        if self.insert_value(self.name, self.email, self.password):
            print("✅ Registration successful!")
            n = input("\nTo LOGIN PRESS 1: ").strip()
            if n == "1":
                self.login()
    def valid_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        self.cursor.execute("SELECT * FROM logs WHERE email = ?", (email,))
        user = self.cursor.fetchone()
        if user :
            print("EMAIL ALREADY EXIST")
            a= False
        else:
            a=True
        return re.fullmatch(pattern, email) is not None and a
    def strong_password(self, password):
        return (
            len(password) >= 8 and
            re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'\d', password) and
            re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
        )
    def valid_email_login(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.fullmatch(pattern, email) is not None 
    def login(self):
        while True:
            self.email = input("ENTER YOUR EMAIL: ").strip().lower()
            if self.valid_email_login(self.email):
                break
            print("INVALID! Enter Valid Email")
        self.password = input("ENTER PASSWORD: ").strip()
        self.cursor.execute(
            "SELECT * FROM logs WHERE email = ?", (self.email,)
        )
        user = self.cursor.fetchone()  
        if user:
            if user[3] == self.password: 
                print("Login successful!")
                return True
            else:
                print("Wrong password!")
                return False
        else:
            print("Email not found!")
            return False
