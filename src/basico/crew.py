# src/basico/crew.py

from crewai import Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.basico.custom_agent import CustomAgent

import os
import openai

api_key = os.getenv("OPENAI_API_KEY")
print(f"OPENAI_API_KEY is set: {api_key is not None}")
if api_key is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

openai.api_key = api_key

@CrewBase
class BasicoCrew():
    """Basico crew"""

    @agent
    def researcher(self) -> CustomAgent:
        return CustomAgent(
            config=self.agents_config['researcher'],
            verbose=True,
        )

    @agent
    def reporting_analyst(self) -> CustomAgent:
        return CustomAgent(
            config=self.agents_config['reporting_analyst'],
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Basico crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
