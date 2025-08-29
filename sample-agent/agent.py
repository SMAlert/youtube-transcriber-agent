import os
from google.adk.agents import Agent
from google.adk.models import Gemini

model=Gemini(
    model="gemini-1.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
)
def summarize_youtube_video(url: str)->str:
    return(
        "This is a placeholder summary for the YouTube video. "
        "Currently, only direct transcript input is supported."
    )

def analyze_sentiment(text: str)->dict:
    text_lower=text.lower()
    positive_words=["good", "great", "excellent", "positive", "leadership", "praised", "motivational"]
    negative_words=["bad", "poor", "negative", "criticized", "problem", "issue", "debt", "nepotism", "ignoring"]
    score=5
    for word in positive_words:
        if word in text_lower:
            score=min(score+3,10)
    for word in negative_words:
        if word in text_lower:
            score=max(score-3,0)
    if "stalin" in text_lower:
        if score>=6:
            reaction="Thumbs Up"
        elif score<=4:
            reaction="Thumbs Down"
        else:
            reaction="Neutral"
    else:
        reaction="Neutral"
    return{
        "Transcribed Text":text,
        "Sentiment Score":score,
        "Stalin Like":reaction
    }

root_agent=Agent(
    name="sample_agent",
    model=model,
    description="Sentiment Analyzer Agent",
    instruction="""
    You are a Sentiment Analyzer who analyzes a given text for reference of a person named "Stalin"
    and provide a sentiment analysis of the given text.
    Step 1: If the input is a Youtube URL, use summarize_youtube_video function to get the hardcoded transcript.
    Step 2: Analyze the transcript sentiment (scale 0–10).
    Step 3: Respond in the exact format:
    Transcribed Text: ""
    Sentiment Score: "0–10"
    Stalin Like: "Thumbs Up / Thumbs Down / Neutral"
    """,
    tools=[summarize_youtube_video, analyze_sentiment]
)

if __name__=="__main__":
    transcript = """
    Stalin is created a problem in TamilNadu. And also greets them with a positive leadership.
    """
    result=analyze_sentiment(transcript)
    print(f'Transcribed Text: "{result["Transcribed Text"]}"')
    print(f'Sentiment Score: "{result["Sentiment Score"]}"')
    print(f'Stalin Like: "{result["Stalin Like"]}"')