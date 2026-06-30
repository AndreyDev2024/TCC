from pathlib import Path

from dotenv import load_dotenv


def carregar_env():
    caminho_env = Path(__file__).resolve().parents[1] / ".env"
    load_dotenv(caminho_env)
