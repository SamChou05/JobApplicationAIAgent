from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from resume_reader import resume_engine
from job_listings_reader import job_listings_engine

load_dotenv()

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=job_listings_engine,
        metadata=ToolMetadata(
            name="job_listings",
            description="this gives a list of job listings",
        ),
    ),
    QueryEngineTool(
        query_engine=resume_engine,
        metadata=ToolMetadata(
            name="resume_data",
            description="this gives information about a resume in pdf format",
        ),
    ),
]

llm = OpenAI(model="gpt-3.5-turbo-0613")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
