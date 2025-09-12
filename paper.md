title: "zipstream-ai: A Python Package for Streaming and Querying Zipped Datasets with LLMs"
tags:

data science

zip processing

large language models

file streaming

natural language interfaces
authors:

name: Pranav Nitin Motarwar
orcid: 0000-0003-2020-2020
corresponding: true
affiliation: 1
affiliations:

name: New York University
index: 1
ror: 00hx57361
date: 12 September 2025
bibliography: paper.bib

Summary

Exploratory data analysis workflows increasingly involve compressed datasets distributed as .zip or .tar.gz archives—particularly across open data portals, machine learning competitions, and large-scale sensing applications. These archives typically contain structured files (e.g., CSV, JSON, TXT) but require cumbersome pre-processing: extraction, file inspection, format guessing, and reloading. Moreover, modern AI tools such as Large Language Models (LLMs) are unable to operate directly on these files without manual conversion or summarization.

We present zipstream-ai: a lightweight, LLM-integrated Python package that allows users to stream, parse, and query structured files inside compressed archives without extraction. This package is especially valuable for data scientists, ML researchers, educators, and developers who frequently work with .zip-based datasets and want to minimize latency in exploration or integrate them into AI pipelines.

zipstream-ai offers both a Python API and a command-line interface for programmatic and interactive use. It auto-detects file formats (CSV, JSON, TXT), converts them into structured Python objects, and allows users to query the contents using natural language via OpenAI's GPT models.

Statement of Need

Despite the ubiquity of compressed datasets, Python’s standard tools (zipfile, tarfile) provide only low-level access. They lack:

format auto-detection,

integration with data analysis libraries (e.g., pandas), and

natural language interfaces for exploration.

Users are typically forced to extract archives manually, inspect file contents, write custom scripts, and only then begin analysis. This slows down workflows and creates barriers for newcomers. In the context of LLM-powered data agents and notebooks, these limitations also block AI-native data interaction pipelines.

zipstream-ai bridges this gap by offering a streaming parser that automatically detects common file types within archives and loads them into Python-native structures. Once parsed, these can be passed into LLMs like GPT for question-answering, summarization, or search.

The package supports both programmatic and CLI-based workflows. It’s ideal for users who want to:

explore ZIPs on the fly in Jupyter,

integrate compressed data into RAG pipelines,

use LLMs as data analysts over .zip archives,

or teach students to interact with datasets without unpacking them.

Methodology

The core modules of zipstream-ai are:

ZipStreamReader: Streams from .zip and .tar.gz archives, lists and reads file content without extracting.

FileParser: Automatically detects and parses .csv, .json, .txt, and .md files. CSV files support delimiter detection.

ask(): Sends a formatted prompt using a sample of the dataset (e.g., df.head() or parsed content) to an LLM (via OpenAI API) and returns a natural language response.

Additional features include:

dotenv integration for API key management

CLI tool built with typer

Streaming-safe architecture (no temporary disk files)

Support for semicolon- and tab-delimited CSVs

Future versions may include image files with OCR, audio transcripts, and local LLM integrations.

Usage

Minimal Python example:

from zipstream_ai import ZipStreamReader, FileParser, ask

reader = ZipStreamReader("sample_data.zip")
parser = FileParser(reader)
df = parser.load("data.csv")
print(ask(df, "What are the top 5 rows with highest revenue?"))

Command-line usage:

zipstream-ai browse sample_data.zip
zipstream-ai query sample_data.zip data.csv "Summarize the numeric columns"

Related Work

While Python provides built-in modules for archive access (zipfile, tarfile), they do not integrate with data parsing or LLM-based interaction. Pandas supports reading from .zip paths if you know the file name, but does not support interactive exploration or file listing. Other zip-based data loaders (e.g., datasets from Hugging Face) require configuration or known formats.

To our knowledge, zipstream-ai is the first open-source tool that:

integrates archive reading,

format detection,

data parsing, and

LLM-based querying
in a single command-line or Python interface.

Implementation

The package is implemented in pure Python 3.8+, with dependencies on pandas, openai, typer, and python-dotenv. The LLM integration is handled via OpenAI’s chat.completions endpoint, with GPT-3.5 and GPT-4 models tested.

The CLI is built with typer for fast prototyping and argument parsing. Test coverage is provided via pytest, and the package supports editable installation for rapid development workflows (pip install -e .).

The project is licensed under MIT, published to PyPI (zipstream-ai), and source code is hosted at: https://github.com/PranavMotarwar/zipstream-ai

Paper Workflow

To generate a draft PDF for submission to JOSS:

# .github/workflows/draft-pdf.yml
name: Draft PDF
on:
  push:
    paths:
      - paper.md
      - paper.bib
      - .github/workflows/draft-pdf.yml

jobs:
  paper:
    runs-on: ubuntu-latest
    name: Paper Draft
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Build draft PDF
        uses: openjournals/openjournals-draft-action@master
        with:
          journal: joss
          paper-path: paper.md
      - name: Upload
        uses: actions/upload-artifact@v4
        with:
          name: paper
          path: paper.pdf

Acknowledgements

This project was developed by Pranav Motarwar as part of NYU's applied machine learning research initiative. Special thanks to peers and professors at NYU Tandon for continuous feedback and inspiration.

References

See paper.bib for all citations.

