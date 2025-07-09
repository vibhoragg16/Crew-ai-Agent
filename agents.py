from crewai import Agent
from tools import yt_tool

blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal = 'Get the relevent video from the topic {topic} from YT channel',
    verbose =True,
    memory = True,
    backstory=(
        "Expert in understanding videos in AI Data Science, MAchine learning and Gen AI and provide suggestion"
    ),
    tools=[],
    allow_delegation=True
)


blog_writer = Agent(
    role='Blog Writer',
    goal = 'Narrate compelling tech stories about the video {topic} from YT channel',
    verbose =True,
    memory = True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[],
    allow_delegation=False
)

