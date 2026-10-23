# LangChain Essay and Poem Generator

This project provides a small text-generation application with a FastAPI/LangServe backend and a Streamlit web client. Enter a topic in the client to generate:

- A 100-word essay using OpenAI.
- A 100-word poem using the local Ollama `llama2` model.

## Project files

- `app.py` creates the FastAPI server and exposes the OpenAI, essay, and poem LangServe routes.
- `client.py` creates the Streamlit interface and sends requests to the essay and poem routes.
- `requirements.txt` lists the Python dependencies.

## Requirements

- Python 3.9 or later.
- An OpenAI API key with API access.
- [Ollama](https://ollama.com/) installed and available locally, with the `llama2` model downloaded.

## Run locally on Windows

Open PowerShell in the project directory and create/activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, allow scripts for the current terminal session and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

Create a `.env` file in the project directory and add your OpenAI key:

```dotenv
OPENAI_API_KEY=your_openai_api_key
```

Keep the key private and do not commit `.env` to source control.

Download the Ollama model before starting the application:

```powershell
ollama pull llama2
```

Make sure Ollama is running. On Windows, starting the Ollama application normally starts its local service. If needed, start it in a separate terminal with:

```powershell
ollama serve
```

### Start the API

In the project directory, with the virtual environment active:

```powershell
python app.py
```

The API listens at `http://localhost:8000`. FastAPI's interactive API documentation is available at `http://localhost:8000/docs`.

### Start the Streamlit client

Keep the API running, open a second PowerShell window in the project directory, activate the same virtual environment, and run:

```powershell
.\venv\Scripts\Activate.ps1
streamlit run client.py
```

Open the local URL printed by Streamlit (typically `http://localhost:8501`) in your browser. The client sends requests to the API at `http://localhost:8000`.

## API routes

The backend registers these LangServe routes:

- `POST /openai/invoke` — invokes the OpenAI chat model directly.
- `POST /essay/invoke` — generates an essay from a `topic`.
- `POST /poem/invoke` — generates a poem from a `topic` using Ollama.

Example essay request:

```powershell
Invoke-RestMethod -Method Post `
  -Uri http://localhost:8000/essay/invoke `
  -ContentType "application/json" `
  -Body '{"input":{"topic":"renewable energy"}}'
```

## Troubleshooting

- **OpenAI authentication error:** Check that `.env` is in the project directory and that `OPENAI_API_KEY` is set to a valid key.
- **Ollama connection or model error:** Confirm Ollama is running and that `ollama list` includes `llama2`. If it is missing, run `ollama pull llama2`.
- **Client cannot connect:** Start the API before using the Streamlit client, and verify that the API is listening on port `8000`.
