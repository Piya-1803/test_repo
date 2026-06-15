def login(user, password):
    db.execute(f"SELECT * FROM users WHERE password={password}")
    return db.fetchone()
