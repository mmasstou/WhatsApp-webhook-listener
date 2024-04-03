# config.py
import sys
import os
from dotenv import load_dotenv
import logging
from flask import Flask
from openai import OpenAI

__all__ = ["Config"]


class Config:
    app: Flask = None

    def __init__(self, app: Flask, env_path: str) -> None:
        load_dotenv(env_path)
        self.app = app
        app.config["ACCESS_TOKEN"] = os.getenv("ACCESS_TOKEN")
        app.config["YOUR_PHONE_NUMBER"] = os.getenv("YOUR_PHONE_NUMBER")
        app.config["APP_ID"] = os.getenv("APP_ID")
        app.config["APP_SECRET"] = os.getenv("APP_SECRET")
        app.config["RECIPIENT_WAID"] = os.getenv("RECIPIENT_WAID")
        app.config["VERSION"] = os.getenv("VERSION")
        app.config["PHONE_NUMBER_ID"] = os.getenv("PHONE_NUMBER_ID")
        app.config["VERIFY_TOKEN"] = os.getenv("VERIFY_TOKEN")
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        app.config["OpenAI_CLIENT"] = OpenAI(api_key=OPENAI_API_KEY)

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            stream=sys.stdout,
        )

    def EditRecipintWaid(self, recipint_waid):
        self.app.config["RECIPIENT_WAID"] = recipint_waid