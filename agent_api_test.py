import os

import requests
from langchain import OpenAI
from langchain.agents import create_openapi_agent, initialize_agent, AgentType
from langchain.agents.agent_toolkits.openapi.spec import reduce_openapi_spec
from langchain.chains.openai_functions.openapi import get_openapi_chain
from langchain.chains.api import open_meteo_docs
from langchain.chains import APIChain
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from langchain.utilities import RequestsWrapper
from langchain.tools.json.tool import JsonSpec
from langchain.agents.agent_toolkits import OpenAPIToolkit, NLAToolkit
from util import conf

# llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
# chain = get_openapi_chain('http://127.0.0.1:8080/swagger/doc.json', llm=llm)

# chain = get_openapi_chain("https://www.klarna.com/us/shopping/public/openai/v0/api-docs/")

# chain = APIChain.from_llm_and_api_docs(llm, 'http://localhost:8080/swagger/doc.json')
# print('hello')
# chain.run("How's the weather like today?")


#
# headers = {"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}
# openai_requests_wrapper = RequestsWrapper(headers=headers)
# data = requests.get('http://localhost:8080/swagger/doc.json').text
# json_spec = JsonSpec(dict_=data, max_value_length=4000)

# openapi_toolkit = OpenAPIToolkit.from_llm(
#     OpenAI(temperature=0), json_spec, openai_requests_wrapper, verbose=True
# )
# openapi_toolkit = NLAToolkit.from_llm_and_url(llm=OpenAI(temperature=0),
#                                               open_api_url="http://localhost:8080/swagger/doc.json")

# spoonacular_toolkit = NLAToolkit.from_llm_and_url(
#     OpenAI(temperature=0),
#     "https://spoonacular.com/application/frontend/downloads/spoonacular-openapi-3.json",
#     max_text_length=1800,  # If you want to truncate the response text
# )
# openapi_agent_executor = create_openapi_agent(
#     llm=OpenAI(temperature=0), toolkit=spoonacular_toolkit, verbose=True
# )

#
# openapi_agent_executor.run("How's the weather like today?")


llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
prompt = OPEN_METEO_DOCS = """ BASE URL: http://localhost:8080
API Documentation is as follows:
{
    "schemes": [],
    "swagger": "2.0",
    "info": {
        "description": "",
        "title": "",
        "contact": {},
        "version": ""
    },
    "host": "",
    "basePath": "/api/v1",
    "paths": {
        "/weather/today": {
            "get": {
                "description": "get today's weather",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "weather tool"
                ],
                "summary": "get today's weather",
                "responses": {
                    "200": {
                        "description": "OK"
                    }
                }
            }
        },
        "/weather/tomorrow": {
            "get": {
                "description": "get today's weather",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "weather tool"
                ],
                "summary": "get today's weather",
                "responses": {
                    "200": {
                        "description": "OK"
                    }
                }
            }
        }
    }
}
"""
# https://www.langchain.com.cn/modules/chains/examples/api
open_meteo_docs.OPEN_METEO_DOCS
chain_new = APIChain.from_llm_and_api_docs(llm, prompt, verbose=True)
api_tool = Tool(name='Api Search', func=chain_new.run,
                description='useful for when you need to answer questions about weather')
tools = [api_tool]
agent = initialize_agent(tools, llm, AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
result = agent.run("明天气温是几度？")
