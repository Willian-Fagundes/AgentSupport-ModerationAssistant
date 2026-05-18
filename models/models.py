from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from openai import OpenAI
from dotenv import load_dotenv
import google.genai as genai
import streamlit as st
import os

load_dotenv(override=True)

api_key = st.secrets["GOOGLE_API_KEY"]

def gemini_model():
    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        google_api_key=api_key,
        temperature=0.4,
        max_tokens=None,
        timeout=15
    )
    return model   

