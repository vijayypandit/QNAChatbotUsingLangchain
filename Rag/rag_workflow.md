# RAG Workflow Diagram

This document contains a Mermaid diagram illustrating the step-by-step Retrieval-Augmented Generation (RAG) process that occurs in the `chain.ipynb` notebook.

You can view this diagram using a Markdown previewer in your IDE that supports Mermaid, or on GitHub.

```mermaid
graph TD
    %% Data Ingestion Flow
    A[📄 attention.pdf] -->|PyPDFLoader| B(Extracted Text Document)
    B -->|RecursiveCharacterTextSplitter| C(Text Chunks <br/>1000 chars)
    C -->|GoogleGenerativeAIEmbeddings| D[Vector Embeddings]
    D -->|FAISS| E[(FAISS Vector Database)]

    %% Query and Retrieval Flow
    F[👤 User Query] -->|GoogleGenerativeAIEmbeddings| G[Query Vector Embedding]
    G -->|Similarity Search<br/>db.as_retriever| E
    E -->|Retrieve Top Matches| H(Relevant Context Chunks)

    %% Generation Flow
    H -->|Stuff Context| I{ChatPromptTemplate}
    F -->|Insert Question| I
    I -->|create_stuff_documents_chain| J((🤖 LLM: ChatGroq<br/>llama-3.1-8b))
    J -->|create_retrieval_chain| K[✨ Final Answer]

    %% Explicit Inline Styles (Provides better compatibility)
    style A fill:#f9d0c4,stroke:#333,stroke-width:2px,color:#000
    style B fill:#c4ddf9,stroke:#333,stroke-width:2px,color:#000
    style C fill:#c4ddf9,stroke:#333,stroke-width:2px,color:#000
    style D fill:#c4f9d0,stroke:#333,stroke-width:2px,color:#000
    style E fill:#f9e7c4,stroke:#333,stroke-width:2px,color:#000
    style F fill:#f9d0c4,stroke:#333,stroke-width:2px,color:#000
    style G fill:#c4f9d0,stroke:#333,stroke-width:2px,color:#000
    style H fill:#c4ddf9,stroke:#333,stroke-width:2px,color:#000
    style I fill:#c4ddf9,stroke:#333,stroke-width:2px,color:#000
    style J fill:#c4f9d0,stroke:#333,stroke-width:2px,color:#000
    style K fill:#f9d0c4,stroke:#333,stroke-width:2px,color:#000
```

### Key Components
1. **Red/Pink Blocks**: Inputs and Outputs (Files, Queries, Answers).
2. **Blue Blocks**: LangChain Processing steps (Loaders, Splitters, Prompts).
3. **Green Blocks**: AI Models generating data (Google Embeddings, Groq LLM).
4. **Yellow/Orange Block**: The Vector Database (FAISS).
