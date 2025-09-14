# -*- coding: utf-8 -*-
"""
zipstream Demo File

"""

pip install zipstream-ai==0.1.2

from zipstream_ai import ZipStreamReader, FileParser, ask

#Load ZIP archive
reader = ZipStreamReader("winequality.zip")

#List files inside it
print(reader.list_files())

#Load the CSV inside the ZIP
parser = FileParser(reader)
df = parser.load("winequality-white.csv")

#Preview data
print(df.head())

import google.generativeai as genai
genai.configure(api_key="<Your-GEMINI-key>")

models = genai.list_models()
for m in models:
    print(m.name)

#Create the model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

#Run a query (structured reasoning)
prompt = """
You are given this table of wine samples as a pandas dataframe. Which 3 wine samples have the highest alcohol content?

""" + df.head(10).to_markdown()

response = model.generate_content(prompt)
print(response.text)

top_3 = df.sort_values('alcohol', ascending=False).head(3)
print(top_3)