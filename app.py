import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Constants
HF_API_URL = "https://api-inference.huggingface.co/models/gpt2"
HF_SIMILARITY_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}


def generate_ideas(prompt):
    """
    Generate 3 unique ideas using Hugging Face's GPT-2 model.
    """
    response = requests.post(HF_API_URL, headers=HEADERS, json={"inputs": prompt})
    if response.status_code == 200:
        generated_text = response.json()[0]["generated_text"]
        return generated_text.split("\n")[:3]
    else:
        raise Exception(f"Failed to generate ideas: {response.text}")


def rank_ideas(ideas, query):
    """
    Rank ideas based on relevance, impact, and feasibility.
    """
    ranked_ideas = []
    for idea in ideas:
        relevance = requests.post(
            HF_SIMILARITY_URL,
            headers=HEADERS,
            json={"inputs": {"source_sentence": query, "sentences": [idea]}}
        ).json()[0] * 10 
         # Scale relevance score
        impact = 5 if any(word in idea.lower() for word in ["app", "platform", "service"]) else 3
        feasibility = max(1, 6 - len(idea.split()))  
        total_score = relevance + impact + feasibility
        ranked_ideas.append({
            "idea": idea,
            "relevance": relevance,
            "impact": impact,
            "feasibility": feasibility,
            "total_score": total_score
        })
    return sorted(ranked_ideas, key=lambda x: x["total_score"], reverse=True)


@app.route("/generate", methods=["POST"])
def generate():
    """
    Generate and rank ideas.
    """
    query = request.json.get("query", "What new app should I build?")
    try:
        ideas = generate_ideas(query)
        ranked_ideas = rank_ideas(ideas, query)
        return jsonify({"ranked_ideas": ranked_ideas}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/expand", methods=["POST"])
def expand():
    """
    Provide detailed suggestions for selected ideas.
    """
    selected_ideas = request.json.get("selected_ideas", [])
    try:
        suggestions = {idea: f"Detailed plan for '{idea}':\n- Add unique features.\n- Target a specific audience.\n- Effective marketing strategies." for idea in selected_ideas}
        return jsonify(suggestions), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
