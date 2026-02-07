# vulnerable_app.py - Test file with intentional security vulnerabilities
# This file contains HIGH severity issues for testing security scanner blocking

import os
import pickle
import hashlib
import sqlite3
import pandas

# HIGH: Hardcoded credentials
DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyz"
SECRET_TOKEN = "super_secret_token_12345"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

# HIGH: SQL Injection vulnerability
def get_user_by_id(user_id):
    """Vulnerable to SQL injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Concatenating user input directly into SQL query
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    return cursor.fetchone()

# HIGH: SQL Injection in search
def search_products(search_term):
    """Another SQL injection point"""
    query = f"SELECT * FROM products WHERE name LIKE '%{search_term}%'"
    return execute_query(query)

# HIGH: Command Injection
def ping_server(hostname):
    """Allows arbitrary command execution"""
    os.system("ping -c 1 " + hostname)

# HIGH: Another command injection
def backup_database(filename):
    """Vulnerable command execution"""
    os.system(f"mysqldump -u root -p{DATABASE_PASSWORD} > {filename}")

# HIGH: Unsafe deserialization with pickle
def load_user_session(session_file):
    """Pickle can execute arbitrary code during deserialization"""
    with open(session_file, 'rb') as f:
        return pickle.load(f)

# HIGH: Dynamic code execution with eval
def calculate_expression(user_expression):
    """Allows arbitrary code execution"""
    return eval(user_expression)

# HIGH: exec() usage
def run_user_code(code_string):
    """Executes arbitrary Python code"""
    exec(code_string)

# MEDIUM: Weak cryptographic hash (MD5)
def hash_password(password):
    """MD5 is not suitable for password hashing"""
    return hashlib.md5(password.encode()).hexdigest()

# MEDIUM: Insecure random for security purposes
import random
def generate_token():
    """Using random instead of secrets module"""
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(20))

# LOW: Broad exception catching (not HIGH but still an issue)
def process_data(data):
    try:
        return data.process()
    except:
        pass

# Some clean code to mix it in
def validate_email(email):
    """This function is fine"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def calculate_total(items):
    """This function is also clean"""
    return sum(item.price for item in items)
