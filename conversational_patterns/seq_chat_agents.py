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

initial_agent=ConversableAgent(
    name="initial_agent",
    llm_config=llm_config,
    system_message="you return me text i give you",
    human_input_mode="NEVER",
)

Upper_case_Agent=ConversableAgent(
    name="Upper_case_Agent",
    llm_config=llm_config,
    system_message="you convert the text in to uppercase i given",
    human_input_mode="NEVER",
)

word_count_Agent=ConversableAgent(
    name="word_count_Agent",
    llm_config=llm_config,
    system_message="you can count the words in the text i given",
    human_input_mode="NEVER",
)

reverse_text_Agent=ConversableAgent(
    name="reverse_text_Agent",
    llm_config=llm_config,
    system_message="you will reverse the text i given",
    human_input_mode="NEVER",
)

summarize_Agent=ConversableAgent(
    name="summarize_Agent",
    llm_config=llm_config,
    system_message="you summarize the text i given you",
    human_input_mode="NEVER",
)


chat_results = initial_agent.initiate_chats(
    [
        {
            "recipient": Upper_case_Agent,
            "message": "This is a sample text document.",
            "max_turns": 2, #each operartional perform twice 
            "summary_method": "last_msg",
        },
        {
            "recipient": word_count_Agent,
            "message": "These are my numbers",
            "max_turns": 2,
            "summary_method": "last_msg",#carryover
        },
        {
            "recipient": reverse_text_Agent,
            "message": "These are my numbers",
            "max_turns": 2,
            "summary_method": "last_msg",
        },
        {
            "recipient": summarize_Agent,
            "message": "These are my numbers",
            "max_turns": 2,
            "summary_method": "last_msg",
        },
    ]
)

print("First Chat Summary: ", chat_results[0].summary)
print("Second Chat Summary: ", chat_results[1].summary)
print("Third Chat Summary: ", chat_results[2].summary)
print("Fourth Chat Summary: ", chat_results[3].summary)