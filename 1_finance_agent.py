from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.deepseek import DeepSeekChat
from phi.model.openai import OpenAIChat
import os
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools


load_dotenv()


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

agent = Agent(
    model=models["groq"],
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,
                         stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data"],
    debug_mode=True
)
agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA, and give latest stock news")

