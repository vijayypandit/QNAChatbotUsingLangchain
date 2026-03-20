# 🤖 Advanced LangChain Ecosystem: RAG, Agents & API Services

Welcome to my comprehensive AI Assistant and RAG integration project! I built this repository to showcase modern LLM orchestration using **LangChain**, **Groq's blazing-fast inference API**, **FastAPI**, and **Streamlit**. 

This repository serves as a multi-faceted playground demonstrating production-grade AI capabilities—from interactive chatbots to advanced tool-calling agents capable of synthesizing information across multiple disjoint data sources.

## 🌟 Key Features & Architecture

- **🧠 Multi-Data Source RAG Agent (`agents/agents.ipynb`)**: 
  A state-of-the-art Jupyter Notebook demonstrating a fully autonomous Retrieval-Augmented Generation (RAG) architecture. The agent utilizes **function calling** to intelligently route queries and pull contextual data across three separate domain tools:
  - **WikipediaTool (`WikipediaQueryRun`)**: For general encyclopedic knowledge.
  - **ArxivTool (`ArxivQueryRun`)**: For up-to-date academic research and scientific papers.
  - **Web Scraper & VectorDB (`WebBaseLoader` + FAISS)**: For chunking, embedding, and retrieving localized domain knowledge.

- **💬 Streamlit AI ChatBot (`AIchatBot/AIAssistant.py`)**: 
  A standalone, interactive conversational UI built with Streamlit. It leverages Groq's ultra-low latency `llama-3.1-8b-instant` model to deliver real-time, fluid conversations.

- **⚡ LangServe API Backend (`api/app.py` & `api/client.py`)**: 
  A robust client-server implementation. The backend exposes LangChain runnable chains as RESTful API endpoints via **FastAPI** and **LangServe**, while the Streamlit client acts as the frontend consumer layer (specifically built for structured generation tasks like writing multi-topic essays).

- **🔍 LangSmith Observability**: 
  Embedded `LANGCHAIN_TRACING_V2` functionality for precise monitoring, latency tracking, and debugging of complex LLM execution chains and agent thoughts under the hood.

---

## 📂 Project Structure

```text
├── .env                  # Standard environment variables
├── requirements.txt      # Python package dependencies
├── AIchatBot/
│   └── AIAssistant.py    # Interative Streamlit AI Chatbot Application
├── Rag/                  # Directory for standalone RAG experiments
├── agents/
│   └── agents.ipynb      # Multi-Data Source RAG Tool-Calling Demo
└── api/
    ├── app.py            # FastAPI/LangServe backend server
    └── client.py         # Streamlit frontend interacting with the API
```

---

## 🛠️ Installation & Setup

If you want to test out this project, interact with the API, or run the RAG agent demo, follow these setup steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Initialize a Virtual Environment**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   (Ensure you have `langchain`, `langchain-groq`, `streamlit`, `faiss-cpu`, `wikipedia`, `arxiv`, etc. installed)
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory and securely add your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   LANGCHAIN_API_KEY=your_langchain_api_key_here
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_PROJECT=your_project_name
   ```

---

## 🚀 How to Run the Demos

You can jump right in and test the different components of the project!

### 1. Test the Multi-Data Source RAG Agent (Notebook)
Want to see the AI autonomously decide which tool to use?
1. Open up **`agents/agents.ipynb`** in your favorite Jupyter environment (like VS Code).
2. Execute the cells sequentially.
3. Watch as the integrated `AgentExecutor` intelligently passes prompts through Groq and decides whether to perform a web search, query the Arxiv archive, or pull embeddings from the FAISS database!

### 2. Run the AI ChatBot Assistant
Want a quick, interactive chat?
1. Open your terminal at the root of the project.
2. Run the Streamlit application:
   ```bash
   streamlit run AIchatBot/AIAssistant.py
   ```
3. A browser tab will open where you can chat immediately with the optimized Groq model.

### 3. Start the Client-Server API Demo
Want to test the RESTful architecture and decoupled API system?
1. **Start the Backend Server**:
   ```bash
   cd api
   python app.py
   ```
   *(The FastAPI server will boot up and bind to `http://localhost:8000`)*

2. **Start the Frontend Client**:
   Open a *second* terminal window in the `api` directory and run:
   ```bash
   cd api
   streamlit run client.py
   ```
   *(This launches a distinct UI that makes real-time HTTP requests to your FastAPI backend!)*

---

## 💻 Technical Stack

- **Core Concepts:** Retrieval-Augmented Generation (RAG), Autonomous Tool Calling, LLM API Serving
- **Frameworks:** LangChain, LangServe, FastAPI, Uvicorn, Streamlit
- **LLM Provider:** Groq
- **Database & Retrieval:** FAISS (Vector DB), Wikipedia API, Arxiv API, WebBaseLoader 

---
*Happy Coding & Exploring!* 🚀
