<div align="center">

# 🚀 MARA AI Assistant

### Multi-Agent AI Assistant powered by LangGraph, LangChain, RAG & Large Language Models

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_AI-00C853?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-blueviolet?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-4285F4?style=for-the-badge)
![OpenRouter](https://img.shields.io/badge/OpenRouter-LLMs-00A67E?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge)
![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

### 🧠 Intelligent • Modular • Multi-Agent • Retrieval-Augmented Generation

---

*A modern AI assistant capable of intelligent routing, document understanding, coding assistance, career guidance, web search, scheduling, email generation, and much more.*

</div>

---

# 📑 Table of Contents

- Overview
- Features
- Technology Stack
- System Architecture
- Project Workflow
- Folder Structure
- Installation
- Configuration
- Running the Project
- Deployment
- Screenshots
- Future Scope
- Skills Demonstrated
- License
- Author

---

# 📖 Overview

**MARA AI Assistant (Multi-Agent Responsive Assistant)** is an intelligent AI platform developed using modern Agentic AI principles.

Instead of relying on one chatbot for every task, MARA automatically routes user queries to specialized AI agents designed for different domains such as:

- Academic Assistance
- PDF Question Answering
- Coding
- Resume Analysis
- Career Guidance
- Document Generation
- Email Writing
- Calendar Planning
- Web Search
- Research Assistance

The project integrates **LangGraph**, **LangChain**, **Retrieval-Augmented Generation (RAG)**, **FAISS**, **SQLite**, **Gemini**, and **OpenRouter** to provide accurate and context-aware responses.

---

# ✨ Features

## 🤖 Multi-Agent AI

- General Assistant
- Study Agent
- Career Agent
- Research Agent
- PDF Agent
- Coding Agent
- Email Agent
- Calendar Agent
- Document Generator
- Web Search Agent

---

## 📄 Intelligent PDF Chat

- Upload multiple PDFs
- Automatic text extraction
- Text chunking
- Vector embeddings
- Semantic similarity search
- Context-aware question answering

---

## 🧠 Agentic AI Workflow

- Automatic intent detection
- Dynamic routing
- Modular architecture
- Specialized AI agents
- Confidence scoring

---

## 💼 Career Tools

- Resume Analyzer
- ATS Score
- Skills Detection
- Missing Skills
- Improvement Suggestions

---

## 💻 Developer Tools

- Python code generation
- Debugging
- Code explanation
- Best practices
- Optimization suggestions

---

## 📧 Productivity Tools

- Professional Emails
- Formal Reports
- Project Documents
- Calendar Planning
- Task Scheduling

---

## 🌐 Web Search

- Latest information
- Internet search
- Real-time query assistance

---

## 💾 Memory

- SQLite conversation storage
- Long-term memory support

---

## 🎨 User Interface

- Responsive Streamlit interface
- Dark Theme
- Light Theme
- Clean dashboard
- Chat interface

---

## 📤 Export

- Chat Export to PDF

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Frontend | Streamlit |
| Agent Framework | LangGraph |
| AI Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | HuggingFace MiniLM |
| LLM | Gemini 2.5 Flash |
| LLM | OpenRouter |
| Database | SQLite |
| PDF Processing | PyPDF |
| Web Search | DuckDuckGo Search |
| PDF Export | ReportLab |
| Authentication | Streamlit Authenticator |

---

# 🏗 System Architecture

```text
                 User
                   │
                   ▼
        Streamlit Web Interface
                   │
                   ▼
          LangGraph Workflow
                   │
          Intent Detection
                   │
        Dynamic Agent Routing
                   │
 ┌────────┬────────┬─────────┬────────┐
 │        │        │         │        │
 ▼        ▼        ▼         ▼        ▼
Study   Career   Coding    Email   Calendar
Agent   Agent    Agent     Agent     Agent

        PDF Agent
        Research Agent
        Document Agent
        Web Search Agent
        General Agent
                   │
                   ▼
      Gemini / OpenRouter Models
                   │
                   ▼
          Response Generation
                   │
                   ▼
           Streamlit Interface
```

---

# 🔄 Workflow

```text
User Query
     │
     ▼
Intent Detection
     │
     ▼
LangGraph Router
     │
     ▼
Specialized AI Agent
     │
     ▼
LLM Processing
     │
     ▼
Response Generation
     │
     ▼
Display to User
```

---

# 📂 Project Structure

```text
MARA-AI-Assistant/

├── app.py
├── agents.py
├── workflow.py
├── config.py
├── rag.py
├── database.py
├── auth.py
├── export_utils.py
├── resume_analyzer.py
├── web_search.py
├── requirements.txt
├── README.md
├── dark.css
├── light.css
├── .streamlit/
│   └── secrets.toml
├── tools/
├── screenshots/
└── assets/
```

---

# 🚀 Installation

Clone Repository

```bash
git clone https://github.com/komalmand2828-art/mara-ai-assistant.git
```

Enter Project

```bash
cd mara-ai-assistant
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

Create:

```
.streamlit/secrets.toml
```

Add

```toml
GEMINI_API_KEY="YOUR_API_KEY"
OPENROUTER_API_KEY="YOUR_API_KEY"
```

---

# ▶ Running

```bash
streamlit run app.py
```

---

# ☁ Deployment

Deploy easily using:

- Streamlit Community Cloud
- GitHub Repository
- Streamlit Secrets Management

---

# 📷 Screenshots

Create a folder named:

```
screenshots/
```

Recommended images:

- Home Page
- Dashboard
- PDF Upload
- Chat Interface
- Resume Analyzer
- Coding Assistant
- Calendar Agent
- Email Generator
- Document Generator
- Dark Theme

---

# 🚀 Future Enhancements

- Voice Assistant
- OCR Support
- Image Understanding
- Speech-to-Text
- Text-to-Speech
- AI Memory Personalization
- Cloud Database
- Multi-language Translation
- Offline AI Support
- Mobile Application

---

# 🎓 Skills Demonstrated

- Agentic AI
- Multi-Agent Systems
- LangGraph
- LangChain
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Vector Databases
- FAISS
- HuggingFace Embeddings
- LLM Integration
- Streamlit Development
- Python Programming
- SQLite
- API Integration
- Software Architecture
- Git & GitHub
- Cloud Deployment

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

## Komalpreet Kaur

**M.Tech – Artificial Intelligence**

GitHub: https://github.com/komalmand2828-art

---

<div align="center">

### ⭐ If you like this project, consider giving it a Star on GitHub!

Made with ❤️ using Python, Streamlit, LangGraph & Generative AI

</div>
