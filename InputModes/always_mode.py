import os
from autogen import ConversableAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

model="gpt-3.5-turbo"

#dict
llm_config={
    "model":model,
    "api_key":os.environ.get("OPEN_API_KEY"),
}

agent_with_animal=ConversableAgent(
    "agent_with_animal",
    system_message="you are thinking of an animal. You have animal elephant in mind, and I will try to guessit If try to guess correctly then give a hint",
    llm_config=llm_config,
    is_termination_msg= lambda msg:"elephant" in msg["content"], #terminate if guessed correctly
    human_input_mode="ALWAYS", #always for  human input mode
)

human_proxy=ConversableAgent(
    "human_proxy",
    llm_config=False,
    human_input_mode="ALWAYS",
)

result=human_proxy.initiate_chat(agent_with_animal, message="parrot",
)