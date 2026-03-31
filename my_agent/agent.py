"""
This file is where you will implement your agent.
The `root_agent` is used to evaluate your agent's performance.
"""

from google.adk.agents import llm_agent
from my_agent.tools.calculator import calculator

root_agent = llm_agent.Agent(
    model="gemini-2.5-flash-lite",
    name="agent",
    description="A helpful assistant with mathematical and reason capabilities.",
    instruction=(
      "Yoy are a helpful assitant that answers question directly and concisely."
      "Use the calculator tool to perform mathematical operations when needed."
      "Use the pdf reader to read the pdf and answer the questions whose input is a pdf file."
    ),
    tools=[calculator, pdf_reader],
    sub_agents=[],
)
