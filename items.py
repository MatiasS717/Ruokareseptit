import db

def add_item(title, ingredients, recipe, classification, user_id):
    sql = """INSERT INTO items (title, ingredients, recipe, classification, user_id)
             VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, ingredients, recipe, classification, user_id])