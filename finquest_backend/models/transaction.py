from pydantic import BaseModel
from datetime import datetime

class AddTransactionRequest(BaseModel):
    amount: float
    category: str
    mode: str

class TransactionResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    category: str
    mode: str
    created_at: datetime

class AddTransactionResponse(BaseModel):
    message: str
    transaction_id: int