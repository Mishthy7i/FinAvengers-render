
from db import get_db_connection
from models.transaction import AddTransactionRequest, TransactionResponse
from controllers.rewards_controller import update_user_rewards


def add_transaction(user_id: int, transaction: AddTransactionRequest):
    db = get_db_connection()
    cursor = db.cursor()
    
    cursor.execute("""
        INSERT INTO transactions (user_id, amount, category, mode)
        VALUES (%s, %s, %s, %s)
    """, (user_id, transaction.amount, transaction.category, transaction.mode))
    db.commit()
    
    cursor.close()
    db.close()

    # Update XP & Badges after transaction
    update_user_rewards(user_id, transaction.amount)

    return {"message": "Transaction added successfully"}

def get_user_transactions(user_id: int):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, amount, category, mode, created_at
        FROM transactions
        WHERE user_id = %s
    """, (user_id,))
    transactions = cursor.fetchall()
    cursor.close()
    db.close()
    return transactions

def update_user_rewards(user_id: int, amount: float):
    db = get_db_connection()
    cursor = db.cursor()

    xp_earned = int(amount // 100) * 10
    cursor.execute("SELECT xp FROM users WHERE id = %s", (user_id,))
    current_xp = cursor.fetchone()[0] or 0
    new_xp = current_xp + xp_earned

    cursor.execute("UPDATE users SET xp = %s WHERE id = %s", (new_xp, user_id))
    db.commit()

    badge = None
    if new_xp >= 500:
        badge = "Master Saver"
    elif new_xp >= 200:
        badge = "Budget Ninja"
    elif new_xp >= 100:
        badge = "Smart Spender"

    if badge:
        cursor.execute("UPDATE users SET badges = %s WHERE id = %s", (badge, user_id))
        db.commit()

    cursor.close()
    db.close()


