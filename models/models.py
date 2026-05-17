from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from openai import OpenAI
from dotenv import load_dotenv
import google.genai as genai
import os

load_dotenv(override=True)

def gemini_model():
    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        google_api_key=os.environ.get("GOOGLE_API_KEY"),
        temperature=0.4,
        max_tokens=None,
        timeout=15
    )
    return model   

