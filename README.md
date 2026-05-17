# Agent Support — Moderation Assistant

A small prototype that uses LangChain, LangGraph and vector search (Chroma) to build a moderation assistant based on a document knowledge base. The UI is a Streamlit app and there is also a simple CLI for quick tests.

**Structure**
- `app/interface.py`: Streamlit front-end (chat UI).
- `app/main.py`: example usage and helper `questions()` function.
- `agents/agent_langchain.py`: agent factory, search/processing logic and a CLI entrypoint.
- `models/models.py`: model factory (Google Gemini wrapper).
- `base/create_db.py`: (helper) create or populate the Chroma DB.
- `conversor_pdf.py`: PDF ingestion utilities.
- `tools/tools.py`: miscellaneous helpers.
- `DB/`: Chroma persistence directory (contains `chroma.sqlite3`).

**Prerequisites**
- Python 3.10+ recommended
- Git (optional)

**Install**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Environment**
Create a `.env` file in the project root with the required API keys. Example:

```env
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
# (optional) OPENAI_API_KEY=your_openai_api_key_here
```

The code expects these environment variables:
- `GOOGLE_API_KEY` — used by `models/gemini_model()` (Gemini/Google GenAI integration)
- `GROQ_API_KEY` — used by the OpenAI-compatible client in `app/main.py` (if used)

**Running**
- Streamlit UI (recommended):

```bash
streamlit run app/interface.py
```

Open the URL shown by Streamlit in your browser.

- CLI (quick tests):

```bash
python agents/agent_langchain.py
```

Type questions in Portuguese/English; enter `quit` to exit the CLI.

**Data / DB**
- The vector DB is persisted under `DB/` (see `DB/chroma.sqlite3`). Do not delete it unless you want to rebuild embeddings.
- Use `base/create_db.py` or `conversor_pdf.py` to ingest documents and build the vector store.

**Security / Notes**
- The agent enforces a strict moderation scope in prompts; review `agents/agent_langchain.py` and `app/main.py` to adjust behavior or thresholds.

**Contributing**
- Feel free to open issues or PRs. Keep secret material out of commits.

**License**
- Apache 2.0.

