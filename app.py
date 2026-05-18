import streamlit as st
from agents.agent_retriever import create_agent_executor
from agents.agent_router import multiagent_pipeline

api_key = st.secrets["GOOGLE_API_KEY"]

st.set_page_config(page_title="Policy Helper (BETA)", layout="wide")
st.title("Policy Helper", text_alignment="center")
st.caption("Pergunte sobre conteúdos/moderação politicas publicas META.", text_alignment= "center")

if "agent" not in st.session_state:
    st.session_state.agent = create_agent_executor()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe histórico de mensagens
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg.get("uncertain"):
            st.warning(msg["content"])
        else:
            st.write(msg["content"])

# Input do chat
if user_input := st.chat_input("Digite sua pergunta..."):
    # Exibe mensagem do usuário
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})

    # Chama o pipeline e exibe resposta
    with st.chat_message("assistant"):
        with st.spinner("Processando..."):
            response, uncertain = multiagent_pipeline(
                user_input,
                st.session_state.agent,
                thread_id="session-1"
            )

        if uncertain:
            st.warning(response)
        else:
            st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "uncertain": uncertain
    })