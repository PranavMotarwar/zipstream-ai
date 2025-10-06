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
    orcid: 0009-0009-1717-4318
    corresponding: true
    affiliation: 1
  - name: Rudra Patil
    affiliation: 1
affiliations:
  - name: New York University
    index: 1
    ror: 0190ak572
date: 12 September 2025
bibliography: paper.bib
---

# Summary

Compressed datasets provided as `.zip` or `.tar.gz` archives are becoming increasingly popular in exploratory data analysis workflows, mainly across the domains of academic research which involves large and complex datasets. These archives usually contain structured files, such as CSV, JSON, or TXT, but these data files also need pre-processing, which usually involves the user following procedures like file extraction, inspection, and before the data could be actually used in the research package. Currently, without human conversion or summarization, these files cannot be directly processed by contemporary AI technologies that use Large Language Models (LLMs).

The **zipstream-ai** is LLM-integrated Python package that allows users to stream, parse, and query structured files inside compressed archives without extraction. This package is valuable for users who frequently work with large and complex datasets which are often wrapped in a zip format  and want to minimize latency in exploration or integrate them into AI pipelines.

zipstream-ai offers both a Python API and a command-line interface (CLI) for programmatic use. It auto-detects file formats, converts them into structured Python objects, and allows users to query the contents using natural language via OpenAI's GPT models.



## Statement of Need
Compressed Datasets are the norm when it comes to modern research. However, conventional Python libraries like tarfile and zipfile lack essential usability aspects and only offer low-level archive access. They don't enable high-level interfaces like natural language searches, interact with tools like pandas, or automatically identify file kinds. Before any valuable insight can be discovered, users must manually unpack archives, examine files, and create boilerplate parsing templates. Such overhead work can limit the adoption of LLM-based technology in real-world processes
In LLM-powered systems, where agents are supposed to interact with data seamlessly, these constraints are troublesome. A large percentage of real-world datasets are still inaccessible to LLM workflows in the absence of a smooth method for retrieving structured material from archives.

`zipstream-ai` addresses this gap by allowing users to directly stream and parse common file from within compressed archives and immediately interact with them using large language models. This enables AI-native exploration of zipped datasets without manual overhead.

The package supports both programmatic and CLI workflows. It’s ideal for users who want to:

- interact with structured data inside compressed files without manual extraction,
- explore ZIP archives directly within Jupyter like environments,
- integrate compressed datasets into Retrieval-Augmented Generation (RAG) pipelines,
- perform natural language querying of archived data using LLMs.

## Methodology

The architecture of `zipstream-ai` is built around three primary Python modules. `ZipStreamReader` allows users to directly stream and list contents from compressed `.zip` and `.tar.gz` archives without requiring extraction. This minimizes disk usage and accelerates the workflow, particularly for large datasets. 

Secondly, `FileParser` automatically detects file formats such as `.csv`, `.json`, `.txt`, and `.md`, and parses them into structured Python-native objects, usually using `pandas`. It also detects common delimiters like commas, semicolons, or tabs, for flexible parsing.

The third component, `ask()`, enables natural language interaction with the parsed data by leveraging OpenAI’s GPT models. This function constructs prompts from representative data and queries the LLM to generate insights or perform analytical reasoning.

To support diverse usage, the package includes `.env` file support for secure API key management via `python-dotenv`, and a command-line interface (CLI) built with `typer` that supports interactive browsing and querying. The architecture is streaming-safe and is designed to plug into both Jupyter-based workflows and backend pipelines. Planned extensions include support for OCR and integration with open-source LLMs for offline use.

![Figure 1: Workflow of *zipstream-ai*, showing how compressed archives are streamed, parsed, and queried using LLMs via CLI or Python interfaces.](zipstream_workflow.png)

# Related Work
While Python provides built-in modules like zipfile and tarfile for archive access, they operate at a low level and do not integrate with data parsing or natural language interfaces. Libraries such as pandas support reading from compressed paths like .zip archives [@mckinney2010data] but only if the internal file name is known. They also do not support archive exploration or file listing. Other tools, such as Hugging Face Datasets [@lhoest2021datasets], allow loading datasets from compressed formats but require predefined dataset configurations.
Several recent efforts have explored using Large Language Models (LLMs) for structured data interaction [@li2023apibench; @hulsebos2021nl4dv], yet these systems assume preprocessed tabular inputs. They do not address the upstream bottlenecks of parsing compressed data.
zipstream-ai is the first open-source tool that combines archive streaming, format detection, data parsing, and LLM-based natural language querying into a single lightweight interface usable via both Python and CLI.
# Implementation

The package is implemented in Python 3.8+ and relies on several widely adopted libraries like `pandas` for data manipulation, `openai` for LLM access, `typer` for building the command-line interface, and `python-dotenv` for managing environment variables securely. The LLM integration is handled via OpenAI’s `chat.completions` endpoint, with extensive testing across both GPT-3.5 and GPT-4 models to ensure compatibility.

The CLI is built using `typer`, allowing for clean argument parsing and quick extensibility. For development and testing, `pytest` is used, and the package supports editable installation to facilitate rapid iteration. The entire project is open-source under the MIT license, available on GitHub, and published on PyPI for ease of installation.

# Project Status

zipstream-ai is actively maintained and openly available. The source code is hosted on GitHub, the package is published on PyPI, and the project is licensed under MIT. This draft was last updated on 13 September 2025.

## Acknowledgements

This project was developed by Pranav Motarwar and Rudra Patil as part of their applied machine learning research work. The tool reflects an independent effort to streamline LLM-based interaction with compressed datasets.

# References

