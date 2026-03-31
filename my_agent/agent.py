"""
This file is where you will implement your agent.
The `root_agent` is used to evaluate your agent's performance.
"""

from google.adk.agents import llm_agent
from my_agent.tools import pdf_tool
from my_agent.tools.calculator import calculator


root_agent = llm_agent.Agent(
    model="gemini-2.5-flash-lite",
    name="agent",
    description="A helpful assistant with mathematical, reasoning, and PDF reading capabilities.",
    instruction=(
      "You answer questions directly and concisely.\n\n"
      "CALCULATOR: Use calculator(operation, a, b) for ALL math.\n"
      "Operations: 'add', 'subtract', 'multiply', 'divide', 'power', 'modulo'\n"
      "For multi-step: Do one operation, read result, use that number in next operation.\n"
      "CRITICAL: Pass plain numbers as a and b, never objects.\n\n"
      "PDF FILES: Use pdf_tool(file_path) to read PDF attachments.\n"
      "When question mentions 'attached file' or references a PDF, use pdf_tool first to extract the information and answer the question."
    ),
    tools=[calculator, pdf_tool],
    sub_agents=[],
)
