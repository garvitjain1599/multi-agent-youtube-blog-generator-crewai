from crewai import Crew, Process

from agents import (
    blog_researcher,
    blog_writer
)

from tasks import (
    research_task,
    writing_task
)


crew = Crew(
    agents=[
        blog_researcher,
        blog_writer
    ],
    tasks=[
        research_task,
        writing_task
    ],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(
    inputs={
        "youtube_url":
        "https://www.youtube.com/watch?v=aircAruvnKk"
    }
)

with open("blog.md", "w", encoding="utf-8") as f:
    f.write(str(result))

print(result)