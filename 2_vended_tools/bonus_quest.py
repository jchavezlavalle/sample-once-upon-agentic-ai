import os
from strands import Agent
from strands.vended_tools.shell import shell
from strands.vended_tools.file_editor import file_editor
from strands.vended_interventions.hitl import HumanInTheLoop

arcane_scribe = Agent(
    tools=[
        shell,
        file_editor
    ],
    system_prompt=f"""You are Kiro the Grey Hat, a wizard who specializes in the ancient art of code magic.
    When asked to create spells (code), you inscribe them on parchment (files) in the directory {os.getcwd()}
    and then cast them to demonstrate their power.""",
    interventions=[HumanInTheLoop(ask="stdio")],
)

response = arcane_scribe("Create a magical scroll that generates the first 10 numbers of the Fibonacci sequence and demonstrate its power!")
