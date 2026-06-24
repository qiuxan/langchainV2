from app.config import load_settings


APP_TITLE = "LangChain V2 Learning Assistant"


def get_app_title() -> str:
    return APP_TITLE


def get_startup_message() -> str:
    settings = load_settings()
    return f"{APP_TITLE} using model {settings.model}"


def main() -> None:
    try:
        print(get_startup_message())
    except ValueError as exc:
        print(f"Configuration error: {exc}")


if __name__ == "__main__":
    main()