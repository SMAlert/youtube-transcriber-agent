import os
import random

from google.adk.agents import Agent
from google.adk.models.gemini import GeminiModel

model = GeminiModel(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

def summarize_youtube_video(url: str) -> str:
    summaries = [
        "This video breaks down AI agents in simple terms: what they are, why they matter, and how to build one.",
        "The video explains the importance of consistency and discipline in personal growth with real-life examples.",
        "It's all about coding tips, debugging faster, and writing clean reusable functions.",
        "A straight-to-point talk on finance basics: saving early, compounding power, and avoiding debt traps.",
        "Motivational push to stop procrastinating and start building your dream project today."
    ]
    return random.choice(summaries)

root_agent = Agent(
    name="sample-agent",
    model=model,
    description="Sample-agent",
    instruction="""
    You are an helpful assistant that summarizes YouTube videos.
    Only use the tool summarize_youtube_video when user gives a youtube URL.
    """,
    tools=[summarize_youtube_video]
)