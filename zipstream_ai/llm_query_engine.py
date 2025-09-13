import os
from dotenv import load_dotenv
import pandas as pd
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask(data, query):
    """
    Ask a natural language question about the dataset using Google Gemini API.
    Supports both DataFrames and plain text content.
    """
    if isinstance(data, str):
        sample = data[:3000]
    elif isinstance(data, pd.DataFrame):
        sample = data.head().to_string()
    else:
        sample = str(data)

    prompt = f"""You are a helpful assistant for exploring datasets.

--- DATA SAMPLE ---
{sample}
-------------------

Now answer the question:
{query}
"""

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
