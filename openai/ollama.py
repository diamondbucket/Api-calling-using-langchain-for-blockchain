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
