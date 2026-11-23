import os
from dotenv import load_dotenv


load_dotenv()

GITHUB_API_URL = os.getenv("GITHUB_API_URL", "https://api.github.com")
GITHUB_URL = os.getenv("GITHUB_URL", "https://github.com")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_LOGIN = os.getenv("GITHUB_LOGIN")
GITHUB_PASSWORD = os.getenv("GITHUB_PASSWORD")
