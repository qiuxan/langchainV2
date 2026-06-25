from langchain_openai import ChatOpenAI

from app.config import Settings


def create_chat_model(settings: Settings) -> ChatOpenAI:
    return ChatOpenAI(
        model=settings.model,
        api_key=settings.openai_api_key,
        temperature=0.2,
    )