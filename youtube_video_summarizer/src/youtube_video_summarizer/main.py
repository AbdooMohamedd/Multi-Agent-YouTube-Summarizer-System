#!/usr/bin/env python
import sys
import warnings
import argparse
import os
import inspect

# Add the parent directory to the path to resolve imports when running directly
current_file = inspect.getfile(inspect.currentframe())
current_dir = os.path.dirname(os.path.abspath(current_file))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)

try:
    from crew import YoutubeVideoSummarizer
except ImportError:
    # Fall back to relative import
    from .crew import YoutubeVideoSummarizer

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run(youtube_url=None):
    """
    Run the transcript extraction crew.
    
    Args:
        youtube_url: URL of the YouTube video to extract transcript from.
    """
    if not youtube_url:
        print("Error: YouTube URL is required.")
        print("Usage: python -m youtube_video_summarizer.main --url <youtube_url>")
        sys.exit(1)
    
    inputs = {
        'youtube_url': youtube_url
    }
    
    try:
        print(f"Extracting transcript from: {youtube_url}")
        print(f"Inputs dictionary: {inputs}")
        YoutubeVideoSummarizer().crew().kickoff(inputs=inputs)
        print(f"Raw transcript extraction complete. Saved to 'transcript.md'")
    except Exception as e:
        raise Exception(f"An error occurred while extracting the transcript: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract transcript from a YouTube video')
    parser.add_argument('--url', type=str, required=True, help='YouTube video URL to extract transcript from')
    
    args = parser.parse_args()
    run(args.url)