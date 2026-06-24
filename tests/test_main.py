from app.main import get_app_title


def test_get_app_title():
    assert get_app_title() == "LangChain V2 Learning Assistant"