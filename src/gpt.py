from core.settings import settings
from core.database.schema import UserChat
from google.genai import types
from google.genai import Client
import logging
client = Client(api_key=settings.GEMINI_API_KEY)

def get_chat_response(history: UserChat, user_message: str) -> str:
    """Генерирует ответ через новый SDK google-genai."""
    
    model_id = "gemini-3-flash-preview"
    
    contents = []
    for m in history.messages[-20:]:
        role = "user" if m.role == "user" else "model"
        contents.append(types.Content(role=role, parts=[types.Part(text=m.content)]))
    
    contents.append(types.Content(role="user", parts=[types.Part(text=user_message)]))

    try:
        response = client.models.generate_content(
            model=model_id,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction="Ты — дружелюбный ассистент в Telegram. Отвечай кратко и по делу.",
                temperature=0.7,
            )
        )
        return response.text
    except Exception as e:
        logging.error(f"GenAI Error: {e}")
        return "Произошла ошибка при генерации ответа. Попробуйте позже."