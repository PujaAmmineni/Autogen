import os
from autogen import ConversableAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

model="gpt-3.5-turbo"

#dict
llm_config={
    "model":model,
    "temperature":0.9,
    "api_key":os.environ.get("OPEN_API_KEY"),
}

agent_with_animal=ConversableAgent(
    "agent_with_animal",
    system_message="you are thinking of an animal. You have animal elephant in mind, and I will try to guessit If try to guess correctly then give a hint",
    llm_config=llm_config,
    max_consecutive_auto_reply=1,
    is_termination_msg= lambda msg:"elephant" in msg["content"], #terminate if guessed correctly
    human_input_mode="TERMINATE", #always for  human input mode
)

agent_guess_animal=ConversableAgent(
    "agent_guess_animal",
    system_message="i have a animal in my mind you will try to guess it if i give hints, use it narrow down  your guesses",
    llm_config=llm_config,
    human_input_mode="NEVER" #no human input mode
)

result=agent_with_animal.initiate_chat(agent_guess_animal, message="I'm thinking of animal guess which animal")
