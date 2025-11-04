<table>
<tr>
<td width="160" align="center">
  <img src="https://github.com/PranavMotarwar/zipstream-ai/blob/main/zipstream-ai-white.png?raw=true" alt="zipstream-ai logo" width="140">
</td>
<td>
  <h1 style="font-size: 2.2em; margin-bottom: 0;">zipstream-ai</h1>
</td>
</tr>
</table>

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zipstream-ai)
![PyPI](https://img.shields.io/pypi/v/zipstream-ai)
![License](https://img.shields.io/pypi/l/zipstream-ai)
![Docs](https://img.shields.io/badge/docs-passing-brightgreen)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![mypy](https://img.shields.io/badge/mypy-checked-blue)

**Stream, Parse, and Chat with Compressed Datasets Using LLMs**

`zipstream-ai` is a Python package that lets you interact with `.zip` and `.tar.gz` files directly—no need to extract them manually. It integrates archive streaming, format detection, data parsing (e.g., CSV, JSON), and natural language querying with LLMs like Gemini, all through a unified interface.

---

## Installation

```bash
pip install zipstream-ai
```

---

## Features

| Feature                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Archive Streaming       | Stream `.zip` and `.tar.gz` files without extraction                        |
| Format Auto-Detection   | Automatically detects file types (CSV, JSON, TXT, etc.)                     |
| DataFrame Integration   | Parses tabular data directly into pandas DataFrames                         |
| LLM Querying            | Ask questions about your data using Gemini (Google's LLM)                   |
| Modular Design          | Easily extensible for new formats or models                                 |
| Python + CLI Support    | Use via command line or as a Python package                                 |

---

## Use Case Examples

### 1. Load & Explore ZIP

```python
from zipstream_ai import ZipStreamReader

reader = ZipStreamReader("dataset.zip")
print(reader.list_files())
```

### 2. Parse CSV from ZIP

```python
from zipstream_ai import FileParser

parser = FileParser(reader)
df = parser.load("data.csv")
print(df.head())
```

### 3. Ask Questions with Gemini

```python
from zipstream_ai import ask

response = ask(df, "Which 3 rows have the highest 'score'?")
print(response)
```

---

## Why zipstream-ai?

| Traditional Workflow               | With `zipstream-ai`                         |
|-----------------------------------|---------------------------------------------|
| Manually unzip files              | Stream directly from archive                |
| Write boilerplate code to parse   | Built-in file parsers (CSV, JSON, etc.)     |
| Switch between tools for LLMs     | One-liner `ask(df, question)` integration   |

---

## Architecture Diagram

```
         ┌──────────────┐
         │  .zip/.tar   │
         └────┬─────────┘
              │
   ┌──────────▼──────────┐
   │  ZipStreamReader    │
   └──────────┬──────────┘
              │
     ┌────────▼────────┐
     │   FileParser    │────>  pd.DataFrame
     └────────┬────────┘
              │
     ┌────────▼────────┐
     │     ask()       │────> Gemini LLM Output
     └─────────────────┘
```




