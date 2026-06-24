import pytest

from app.config import load_settings


def test_load_settings_reads_required_api_key(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.delenv("LANGCHAIN_MODEL", raising=False)

    settings = load_settings()

    assert settings.openai_api_key == "test-key"
    assert settings.model == "gpt-4.1-mini"


def test_load_settings_reads_model(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("LANGCHAIN_MODEL", "custom-model")

    settings = load_settings()

    assert settings.model == "custom-model"


def test_load_settings_requires_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        load_settings()