from crewai import Agent, LLM
from dotenv import load_dotenv
import os
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)   

blog_researcher = Agent(
    role="Senior YouTube Content Researcher",
    goal="""
    Extract important insights,
    identify key themes,
    summarize complex concepts,
    and create structured research notes.
    """,
    backstory="""
    Expert researcher specializing in
    educational and technical YouTube content.
    Skilled at identifying hidden insights,
    frameworks, examples, and actionable lessons.
    """,
    verbose=True,
    llm=llm
)

blog_writer = Agent(
    role="SEO Technical Blog Writer",
    goal="""
    Transform research into highly engaging,
    SEO-friendly blog posts that are easy
    to read and professionally structured.
    """,
    backstory="""
    Experienced technical writer with expertise
    in converting video content into blogs
    that rank well and maintain reader engagement.
    """,
    verbose=True,
    llm=llm
)