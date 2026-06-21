from crewai.tools import BaseTool
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp
import re


class YouTubeResearchTool(BaseTool):
    name: str = "YouTube Research Tool"
    description: str = """
    Extract transcript and metadata from a YouTube video.
    Input: YouTube URL
    """

    def _extract_video_id(self, url: str):

        patterns = [
            r"v=([0-9A-Za-z_-]{11})",
            r"youtu\.be\/([0-9A-Za-z_-]{11})"
        ]

        for pattern in patterns:
            match = re.search(pattern, url)

            if match:
                return match.group(1)

        raise ValueError("Invalid YouTube URL")

    def _get_video_metadata(self, url):

        ydl_opts = {
            "quiet": True,
            "skip_download": True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        return {
            "title": info.get("title"),
            "channel": info.get("channel"),
            "views": info.get("view_count"),
            "duration": info.get("duration"),
            "upload_date": info.get("upload_date")
        }

    def _run(self, url: str):

        video_id = self._extract_video_id(url)

        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        transcript_text = " ".join(
            chunk["text"]
            for chunk in transcript
        )

        metadata = self._get_video_metadata(url)

        return f"""
        VIDEO INFORMATION

        Title: {metadata['title']}
        Channel: {metadata['channel']}
        Views: {metadata['views']}
        Duration: {metadata['duration']}
        Upload Date: {metadata['upload_date']}

        TRANSCRIPT

        {transcript_text}
        """


yt_tool = YouTubeResearchTool()