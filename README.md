#  AI Email Generator using Ollama + Streamlit

This project generates professional emails using **LLM (Ollama)** with a **Streamlit** frontend and a Python backend.  
Users input a few key fields (email type, tone, recipient role, and purpose), and the system generates a clear, natural email body.

---

##  Project Structure
```
EMAIL_GENERATOR/
├── src/
│ ├── server.py # Backend: chatbot class using Ollama
│ └── streamlit_app.py # Frontend: Streamlit UI
├── conversation_history.json # Optional: stores prompt/response history
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md
```

---

##  Features

-  Generates formal/casual/friendly emails
-  Uses `llama3.2:1b` model via [Ollama](https://ollama.com/)
-  History tracking (optional)
-  Local-only, no data leaves your system

---

##  Tech Stack

- [Python 3.10+](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — frontend UI
- [Ollama](https://ollama.com/) — runs LLM locally (no API keys needed)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sourav-paul-JKT/email-generator.git
cd email-generator
```
### 2. Create and Activate Virtual Environment
```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Start Ollama
Ensure Ollama is installed:
https://ollama.com/download

Then start the server:
```
ollama serve
```
Make sure the model llama3.2:1b is available:
```
ollama run llama3.2:1b
```
### 5. Run the App
```
streamlit run src/streamlit_app.py
```

## Future Work
 Add email sending functionality (via SMTP)

 Add export as PDF or copy-to-clipboard

 Docker support

