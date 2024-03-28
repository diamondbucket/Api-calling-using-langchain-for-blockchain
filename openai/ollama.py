from langchain_community.llms.ollama import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers.openai_tools import JsonOutputToolsParser
import warnings
import getpass
import os

llm = Ollama(model="tinyllama",callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),temperature=0)
#llm("tell me 5 facts about roman history")

from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["topic"],
    template="give me 5 interesting facts about {topic}?"
)
warnings.simplefilter('ignore', DeprecationWarning)
from langchain.chains.llm import LLMChain
chain = LLMChain(llm=llm,prompt=prompt)
topic = input("enter the topic you want some facts about: ")
print(chain.run({topic}))

'''class Multiply(BaseModel):
    a: int = Field(...,description="first integer")
    b: int = Field(...,description="second integer")

openai_api_key = "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"
llm = ChatOpenAI(model="gpt-3.5-turbo-0125",temperature=0,openai_api_key=openai_api_key)
llm_with_tools = llm.bind_tools([Multiply])
#response = llm_with_tools.invoke("what's 3*12")

tool_chain = llm_with_tools | JsonOutputToolsParser()
response = tool_chain.invoke("what's 3 * 12")
#from openai import ChatOpenAI, BaseModel, Field  # Assuming imports from OpenAI library

# Assuming BaseModel defines fields

#openai_api_key = "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"
#llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

# Create an instance of Multiply with values
multiplier = Multiply(a=3, b=12)

llm_with_tools = llm.bind_tools([Multiply])
response = llm_with_tools.invoke(multiplier)  # Pass the instance to invoke
print(response)'''
