from agents.agent_retriever import invoke_agent

def summarize_content(agent, pergunta: str, validated_content: str, thread_id: str = "session-1") -> str:
    """
    Recebe conteúdo validado e retorna a resposta final estruturada.
    """
    prompt_summarizer = f"""
        Você é um SUMARIZADOR e EXPLICADOR técnico.
        Baseado no conteúdo validado abaixo, gere uma resposta completa, técnica e justificada à pergunta do usuário.

        Pergunta: {pergunta}
        Conteúdo validado: {validated_content}

        Explique e cite onde as informações foram encontradas, referenciando os tópicos da política.
        """
    return invoke_agent(agent, thread_id, prompt_summarizer)