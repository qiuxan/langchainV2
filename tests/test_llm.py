from app.config import Settings
from app.llm import create_chat_model


def test_create_chat_model_uses_settings():
    settings = Settings(
        openai_api_key="test-key",
        model="test-model",
    )

    model = create_chat_model(settings)

    assert model.model_name == "test-model"
    assert model.temperature == 0.2
    assert model.openai_api_key.get_secret_value() == "test-key"