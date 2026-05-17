from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

@tool
def get_user_messages(Chat_History):
    """Recupere as perguntas feitas pelo agente de morderação"""
    return [msg.content for msg in Chat_History if isinstance(msg, HumanMessage)]