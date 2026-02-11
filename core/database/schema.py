
from pydantic import BaseModel
from typing import List, Literal

class MessageModel(BaseModel):
    role: Literal["user", "model"]
    content: str

class UserChat(BaseModel):
    user_id: int
    messages: List[MessageModel] = []