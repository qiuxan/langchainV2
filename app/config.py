import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    model: str = "gpt-4.1-mini"


def load_settings() -> Settings:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is required")

    model = os.getenv("LANGCHAIN_MODEL", "gpt-4.1-mini")

    return Settings(
        openai_api_key=api_key,
        model=model,
    )