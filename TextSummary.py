from youtube_transcript_api._api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_youtube_transcript(video_url):
    # 1. Extract the ID (The class notes say: "NOT the full URL!")
    try:
        video_id = video_url.split("v=")[1].split("&")[0]
    except Exception:
        return "Invalid URL"

    try:

        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id, languages=['en'])

        formatter = TextFormatter()
        return formatter.format_transcript(transcript_data)

    except Exception as e:
        return f"Could not retrieve transcript: {e}"

video_url = "https://www.youtube.com/watch?v=AI4uTwuEip0"
print(get_youtube_transcript(video_url))