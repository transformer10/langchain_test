from langchain import SerpAPIWrapper, LLMMathChain, SQLDatabase, HuggingFaceHub
from langchain.agents import initialize_agent, AgentType
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool

from util import conf

question1 = '''
获得2022年世界杯金球奖、金靴奖、金手套奖的分别是谁？
'''

question2 = '''
查询数据库，告诉我杭州市质差小区名称和eci有哪些。
'''

question3 = '''
查询数据库，分析下eci为189943554的小区质差原因。
'''

pg_uri = f"postgresql+psycopg2://{conf.postgresql['username']}:{conf.postgresql['password']}@{conf.postgresql['host']}:{conf.postgresql['port']}/{conf.postgresql['database']}"
mysql_uri = f"mysql+pymysql://{conf.mysql['username']}:{conf.mysql['password']}@{conf.mysql['host']}:{conf.mysql['port']}/{conf.mysql['database']}"
db = SQLDatabase.from_uri(mysql_uri)
llm = ChatOpenAI(temperature=0)
# llm = HuggingFaceHub(repo_id="WizardLM/WizardCoder-Python-34B-V1.0")
search_tool = Tool(name='search', func=SerpAPIWrapper().run,
                   description='useful for when you need to answer questions about current events')
math_tool = Tool(name='Calculator', func=LLMMathChain(llm=llm, verbose=True).run,
                 description='useful for when you need to answer questions about math')
sql_toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools = [search_tool, math_tool, *sql_toolkit.get_tools()]
agent = initialize_agent(tools, llm, AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
result = agent.run(question2)
print(result)
