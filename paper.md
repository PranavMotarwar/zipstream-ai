---
title: "zipstream-ai: A Python Package for Streaming and Querying Zipped Datasets with LLMs"
tags:
  - data science
  - zip processing
  - large language models
  - file streaming
  - natural language interfaces
authors:
  - name: Pranav Motarwar
    orcid: 0000-0003-2020-2020
    corresponding: true
    affiliation: 1
  - name: Rudra Patil
    affiliation: 1
affiliations:
  - name: New York University
    index: 1
    ror: 00hx57361
date: 12 September 2025
bibliography: paper.bib
---

# Summary

Exploratory data analysis workflows increasingly involve compressed datasets distributed as `.zip` or `.tar.gz` archives—particularly across open data portals, machine learning competitions, and large-scale sensing applications. These archives typically contain structured files (e.g., CSV, JSON, TXT) but require cumbersome pre-processing: extraction, file inspection, format guessing, and reloading. Moreover, modern AI tools such as Large Language Models (LLMs) are unable to operate directly on these files without manual conversion or summarization.

We present **zipstream-ai**: a lightweight, LLM-integrated Python package that allows users to stream, parse, and query structured files inside compressed archives without extraction. This package is especially valuable for data scientists, ML researchers, educators, and developers who frequently work with `.zip`-based datasets and want to minimize latency in exploration or integrate them into AI pipelines.

zipstream-ai offers both a Python API and a command-line interface for programmatic and interactive use. It auto-detects file formats (CSV, JSON, TXT), converts them into structured Python objects, and allows users to query the contents using natural language via OpenAI's GPT models.

# Statement of Need

Despite the ubiquity of compressed datasets, Python’s standard tools (`zipfile`, `tarfile`) provide only low-level access. They lack:

- format auto-detection,
- integration with data analysis libraries (e.g., pandas), and
- natural language interfaces for exploration.

Users are typically forced to extract archives manually, inspect file contents, write custom scripts, and only then begin analysis. This slows down workflows and creates barriers for newcomers. In the context of LLM-powered data agents and notebooks, these limitations also block AI-native data interaction pipelines.

zipstream-ai bridges this gap by offering a streaming parser that automatically detects common file types within archives and loads them into Python-native structures. Once parsed, these can be passed into LLMs like GPT for question-answering, summarization, or search.

The package supports both programmatic and CLI-based workflows. It’s ideal for users who want to:

- explore ZIPs on the fly in Jupyter,
- integrate compressed data into RAG pipelines,
- use LLMs as data analysts over `.zip` archives, or
- teach students to interact with datasets without unpacking them.

## Methodology

The architecture of `zipstream-ai` is built around three primary Python modules. `ZipStreamReader` allows users to directly stream and list contents from compressed `.zip` and `.tar.gz` archives without requiring extraction. This minimizes disk usage and accelerates the workflow, particularly for large datasets. On top of this, `FileParser` automatically detects file formats such as `.csv`, `.json`, `.txt`, and `.md`, and parses them into structured Python-native objects, usually using `pandas`. It also detects common delimiters like commas, semicolons, and tabs, ensuring flexible parsing.

The third component, `ask()`, enables natural language interaction with the parsed data by leveraging OpenAI’s GPT models. This function constructs prompts from representative data (e.g., DataFrame head or content sample) and queries the LLM to generate insights, summaries, or perform analytical reasoning.

To support diverse usage, the package includes `.env` file support for secure API key management via `python-dotenv`, and a command-line interface (CLI) built with `typer` that supports interactive browsing and querying. The architecture is streaming-safe, avoiding temporary files, and is designed to plug into both Jupyter-based workflows and backend pipelines. Planned extensions include support for OCR, audio transcription, and integration with open-source LLMs for offline use.

# Related Work

While Python provides built-in modules for archive access (`zipfile`, `tarfile`), they do not integrate with data parsing or LLM-based interaction. `pandas` supports reading from `.zip` paths if you know the file name, but does not support interactive exploration or file listing. Other zip-based data loaders (e.g., Hugging Face datasets) require configuration or known formats.

To our knowledge, **zipstream-ai** is the first open-source tool that integrates archive reading, format detection, data parsing, and LLM-based querying in a single command-line or Python interface.

# Implementation

The package is implemented in pure Python 3.8+ and relies on several widely adopted libraries including `pandas` for data manipulation, `openai` for LLM access, `typer` for building the command-line interface, and `python-dotenv` for managing environment variables securely. The LLM integration is handled via OpenAI’s `chat.completions` endpoint, with extensive testing across both GPT-3.5 and GPT-4 models to ensure compatibility.

The CLI is built using `typer`, allowing for clean argument parsing and quick extensibility. For development and testing, `pytest` is used, and the package supports editable installation (`pip install -e .`) to facilitate rapid iteration. The entire project is open-source under the MIT license, available on GitHub, and published on PyPI for ease of installation.

# Project Status

zipstream-ai is actively maintained and openly available. The source code is hosted on GitHub, the package is published on PyPI, and the project is licensed under MIT. This draft was last updated on 12 September 2025.

# Acknowledgements

This project was developed by Pranav Motarwar as part of NYU’s applied machine learning research initiative. Special thanks to peers and professors at NYU Tandon for continuous feedback and inspiration throughout the development of this tool.

# References

See `paper.bib` for all references.


