from app.config import load_settings
from app.llm import create_chat_model


APP_TITLE = "LangChain V2 Learning Assistant"


def get_app_title() -> str:
    return APP_TITLE


def get_startup_message() -> str:
    settings = load_settings()
    model = create_chat_model(settings)
    return f"{APP_TITLE} ready with model {model.model_name}"


def main() -> None:
    try:
        print(get_startup_message())
    except ValueError as exc:
        print(f"Configuration error: {exc}")


if __name__ == "__main__":
    main()