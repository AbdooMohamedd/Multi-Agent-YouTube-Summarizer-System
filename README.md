# 🧠 Multi-Agent YouTube Video Summarizer

![YouTube Video Summarizer Banner](path/to/banner/image.png)

## 📋 Overview

This system uses CrewAI's multi-agent architecture to transform YouTube videos into concise, professional summaries with minimal user input. Perfect for researchers, students, and professionals who need to quickly extract valuable information from video content.

## 🚀 What This System Does

The YouTube Video Summarizer automates the entire process of:

1. Extracting the complete transcript from any YouTube video
2. Cleaning and preprocessing the raw transcript
3. Creating a professional, well-structured summary
4. Evaluating the summary for accuracy and completeness
5. Generating a PDF document of the approved summary

All with just one command and a YouTube URL!

## 🔄 Workflow

```
YouTube URL → Extract Transcript → Preprocess → Summarize → Evaluate → Generate PDF
```

1. **Input**: User provides a YouTube video URL
2. **Extraction**: System pulls the complete transcript from the video
3. **Preprocessing**: Raw transcript is cleaned and formatted
4. **Summarization**: AI generates a comprehensive, structured summary
5. **Evaluation**: Summary is assessed for quality and completeness
6. **Output**: Approved summaries are saved as both Markdown and PDF

## 👥 Agent System Design

This project uses a specialized team of 5 AI agents, each with a dedicated role:

### 1. Transcript Extractor Agent

- **Task**: Extract the complete transcript from a YouTube video
- **Input**: YouTube URL
- **Output**: Raw transcript text (saved to `transcript.md`)
- **Tools**: `youtube-transcript-api`

### 2. Preprocessing Agent

- **Task**: Clean and prepare the transcript for summarization
- **Input**: Raw transcript from Agent 1
- **Output**: Cleaned, well-formatted text
- **Process**: Removes timestamps, repetitions, filler words, and fixes formatting issues

### 3. Summarization Agent

- **Task**: Generate a comprehensive, well-structured summary
- **Input**: Preprocessed transcript from Agent 2
- **Output**: Professional summary with headings, sections, and key points
- **Features**: Creates markdown formatting, proper structure, and logical organization

### 4. Evaluation Agent

- **Task**: Assess summary quality and accuracy
- **Input**: Original transcript and generated summary
- **Output**: Approved summary (saved to `summary.md`) or rejection message
- **Quality Standard**: Only approves summaries scoring 7/10 or higher

### 5. PDF Generation

- **Task**: Convert the approved markdown summary to a professional PDF
- **Input**: `summary.md` file
- **Output**: `summary.pdf` in the project directory
- **Tools**: `markdown-pdf` library

## 💻 How to Run the System

### Installation

1. Clone the repository:

   ```powershell
   git clone https://github.com/AbdooMohamedd/Multi-Agent-YouTube-Summarizer-System.git
   cd Multi-Agent-YouTube-Summarizer-System
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a `.env` file in the root directory
   - Add your API key: `OPENAI_API_KEY=your_api_key_here`

### Usage

Run the system with the following command:

```powershell
python .\src\youtube_video_summarizer\main.py --url "https://www.youtube.com/watch?v=OKuu2BVfMhM"
```

## 🧪 Test Results

We've successfully tested the system on this YouTube video:
[https://www.youtube.com/watch?v=OKuu2BVfMhM](https://www.youtube.com/watch?v=OKuu2BVfMhM)

The summary and PDF were automatically generated and saved to the project directory.

You can find the generated PDF at: `youtube_video_summarizer/summary.pdf`

Here's a preview of the generated PDF:
[Generated PDF Preview]((https://github.com/AbdooMohamedd/Multi-Agent-YouTube-Summarizer-System/blob/main/youtube_video_summarizer/summary.pdf))

## ✅ Project Outputs

For each video, the system produces:

- `transcript.md` - The raw transcript extracted from the video
- `summary.md` - The cleaned, professionally formatted summary
- `summary.pdf` - A PDF version of the summary for easy sharing

## 🔧 Technical Details

- **Python Version**: 3.10+
- **Key Dependencies**:
  - CrewAI for the multi-agent architecture
  - OpenAI API for summarization and evaluation
  - youtube-transcript-api for transcript extraction
  - markdown-pdf for PDF generation

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- CrewAI for the multi-agent framework
- OpenAI for the language processing capabilities
- YouTube API for transcript access

## 📬 Contact

For questions or feedback, please open an issue on the GitHub repository or contact the project maintainer.
