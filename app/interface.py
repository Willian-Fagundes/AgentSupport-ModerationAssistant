import streamlit as st
from agents.agent_langchain import create_agent_executor, process_message

st.title("Agent Support")
st.caption("Assistente para moderadores — baseado na base de conhecimento pública da Meta.")

# ── Inicialização: executada UMA vez por sessão do navegador ──────────────────
if "agent" not in st.session_state:
    st.session_state.agent = create_agent_executor()
    st.session_state.thread_id = "session-1"

if "messages" not in st.session_state:
    st.session_state.messages = []
if "awaiting_context" not in st.session_state:
    st.session_state.awaiting_context = False

# ── Sidebar ───────────────────────────────────────────────────────────────────
if st.sidebar.button("🗑️ Limpar conversa"):
    # Recria o agente do zero para zerar o histórico do LangGraph
    st.session_state.agent = create_agent_executor()
    st.session_state.thread_id = "session-1"
    st.session_state.messages = []
    st.session_state.awaiting_context = False
    st.rerun()

if st.session_state.awaiting_context:
    st.info("⚠️ Aguardando contexto adicional para continuar.", icon="ℹ️")

# ── Histórico visual ──────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Input ─────────────────────────────────────────────────────────────────────
if prompt := st.chat_input("Digite sua pergunta..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Consultando base de conhecimento..."):
            response, needs_context = process_message(
                pergunta=prompt,
                agent=st.session_state.agent,
                thread_id=st.session_state.thread_id,
            )
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.awaiting_context = needs_context
    