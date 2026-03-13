# Langchain & Groq AI Assistant Project 🤖

Welcome to my AI Assistant project! I built this project to explore and learn how to integrate **Langchain**, **Groq's blazing-fast inference API**, **FastAPI**, and **Streamlit**. 

This repository contains two main parts: a standalone Streamlit chatbot and a client-server architecture using Langserve to generate an essay about any topic.

## 🌟 Features

- **Standalone AI Chatbot (`AIAssistant.py`)**: A simple, interactive UI built with Streamlit that answers general queries quickly using Groq's `llama-3.1-8b-instant` model.
- **Langserve API Server (`api/app.py`)**: A FastAPI backend that serves Langchain models and chains as REST APIs. It includes an endpoint specifically designed to write 1000-word essays based on a specific prompt template.
- **Streamlit Client (`api/client.py`)**: A frontend app that communicates with the FastAPI backend to request and display generated essays.
- **Langchain Tracing**: Integrated with LangSmith (via `LANGCHAIN_TRACING_V2`) for monitoring and debugging LLM calls under the hood.

## 📂 Project Structure

```text
├── .env                  # Environment variables (you'll need to create this!)
├── requirements.txt      # Python dependencies
├── AIAssistant.py        # Standalone Streamlit chatbot app
└── api/
    ├── app.py            # FastAPI server using Langserve
    └── client.py         # Streamlit frontend client that talks to the Langserve API
```

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   I've included a `requirements.txt` file (and you can also use `uv` since `uv.lock` is included!).
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Environment Variables:**
   Create a `.env` file in the root directory and add your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   LANGCHAIN_API_KEY=your_langchain_smith_api_key_here
   ```

## 🚀 Running the Applications

Depending on what you want to test, you can run different parts of the project:

### 1. Standalone Chatbot
To run the basic AI Chatbot UI:
```bash
streamlit run AIAssistant.py
```

### 2. API Server & Client Architecture
First, start the FastAPI/Langserve backend from the `api` directory:
```bash
cd api
python app.py
```
*(The server will run on `http://localhost:8000`)*

Then, open a new terminal window, navigate to the `api` directory again, and start the Streamlit client:
```bash
cd api
streamlit run client.py
```

## 💻 Technologies Used

- **Python** 🐍
- **Langchain & Langserve** for LLM orchestration and API routing
- **Groq** for high-speed model inference (`llama-3.1-8b-instant`)
- **Streamlit** for building the interactive web UIs
- **FastAPI & Uvicorn** for the robust backend server

## 🤝 Contributing & Feedback

Feel free to fork this project, submit pull requests, or open an issue if you have suggestions. This is a learning project, so I'm always open to ideas on how to improve the code!

---
*Happy Coding!* 🚀
