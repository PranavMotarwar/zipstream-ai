# zipstream_ai/llm_query_engine.py

import os
import pandas as pd
import google.generativeai as genai

# Load the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def ask(data, query):
    """
    Ask a natural language question about the dataset using Google Gemini API.
    Supports both DataFrames and plain text content.
    """
    if isinstance(data, str):
        # For large Markdown or text files
        sample = data[:3000]
    elif isinstance(data, pd.DataFrame):
        # Show top 10 rows in markdown
        sample = data.head(10).to_markdown()
    else:
        sample = str(data)

    prompt = f"""You are a helpful assistant for exploring datasets.

--- DATA ---

{sample}

--- TASK ---

{query}
"""
    response = model.generate_content(prompt)
    return response.text
