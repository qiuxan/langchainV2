from langchain_core.messages import HumanMessage

from app.config import Settings
from app.llm import create_chat_model


def ask_once(settings: Settings, question: str) -> str:
    model = create_chat_model(settings)
    response = model.invoke([HumanMessage(content=question)])
    return response.content