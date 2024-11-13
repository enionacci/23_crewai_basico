from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.basico.custom_agent import CustomAgent  # Importe o agente personalizado

# from dotenv import load_dotenv
# load_dotenv()

import os
import openai
# Configure a chave da API
api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key  # Adicione esta linha
openai.api_key = api_key

# Uncomment the following line to use an example of a custom tool
# from basico.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class BasicoCrew():
	"""Basico crew"""

	@agent
	def researcher(self) -> CustomAgent:
		return Agent(
			config=self.agents_config['researcher'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			llm="gpt-4o-mini",
		)

	@agent
	def reporting_analyst(self) -> CustomAgent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			llm="gpt-4o-mini",
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
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)