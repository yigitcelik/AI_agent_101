from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.deepseek import DeepSeekChat
from phi.model.openai import OpenAIChat
import os
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo



load_dotenv()
# Your existing code here

models ={"groq":Groq(
        model_name="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
    ),
    "deepseek":DeepSeekChat(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY")
),
    "openai":OpenAIChat(
    model="gpt-3.5-turbo", #gpt-3.5-turbo,gpt-4o
    api_key=os.getenv("OPENAI_API_KEY")
)
}


web_agent =Agent(
    name= "web_agent",
    model=models["groq"],
    tools=[DuckDuckGo()],
    instructions=["Always include sources in your response"],
    debug_mode=True,
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name= "finance_agent",
    role = "get financial data",
    model = models["groq"],
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,
                         stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data"],
    debug_mode=True

)

agent_team = Agent(
    team=[web_agent,finance_agent],
    model=models["openai"],
    instructions=["Always include sources","use tables to display data"],
    show_tool_calls=True,
    markdown=True

)

agent_team.print_response("Summarize analyst recommendations and share the latest news for TSLA stock.")

