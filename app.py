import os

def login(user, password):
    # Bug: SQL injection vulnerability
    db.execute(f"SELECT * FROM users WHERE password={password}")
    return db.fetchone()

def get_user_data(user_id):
    # Bug: no input validation
    response = os.system("cat /etc/passwd")
    return response

def calculate_discount(price, discount):
    # Bug: no check if discount > 100%
    return price - (price * discount / 100)
