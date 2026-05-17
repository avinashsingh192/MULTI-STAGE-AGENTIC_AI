from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
# Create client once
client = OpenAI(
    api_key=os.getenv("azure_researcher_api"),
    base_url=os.getenv("azure_researcher_endpoint") 
)

# Research Agent Function
def research_agent(user_query):

    response = client.responses.create(
        model="o4-mini",

        tools=[
            {
                "type": "web_search"
            }
        ],

        input=user_query
    )

    return response.output_text

result=research_agent("who won the ipl today")
print(result)