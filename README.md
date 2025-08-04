# Chapter Rewriter

A simple LangGraph-based tool that scrapes book chapters from URLs, rewrites them using AI, and provides quality metrics.

## 🚀 Quick Start

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   playwright install
   ```

2. **Set up API key:**
   Create a `.env` file:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Run the app:**

   ```bash
   streamlit run main.py
   ```

   **For development with LangSmith tracking:**

   ```bash
   python dev_simple.py
   ```

   Or test with a specific URL:

   ```bash
   python dev_simple.py --url "https://en.wikisource.org/wiki/Pride_and_Prejudice/Chapter_1"
   ```

   _Note: This works with Python 3.10 and provides full LangSmith tracking._

## 🎯 Features

- **Web Scraping**: Extract text from book chapter URLs
- **AI Rewriting**: Transform content using Groq/Llama
- **Quality Metrics**: Length, readability, diversity, coherence scores
- **Screenshots**: Visual capture of original pages
- **Reward System**: Automated quality assessment

## 📊 Quality Metrics

- **Length**: Optimal text length (normalized to 2000 chars)
- **Readability**: Word length optimization (target: 5 chars avg)
- **Diversity**: Unique word ratio for vocabulary richness
- **Coherence**: Sentence structure analysis (target: 15 words avg)

## 🔄 Workflow

1. **Scrape**: Extract content from URL
2. **Screenshot**: Capture visual representation
3. **Rewrite**: AI-powered content transformation
4. **Reward**: Quality evaluation and scoring

## 📝 License

This project is for educational purposes. The developer retains all rights to their original code.
