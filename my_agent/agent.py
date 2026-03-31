"""
This file is where you will implement your agent.
The `root_agent` is used to evaluate your agent's performance.
"""

from google.adk.agents import llm_agent
from my_agent.tools.calculator import calculator
from my_agent.tools.fetch_webpage import fetch_webpage
from my_agent.tools.read_pdf import read_pdf
from my_agent.tools.web_search import web_search
from my_agent.tools import *

root_agent = llm_agent.Agent(
    model="gemini-2.5-flash-lite",
    name="agent",
    description="A helpful assistant with mathematical, reasoning, and PDF reading capabilities.",
    instruction=(
      "You answer questions directly and concisely.\n\n"
      "CALCULATOR: Use calculator(operation, a, b) for ALL math.\n"
      "Operations: 'add', 'subtract', 'multiply', 'divide', 'power', 'modulo'\n"
      "Be precise: if asked for a setting name, give only the name, not the full heading.\n"
      "For multi-step: Do one operation, read result, use that number in next operation.\n"
      "CRITICAL: Pass plain numbers as a and b, never objects.\n\n"
      "PDF FILES: Use read_pdf(file_path) to read PDF attachments and answer shortly for large pdfs pass a search term argument to find a specific content.\n"
      "WEB: Use web_search(query, max_results) to find relevant URLs when web knowledge is required.\n"
      "Then use fetch_webpage(url, max_chars) to read one selected page and extract the exact answer.\n"
      "Prefer trusted sources and provide only the final requested output format.\n"
        ),
    tools=[calculator, read_pdf, web_search, fetch_webpage],
    sub_agents=[],
)
