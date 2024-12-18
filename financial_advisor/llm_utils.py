import requests
import json

OLLAMA_BASE_URL = "http://localhost:11434/api/generate" # Default Ollama API endpoint

def query_ollama(model_name: str, prompt: str, context=None):
    """
    Sends a prompt to the Ollama API and returns the response.

    Args:
        model_name: The name of the LLM model to use (e.g., "llama2", "mistral").
        prompt: The prompt to send to the model.
        context: An optional list of integers representing the previous dialog context.

    Returns:
        A dictionary containing the model's response and the updated context.
    """
    data = {
        "model": model_name,
        "prompt": prompt,
        "stream": False,
        "context": context,
    }

    response = requests.post(OLLAMA_BASE_URL, data=json.dumps(data))
    response.raise_for_status()  # Raise an exception for bad status codes

    response_json = response.json()
    return {
        "response": response_json["response"],
        "context": response_json.get("context")
    }

# Example usage:
# financial_data = get_financial_data_from_other_modules() # Implement this function
# prompt = f"Analyze the following financial data and provide insights:\n{financial_data}"
# result = query_ollama("llama2", prompt)
# advice = result["response"]
