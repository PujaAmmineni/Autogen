import os
from autogen import ConversableAgent, AssistantAgent, UserProxyAgent
from typing import Annotated

from dotenv import load_dotenv

load_dotenv()

model = "gpt-3.5-turbo"
llm_config = {
    "model": model,
    "temperature": 0.9,
    "api_key": os.environ["OPENAI_API_KEY"],
}

travel_agent=ConversableAgent(
    name="Travel_Agent",
    system_message="You a traveler Planning a Vacation",
    llm_config=llm_config,
)

guide_agent=ConversableAgent(
    name="Guide_Agent",
    system_message="You a GuideAgent you will have extensive knowledge about travels",
    llm_config=llm_config,
)


chat_agent=travel_agent.initiate_chat(
    guide_agent,
    message="what are must see attraction on india",
    summary_method="reflection_with_llm",
    max_turns=2,

)


#print(chat_agent)

print("\n ***Chat Summary***: \n")
print(chat_agent.summary)
print(ConversableAgent.DEFAULT_SUMMARY_PROMPT)

import pprint

print("\nChat history: \n")
pprint.pprint(chat_agent.chat_history)

print("\n**Chat Cost**: \n")
pprint.pprint(chat_agent.cost)