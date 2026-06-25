from app.main import get_app_title, get_startup_message


def test_get_app_title():
    assert get_app_title() == "LangChain V2 Learning Assistant"


def test_get_startup_message_uses_config(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("LANGCHAIN_MODEL", "test-model")

    assert get_startup_message() == "LangChain V2 Learning Assistant ready with model test-model"