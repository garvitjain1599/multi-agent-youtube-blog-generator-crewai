# 🎥 Multi-Agent YouTube-to-Blog Generator with Crew AI

An AI-powered application that converts YouTube videos into well-structured, SEO-friendly blog articles using a multi-agent workflow built with CrewAI and Groq LLMs.

## 🚀 Overview

This project leverages multiple AI agents to automate the process of transforming YouTube video content into professional blog posts. The system extracts video transcripts, performs content analysis, identifies key insights, and generates a polished blog article in Markdown format.

The workflow follows a collaborative multi-agent architecture where each agent specializes in a specific task, resulting in higher-quality output and better content organization.

---

## ✨ Features

- Multi-agent architecture using CrewAI
- Automatic YouTube transcript extraction
- Video metadata retrieval
- AI-powered content analysis
- Blog generation from video content
- Structured markdown output
- Modular and extensible design
- Fast inference using Groq LLMs

---

## 🏗️ System Architecture

```text
YouTube URL
    │
    ▼
Transcript & Metadata Extraction
    │
    ▼
Research Agent
(Content Analysis)
    │
    ▼
Structured Research Notes
    │
    ▼
Blog Writer Agent
(Content Generation)
    │
    ▼
Markdown Blog Article
```

---

## 🛠️ Tech Stack

- Python
- CrewAI
- Groq LLMs
- YouTube Transcript API
- yt-dlp
- python-dotenv

---

## 📂 Project Structure

```text
.
├── agents.py        # Agent definitions
├── tasks.py         # Task definitions
├── tools.py         # Custom YouTube research tool
├── crew.py          # Crew orchestration
├── .env             # Environment variables
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-to-blog-generator.git
cd youtube-to-blog-generator
```

### Create Virtual Environment

```bash
conda create -n youtube-blog python=3.11
conda activate youtube-blog
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Usage

Update the YouTube URL in `crew.py`:

```python
inputs = {
    "youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

Run the application:

```bash
python crew.py
```

The generated blog article will be displayed in the terminal and can optionally be saved as a Markdown file.

---

## 🤖 Agents

### YouTube Content Researcher

Responsible for:

- Extracting insights from transcripts
- Identifying key concepts and takeaways
- Organizing research notes
- Summarizing video content

### Technical Blog Writer

Responsible for:

- Converting research into a blog article
- Structuring content into sections
- Improving readability and flow
- Generating markdown output

---

## 📋 Workflow

1. User provides a YouTube video URL.
2. The custom research tool extracts the transcript and metadata.
3. The Research Agent analyzes the video content.
4. Research findings are passed to the Blog Writer Agent.
5. The Blog Writer Agent generates a complete blog article.
6. Final output is returned in Markdown format.

---

## 🎯 Learning Outcomes

This project demonstrates:

- Multi-Agent AI Systems
- Agent Orchestration with CrewAI
- Prompt Engineering
- LLM Application Development
- Tool Integration
- Automated Content Generation
- Generative AI Workflows

---

## 🔮 Future Enhancements

- Streamlit Web Interface
- PDF Export Support
- SEO Keyword Optimization
- Multi-Language Blog Generation
- ChromaDB-Based RAG for Long Videos
- Blog Review Agent
- Fact-Checking Agent
- Human Feedback Loop

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Garvit Jain**

Data Scientist | Generative AI Enthusiast | AI Application Developer
