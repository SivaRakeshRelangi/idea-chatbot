import requests

BASE_URL = "http://127.0.0.1:5000"


def display_ranked_ideas(ranked_ideas):
    """
    Display ranked ideas in a user-friendly format.
    """
    print("\nGenerated Ideas (Ranked):")
    for idx, idea in enumerate(ranked_ideas, 1):
        print(f"{idx}. {idea['idea']} (Score: {idea['total_score']:.2f})")


def get_user_selection(ranked_ideas):
    """
    Ask the user to select two ideas by number.
    """
    while True:
        try:
            selection = input("\nPlease choose two ideas by typing their numbers (e.g., 1,3): ")
            selected_indices = [int(num.strip()) - 1 for num in selection.split(",")]
            if len(selected_indices) == 2 and all(0 <= idx < len(ranked_ideas) for idx in selected_indices):
                return [ranked_ideas[idx]["idea"] for idx in selected_indices]
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please select two numbers separated by a comma (e.g., 1,3).")


def display_detailed_suggestions(suggestions):
    """
    Display detailed suggestions for selected ideas.
    """
    print("\nDetailed Suggestions:")
    for idea, suggestion in suggestions.items():
        print(f"- {idea}:\n{suggestion}\n")


def main():
    # Step 1: Get user query
    query = input("Enter your query (e.g., 'What new app should I build?'): ")

    # Step 2: Generate and rank ideas
    response = requests.post(f"{BASE_URL}/generate", json={"query": query})
    if response.status_code == 200:
        ranked_ideas = response.json()["ranked_ideas"]
        display_ranked_ideas(ranked_ideas)
    else:
        print(f"Error generating ideas: {response.json()['error']}")
        return

    # Step 3: User selects two ideas
    selected_ideas = get_user_selection(ranked_ideas)

    # Step 4: Get detailed suggestions for selected ideas
    response = requests.post(f"{BASE_URL}/expand", json={"selected_ideas": selected_ideas})
    if response.status_code == 200:
        suggestions = response.json()
        display_detailed_suggestions(suggestions)
    else:
        print(f"Error expanding ideas: {response.json()['error']}")


if __name__ == "__main__":
    main()
