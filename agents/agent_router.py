from agents.agent_retriever import invoke_agent, search_kb, is_uncertain
from agents.agent_summarizer import summarize_content


def multiagent_pipeline(pergunta: str, agent, thread_id: str = "session-1") -> tuple[str, bool]:
    # Busca
    kb = search_kb(pergunta)
    if kb is None:
        return (
            "Não encontrei informações suficientes na base de conhecimento para responder com precisão.\n"
            "O conteúdo pode não ser violatório!",
            True
        )

    # Sumarização / Resposta final
    final_answer = summarize_content(agent, pergunta,kb, thread_id)

    if is_uncertain(final_answer):
        return (
            f"{final_answer}\n\n"
            "Para que eu possa ajudar melhor, você poderia fornecer mais contexto?",
            True
        )

    return final_answer, False