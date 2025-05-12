# 🧠 Multi-Agent YouTube Summarizer System (CrewAI-Based)

## 📌 Objective

Build a multi-agent system using **CrewAI** that:
1. Accepts a YouTube video URL
2. Extracts the transcript
3. Cleans and preprocesses the transcript
4. Summarizes the video content
5. Evaluates the summary’s accuracy
6. Saves the final summary as a local PDF file

---

## ⚙️ Technology Stack

- Python 3.10+
- CrewAI
- youtube-transcript-api (for transcript extraction)
- OpenAI API (for summarization and evaluation)
- FPDF (for PDF export)
- LangChain (optional for chaining and memory)

---

## 🧩 System Design: 5 Agents

### ✅ Agent 1: Transcript Agent

- **Role:** Extract transcript from the YouTube video.
- **Input:** YouTube video URL
- **Output:** Raw transcript text
- **Notes:** Uses `youtube-transcript-api` to fetch subtitles.

---

### ✅ Agent 2: Preprocessing Agent

- **Role:** Clean and preprocess the raw transcript.
- **Input:** Raw transcript text
- **Output:** Cleaned, structured transcript
- **Notes:** Removes timestamps, unnecessary breaks, and formats the text.

---

### ✅ Agent 3: Summarization Agent

- **Role:** Generate a concise and coherent summary of the cleaned transcript.
- **Input:** Cleaned transcript
- **Output:** Short paragraph/text summary
- **Notes:** Uses OpenAI’s GPT model for summarization.

---

### ✅ Agent 4: Accuracy Evaluator Agent

- **Role:** Assess the quality and accuracy of the summary.
- **Input:** Original transcript + summary
- **Output:** Accuracy score and evaluation feedback
- **Notes:** Compares concepts or checks alignment using a language model or similarity scoring.

---

### ✅ Agent 5: PDF Export Agent

- **Role:** Save the summary to a local PDF file.
- **Input:** Final summary
- **Output:** `video_summary.pdf` stored locally
- **Notes:** Uses FPDF or other PDF generation library.

---

## 🔁 Workflow Steps

1. User provides a YouTube URL.
2. Agent 1 extracts the transcript from the video.
3. Agent 2 cleans and formats the transcript text.
4. Agent 3 generates a summary.
5. Agent 4 evaluates how well the summary matches the original content.
6. Agent 5 saves the final summary as a PDF file on disk.

---

## ✅ Output

- Clean and accurate summary of the video.
- Evaluation score/feedback on summary quality.
- PDF file named `video_summary.pdf` stored locally.
