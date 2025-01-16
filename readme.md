
# Idea Generation Chatbot

## Project Overview
This project is a chatbot that generates 3 unique ideas for a user query, ranks them based on relevance, impact, and feasibility, and provides detailed suggestions for the selected ideas. It includes a Flask API and a CLI for user interaction.

## File Structure
- `app.py`: Flask API for idea generation, ranking, and expansion.
- `cli.py`: Command-line interface for user interaction.
- `.env`: Environment variables (Hugging Face API Key).
- `requirements.txt`: Python dependencies.

## Setup Instructions
1. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   
   venv\Scripts\activate

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt


3. **Add Your API Key**:
   ```bash
   HUGGINGFACE_API_KEY= " Your API Key "

4. **python app.py**:
   ```bash
   python app.py

5. **Run CLI**:
   ```bash
   python cli.py


