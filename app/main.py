from app.config import load_settings,Settings
from app.llm import create_chat_model
from app.chat import ask_once


APP_TITLE = "LangChain V2 Learning Assistant"


def get_app_title() -> str:
    return APP_TITLE


def get_startup_message(settings: Settings) -> str:
    return f"{APP_TITLE} ready with model {settings.model}"


def main() -> None:
    try:
        settings = load_settings()
        print(get_startup_message(settings))
        answer = ask_once(settings, "One sentence, what is LangChain?")
        print(answer)
    except ValueError as exc:
        print(f"Configuration error: {exc}")


if __name__ == "__main__":
    main()