# src/basico/custom_agent.py

import os
import openai
from crewai import Agent

class CustomAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Configure a chave da API da OpenAI
        openai.api_key = os.getenv("OPENAI_API_KEY")
    
    def run(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use um modelo válido
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
