# 🧠 Multi-Agent YouTube Summarizer System (CrewAI-Based)

## 📌 Objective

Build a multi-agent system using **CrewAI** that:

1. Accepts a YouTube video URL
2. Extracts the transcript
3. Cleans and preprocesses the transcript
4. Summarizes the video content
5. Evaluates the summary’s accuracy
6. Saves the final summary to a `.md` file named after the video title
7. Converts the `.md` file into a PDF saved in the project directory

---

## ⚙️ Technology Stack

- Python 3.10+
- CrewAI
- youtube-transcript-api (for transcript extraction)
- OpenAI API (for summarization and evaluation)
- Markdown & PDF libraries (like `markdown`, `fpdf`, or `pdfkit`)
- LangChain (optional)

---

## 🧩 System Design: 5 Agents

### ✅ Agent 1: Transcript Agent

- **Role:** Extract transcript from the YouTube video.
- **Input:** YouTube video URL
- **Output:** Raw transcript text
- **Tools:** `youtube-transcript-api`

---

### ✅ Agent 2: Preprocessing Agent

- **Role:** Clean and preprocess the raw transcript.
- **Input:** Raw transcript text
- **Output:** Cleaned transcript
- **Notes:** Removes timestamps and formats the text for summarization.

---

### ✅ Agent 3: Summarization Agent

- **Role:** Generate a summary from the cleaned transcript.
- **Input:** Cleaned transcript
- **Output:** Text summary
- **Notes:** Uses OpenAI GPT for generating summaries.

---

### ✅ Agent 4: Accuracy Evaluator & Markdown Saver Agent

- **Role:**
  1. Evaluate the accuracy of the summary against the original transcript.
  2. If the summary is acceptable, save it as a Markdown file.
- **Input:** Transcript + Summary
- **Output:** `Youtube_video_title.md` file containing the final summary
- **Notes:** Summary must pass a quality threshold (e.g., 7/10 or higher score) before saving.

---

### ✅ Agent 5: PDF Export Agent

- **Role:** Convert the saved Markdown file into a PDF.
- **Input:** `Youtube_video_title.md`
- **Output:** `Youtube_video_title.pdf` in the same project folder
- **Notes:** Uses PDF generation libraries to render the Markdown to PDF.

---

## 🔁 Workflow Steps

1. User inputs a YouTube URL.
2. **Agent 1** extracts the transcript.
3. **Agent 2** cleans and formats the transcript.
4. **Agent 3** generates a summary.
5. **Agent 4** evaluates the summary:
   - If it passes, saves it to `Youtube_video_title.md`
   - If it fails, stops the workflow or loops back for revision.
6. **Agent 5** converts the `.md` file to `Youtube_video_title.pdf`.

---

## ✅ Output

- Accurate video summary in `.md` format.
- Matching `.pdf` version of the summary.
- Saved in the project directory, named after the video title.

---

## 🚀 Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Multi-Agent-YouTube-Summarizer-System.git
   cd Multi-Agent-YouTube-Summarizer-System
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   # On Windows with PowerShell
   .\venv\Scripts\Activate.ps1
   # On Windows with Command Prompt
   # venv\Scripts\activate.bat
   # On macOS/Linux
   # source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

### Usage

There are multiple ways to run the system:

#### Option 1: Use the CLI tool (Recommended)

The CLI tool provides a friendly interface with validation checks:

```powershell
# Check if your environment is properly set up
python -m multi_agent_youtube_summarizer_system.cli check

# Run the tests to verify functionality
python -m multi_agent_youtube_summarizer_system.cli test

# Run the integration test
python -m multi_agent_youtube_summarizer_system.cli test --integration

# Summarize a YouTube video
python -m multi_agent_youtube_summarizer_system.cli summarize "https://www.youtube.com/watch?v=VIDEO_ID"
```

#### Option 2: Use the module directly

Run the system with a YouTube URL:

```powershell
python -m multi_agent_youtube_summarizer_system.main "https://www.youtube.com/watch?v=VIDEO_ID"
```

#### Option 3: Use the convenience scripts

For Windows:

```powershell
.\run.bat "https://www.youtube.com/watch?v=VIDEO_ID"
```

For Linux/macOS:

```bash
./run.sh "https://www.youtube.com/watch?v=VIDEO_ID"
```

The system will:

1. Extract the transcript from the YouTube video
2. Process and summarize the content
3. Save the summary as both `.md` and `.pdf` files in the project directory

### Example

```powershell
python -m multi_agent_youtube_summarizer_system.cli summarize "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

## 🐳 Docker Support

You can also run the system using Docker:

### Build the Docker image

```powershell
docker build -t youtube-summarizer .
```

### Run with Docker

```powershell
docker run --rm -v ${PWD}/output:/app/output -e OPENAI_API_KEY=your_api_key_here youtube-summarizer summarize "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Run with Docker Compose

1. Create a `.env` file with your OpenAI API key
2. Run the following command:

```powershell
$env:YOUTUBE_URL="https://www.youtube.com/watch?v=VIDEO_ID"; docker-compose up
```

Output files will be saved in the `output` directory.

## ⚖️ License

This project is licensed under the MIT License - see the LICENSE file for details.
