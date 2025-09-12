import openai
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask(data, question: str) -> str:
    if isinstance(data, pd.DataFrame):
        sample = data.head(10).to_csv(index=False)
        prompt = f"""
You are a helpful data analyst.

Here is a sample of the data:
{sample}

Question: {question}
Answer:
"""
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]
    else:
        return "Only DataFrame-based queries are supported for now."