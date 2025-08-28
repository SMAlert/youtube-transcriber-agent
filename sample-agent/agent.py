import os
import random

from google.adk.agents import Agent
from google.adk.models import Gemini
# testing to create a branch
model = Gemini(
    model="gemini-1.5-flash",
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
    You are an Sentiment Analyzer who analyzes a given text for reference of a person named "Stalin" and provide an sentiment analysis of the given text.
    Step 1:     If the input is a  Youtube url, please use get transcrive function to transcribe the Youtube  URL
    Step 2: The transcribed  output should be analyzed for the sentiment of a person named "Stalin"
    The output of the sentiment analysis should be in the format of 
    Transcribed Text: ""
    Sentiment Score: "This should be a  score of 0-10. 0 being negative sentiment and 10 being the postive sentiment"
    Stalin Like: "A thumbs up for a postive sentiment and a thumbs down for negative sentiment. If no mention, equal should be returned."
    """,
    tools=[summarize_youtube_video]
)
