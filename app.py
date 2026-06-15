def login(users, password):
    db.execute(f"SELECT * FROM users WHERE password={password}")
    return db.fetchone()
