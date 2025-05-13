from crewai.tools import BaseTool
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

class TranscriptTool(BaseTool):
    name: str = "YouTube Transcript Tool"
    description: str = "Extracts and returns the transcript from a YouTube video URL."

    def _get_video_id(self, url: str) -> str | None:
        query = urlparse(url)
        if query.hostname == 'youtu.be':
            return query.path[1:]
        elif query.hostname in ['www.youtube.com', 'youtube.com']:
            return parse_qs(query.query).get('v', [None])[0]
        return None
        
    def _run(self, url: str) -> str:
        video_id = self._get_video_id(url)
        if not video_id:
            return "Invalid YouTube URL."

        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            for transcript in transcript_list:
                if transcript.language_code.startswith('en'):
                    segments = transcript.fetch()
                    return "\n".join([segment.text for segment in segments])
            return "No English transcript found."
        except Exception as e:
            return f"Error: {e}"
