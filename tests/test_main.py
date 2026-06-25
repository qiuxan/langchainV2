from app.main import get_app_title, get_startup_message
from app.config import Settings


def test_get_app_title():
    assert get_app_title() == "LangChain V2 Learning Assistant"


def test_get_startup_message_uses_config(monkeypatch):
    settings = Settings(
        openai_api_key="test-key",
        model="test-model",
    )

    assert get_startup_message(settings) == "LangChain V2 Learning Assistant ready with model test-model"