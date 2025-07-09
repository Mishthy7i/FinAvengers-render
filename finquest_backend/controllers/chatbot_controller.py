import os
import requests
from fastapi import HTTPException
from db import get_db_connection

def get_user_profile(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT name, dob, salary FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    finally:
        cursor.close()
        conn.close()

def ask_chatbot(user_id: int, question: str):
    try:
        user = get_user_profile(user_id)

        # Craft custom system prompt using user data
        system_prompt = (
            f"You are a helpful personal finance assistant for a user named {user['name']}, "
            f"who was born in {user['dob']} and earns ₹{user['salary']} per month. "
            f"Provide personalized answers and financial tips based on that."
        )

        headers = {
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json"
        }

        body = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
        res = response.json()

        return {"answer": res["choices"][0]["message"]["content"].strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))