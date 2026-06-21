from crewai import Task
from agents import blog_researcher, blog_writer
from tools import yt_tool


research_task = Task(
    description="""
    Analyze the YouTube video:

    {youtube_url}

    Extract:

    1. Main Topic
    2. Core Concepts
    3. Important Frameworks
    4. Actionable Insights
    5. Key Examples
    6. Important Quotes
    7. Final Summary

    Use the YouTube Research Tool.
    """,

    expected_output="""
    Comprehensive structured research report.
    """,

    tools=[yt_tool],
    agent=blog_researcher
)


writing_task = Task(
    description="""
    Using the research report:

    Create a detailed blog article.

    Requirements:

    - SEO-friendly title
    - Hook introduction
    - Clear H2 and H3 sections
    - Real-world examples
    - Bullet point summaries
    - Actionable takeaways
    - Conclusion
    - FAQ section

    Output Markdown only.
    """,

    expected_output="""
    Professional markdown blog article.
    """,

    agent=blog_writer,
    context=[research_task]
)