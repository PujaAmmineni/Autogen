import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

model="gpt-3.5-turbo"

#dict
llm_config={
    "model":model,
    "api_key":os.environ.get("OPEN_API_KEY"),
}

assistant=AssistantAgent(
    name="Assistant",
    llm_config=llm_config,

)

user_proxy=UserProxyAgent(
    name="user",
    human_input_mode="ALWAYS",
    code_execution_config={
        "work_dir":"coding",
        "use_docker":False,

    },
)

user_proxy.initiate_chat(
    assistant, message="plot a chart of meta and telsa stock price change"
)