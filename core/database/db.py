from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase
from core.database.schema import UserChat, MessageModel
from pymongo.asynchronous.collection import AsyncCollection
from core.settings import settings

class MongoDB:
    def __init__(self, url: str = settings.DB_CONNECT) -> None:
        self.client: AsyncMongoClient = AsyncMongoClient(url)
        self.db: AsyncDatabase[UserChat] = self.client[settings.DB_NAME]
        self.collection: AsyncCollection[MessageModel] = self.db["history"]

    async def get_history(self, user_id: int) -> UserChat:
        """Получает историю пользователя
        Args:
            user_id: ID пользователя
        Returns:
            UserChat: История пользователя
        """
        user_data = await self.collection.find_one({"user_id": user_id})
        if user_data:
            return UserChat(user_id=user_id, messages=[MessageModel(role=m["role"], content=m["content"]) for m in user_data["messages"]])
        return UserChat(user_id=user_id, messages=[])

    async def add_message(self, user_id: int, role: str, content: str):
        """Добавляет сообщение в массив истории пользователя
        Args:
            user_id: ID пользователя
            role: Роль пользователя
            content: Сообщение
        Returns:
            None
        """
        new_msg = MessageModel(role=role, content=content).model_dump()
        
        await self.collection.update_one(
            {"user_id": user_id},
            {"$push": {"messages": new_msg}},
            upsert=True
        )

    async def clear_history(self, user_id: int):
        """Сброс контекста
        Args:
            user_id: ID пользователя
        Returns:
            None
        """
        await self.collection.delete_one({"user_id": user_id})

    async def close(self):
        """Закрывает соединение с MongoDB
        Returns:
            None
        """
        await self.client.close()

db_session = MongoDB()