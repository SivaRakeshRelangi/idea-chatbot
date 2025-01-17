
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

## Logic to prioritize intents in this project
Scoring system that evaluates each idea across three key dimensions: **Relevance**, **Impact**, and **Feasibility**. These dimensions are defined as follows:  

1. **Relevance**: How well the idea aligns with the user's query or needs.  
2. **Impact**: The potential return on investment (ROI) or value the idea can generate.  
3. **Feasibility**: The ease of implementing the idea considering technical and resource constraints.  

Each dimension is scored on a scale of 1 to 5, with 5 being the highest. The scores are provided by an AI model and are averaged to calculate an **overall priority score** for each idea.  

Finally, the ideas are sorted in descending order of their scores, ensuring the most promising ideas are ranked highest. This approach ensures that user preferences and implementation practicality are balanced effectively.

