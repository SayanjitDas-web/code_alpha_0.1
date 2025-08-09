import re
import os
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_AI_API")


llm = GoogleGenerativeAI(
    model="gemini-2.5-pro",
    api_key=gemini_api_key
)


def create_file(command: str) -> str:
    """
    Creates a file from 'filename:content' format.
    Sanitizes extra markdown or formatting.
    Returns only the content so next chain step can use it.
    """
    
    cleaned = re.sub(r"```[a-zA-Z]*", "", command)
    cleaned = cleaned.replace("```", "").strip()

    parts = cleaned.split(":", 1)
    if len(parts) != 2:
        raise ValueError(f"Invalid command format: {command}")

    filename = parts[0].strip()
    content = parts[1].strip()

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"File '{filename}' created successfully.")
        return content  # Pass content to next chain step
    except Exception as e:
        print(f"Error creating file '{filename}': {e}")
        return ""

file_tool = RunnableLambda(create_file)

html_prompt = PromptTemplate(
    template="""
{task}

Rules:
- Strictly return ONLY in this format (no markdown, no extra text):
  filename:html_code
- Do not include ```html``` or ``` fences and don't include css in the style tag.
- Include a link tag containing style.css named file link and also use external links for images and js script making
- Filename must end with `.html`.
""",
    input_variables=["task"]
)

css_prompt = PromptTemplate(
    template="""
{html}

Generate CSS for the given HTML.

Rules:
- Strictly return ONLY in this format (no markdown, no extra text):
  filename:css_code
- Do not include ```css``` or ``` fences.
- Filename must end with `.css`.
""",
    input_variables=["html"]
)

chain = (
    html_prompt
    | llm
    | StrOutputParser()
    | file_tool
    | css_prompt
    | llm
    | StrOutputParser()
    | file_tool
)

chain.invoke({"task": "create a landing page for a cloth store"})
