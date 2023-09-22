import os

from util.config import Config

conf = Config()

os.environ["http_proxy"] = conf.proxy['local']
os.environ["https_proxy"] = conf.proxy['local']
os.environ["OPENAI_API_KEY"] = conf.keys['openai-key']
os.environ["HUGGINGFACEHUB_API_TOKEN"] = conf.keys['huggingface-key']
os.environ["SERPAPI_API_KEY"] = conf.keys['serpapi-key']
