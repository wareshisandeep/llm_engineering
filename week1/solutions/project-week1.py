# imports
import os
#import requests
#import json
#from typing import List
#from dotenv import load_dotenv
#from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display
from openai import OpenAI

# constants
MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'
MODEL_DEEPSEEK = "deepseek-r1:1.5b"

OLLAMA_BASE_URL = 'http://localhost:11434/v1'
OLLAMA_API_KEY = 'ollama'
HEADERS = {"Content-Type": "application/json"}

openai = OpenAI(base_url=OLLAMA_BASE_URL, api_key=OLLAMA_API_KEY)


# set up environment

system_prompt = "You are a helpful technical tutor who answers questions about python code, software engineering, data science and LLMs"


# method to return user prmpt
def get_user_prompt(question):
    user_prompt = f"I am stuck with following question: {question} - "
    user_prompt += '''please help me understand what the code is trying to do, provide  '''
    return user_prompt



def answer_question(queston):
    user_prompt = get_user_prompt(question)
    response = openai.chat.completions.create(
        model=MODEL_LLAMA,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

    )
    result = response.choices[0].message.content
    display(Markdown(result))


question = """
how are you
"""

answer_question(question)