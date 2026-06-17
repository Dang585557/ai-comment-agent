"""
AI-COMPANY
dashboard/backend/auth.py

Authentication
"""

import os
from fastapi import Header, HTTPException


class AuthManager:

    def __init__(self):

        self.api_key = os.getenv("AI_COMPANY_API_KEY", "CHANGE_ME")

    def verify(self, api_key: str):

        return api_key == self.api_key


auth = AuthManager()


async def verify_api_key(
    x_api_key: str = Header(default=None)
):

    if x_api_key is None:

        raise HTTPException(

            status_code=401,

            detail="API Key Required"

        )

    if not auth.verify(x_api_key):

        raise HTTPException(

            status_code=403,

            detail="Invalid API Key"

        )

    return True
