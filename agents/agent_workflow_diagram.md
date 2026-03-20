# Multi-Data Source RAG Agent Workflow

This diagram illustrates the step-by-step workflow of the intelligent tool-calling agent designed in `agents.ipynb`. The agent orchestrates between three separate data retrieval systems to determine the best source of information based on a user's prompt.

```mermaid
graph TD
    %% Define Styles
    classDef llm fill:#4caf50,stroke:#388e3c,stroke-width:2px,color:#fff
    classDef db fill:#ff9800,stroke:#f57c00,stroke-width:2px,color:#fff
    classDef process fill:#2196f3,stroke:#1976d2,stroke-width:2px,color:#fff
    classDef user fill:#9c27b0,stroke:#7b1fa2,stroke-width:2px,color:#fff
    classDef error fill:#f44336,stroke:#d32f2f,stroke-width:2px,color:#fff

    %% User Input
    User((User Input)):::user
    Prompt[hwchase17/openai-functions-agent Prompt]:::process

    %% Core Components
    AgentExecutor{LangChain Agent Executor}:::process
    ChatGroq[ChatGroq LLM <br/> llama-3.1-8b-instant]:::llm
    
    %% Tool Registration
    ToolsHub[[Tools Registry]]:::process
    
    %% Data Source 1: Wikipedia
    subgraph "Wikipedia Tool"
        WikiWrapper[WikipediaAPIWrapper]
        WikiRun[WikipediaQueryRun]
        WikiWrapper --> WikiRun
    end

    %% Data Source 2: RAG Pipeline
    subgraph "Custom PDF / Web RAG Pipeline"
        WebLoader(WebBaseLoader)
        Splitter[RecursiveCharacterTextSplitter]
        Embeddings[GoogleGenerativeAIEmbeddings]
        FAISS[(FAISS Vector DB)]:::db
        Retriever[as_retriever]
        RetrieverTool[create_retriever_tool <br/> 'langsmith_search']
        
        WebLoader --> Splitter --> Embeddings --> FAISS --> Retriever --> RetrieverTool
    end

    %% Data Source 3: Arxiv
    subgraph "Arxiv Tool"
        ArxivWrapper[ArxivAPIWrapper]
        ArxivRun[ArxivQueryRun]
        ArxivWrapper --> ArxivRun
    end

    %% Connections
    WikiRun -->|Register| ToolsHub
    RetrieverTool -->|Register| ToolsHub
    ArxivRun -->|Register| ToolsHub

    User -->|Question/Prompt| Prompt
    Prompt --> AgentExecutor
    
    ToolsHub --> AgentExecutor
    ChatGroq --> AgentExecutor

    AgentExecutor -.->|Decides: General Knowledge| WikiRun
    AgentExecutor -.->|Decides: Deep Tech/Docs| RetrieverTool
    AgentExecutor -.->|Decides: Scientific Papers| ArxivRun

    WikiRun -.->|Results| ChatGroq
    RetrieverTool -.->|Results| ChatGroq
    ArxivRun -.->|Results| ChatGroq

    ChatGroq -->|Final Response| Output((Final Answer)):::user
```

### Flow Breakdown:
1. **Data Ingestion (Bottom Layer):** The notebook establishes three separate pipelines: Wikipedia API for natural-language facts, Arxiv API for academic publications, and a FAISS database containing document embeddings scraped from Langsmith docs.
2. **Tool Consolidation:** The three disparate data pipelines are wrapped into uniform LangChain "Tools".
3. **Core Orchestration:** The `AgentExecutor` takes the user prompt, utilizes Groq's high-speed logical reasoning capacity (`ChatGroq`), and dynamically chooses *which* tool to query based on what information is needed to fulfill the instruction.
4. **Final Synthesis:** The returned raw data from the chosen tool is fed back to the underlying LLM, which synthesizes a robust, natural-sounding answer for the user.
