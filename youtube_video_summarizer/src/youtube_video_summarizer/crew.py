from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from dotenv import load_dotenv
from tools.transcript_tool import TranscriptTool

load_dotenv()

@CrewBase
class YoutubeVideoSummarizer():
    """YoutubeVideoSummarizer crew for extracting YouTube video transcripts"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def transcript_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['transcript_extractor'], 
            verbose=True,
            tools=[TranscriptTool()]
        )
    
    @agent
    def preprocessing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['preprocessing_agent'], 
            verbose=True
        )
    
    @agent
    def summarization_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['summarization_agent'], 
            verbose=True
        )
    @agent
    def evaluation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['evaluation_agent'], 
            verbose=True
        )

    @task
    def transcript_task(self) -> Task:
        return Task(
            config=self.tasks_config['transcript_task'], 
        )
    
    @task
    def preprocessing_task(self) -> Task:
        return Task(
            config=self.tasks_config['preprocessing_task'], 
        )
    
    @task
    def summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarization_task'], 
        )
    @task
    def evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluation_task'], 
        )

    @crew
    def crew(self) -> Crew:
        """Creates the YoutubeVideoSummarizer crew for transcript extraction"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True
        )
