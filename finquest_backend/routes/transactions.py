
from fastapi import APIRouter, Depends
from typing import List
from models.transaction import (
    AddTransactionRequest, 
    TransactionResponse, 
    AddTransactionResponse
)
from controllers.transaction_controller import (
    add_transaction,
    get_user_transactions,
)
from utils.auth_utils import jwt_bearer
from db import get_db_connection

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/add", response_model=AddTransactionResponse)
def add_transaction_route(
    transaction: AddTransactionRequest,
    user_id: int = Depends(jwt_bearer)
):
    return add_transaction(user_id, transaction)

@router.get("/", response_model=List[TransactionResponse])
def get_transactions_route(
    user_id: int = Depends(jwt_bearer),
):
    return get_user_transactions(user_id)

@router.get("/rewards")
def get_user_rewards(user_id: int = Depends(jwt_bearer)):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT xp, badges FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return {"xp": result[0], "badge": result[1]}

#  XP & Badge Update Function 
def update_rewards(user_id, xp_gain, new_badge=None):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("UPDATE users SET xp = xp + %s WHERE id = %s", (xp_gain, user_id))
    
    if new_badge:
        cursor.execute("UPDATE users SET badges = %s WHERE id = %s", (new_badge, user_id))
    
    db.commit()
    cursor.close()
    db.close()
