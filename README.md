# PDF Agent – HTML & CSS Generator

This project uses [LangChain](https://www.langchain.com/) and [Google Generative AI](https://ai.google/) to automatically generate HTML and CSS files based on natural language tasks.  
The HTML is styled with generated CSS and both are saved locally.

## Features
- Generate HTML from a natural language prompt.
- Automatically create matching CSS styles for the HTML.
- Save both files to disk with correct filenames.
- Fully customizable prompt templates for HTML and CSS generation.

## How It Works
1. **HTML Generation**  
   - You provide a task such as `"Create a landing page for a book store"`.  
   - The LLM outputs `filename:html_code`.
   - The `RunnableLambda` tool saves the HTML to disk.

2. **CSS Generation**  
   - The HTML content is passed to another LLM prompt.  
   - The LLM outputs `filename:css_code`.
   - The CSS file is saved.

3. **File Creation**  
   - Any unwanted markdown/code fences are cleaned before saving.
   - Filenames and content are separated by the first colon only.

## Project Structure

├── main.py # Main script to run the chain
├── cloth_store_landing.html # Example generated HTML file
├── style.css # Example generated CSS file
├── .env # Environment variables (API key)
├── README.md # Project documentation
└── pyproject.toml # Project dependencies


## Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <folder_name>
2. Install dependencies:
   ```bash
   uv sync
3. Add your Google Generative AI API key to .env:
   ```bash
   git clone <repo-url>
   cd pdfagent

## Usage
1. Run the script:
   ```bash
   uv run main.py
2. Example task:
   ```bash
   chain.invoke({"task": "create a landing page for a book store"})

Generated files will appear in the project folder.

**Requirements**
 - Python 3.9+
 - langchain
 - langchain-google-genai
 - uv (optional, for environment management)