from vaultsecrets import *
from openai import AzureOpenAI
from numpy import random
from dotenv import load_dotenv

def generate_ticket_content():
  load_dotenv()
  apikeyPath= "/qa/data/environment/common/openai"
  
  # gets credentials to login into openai
  api_key = get_openai_details(apikeyPath, "OPENAI_API_KEY_V2")
  api_version = get_openai_details(apikeyPath, "OPENAI_API_VERSION_V2")
  azure_endpoint = get_openai_details(apikeyPath, "OPENAI_API_ENDPOINT_V2")
    
  num_tickets = os.getenv("NUM_TICKETS")
  specified_domain = os.getenv("SPECIFIED_DOMAIN")

  prompt = f"Please create {num_tickets} sample Jira tickets for {specified_domain}, \
            each with the following fields: Summary, Description, Issue Type, Priority, Status, \
            Assignee, Reporter, Labels, Components, Fix Versions, Affected Versions, and Resolution. \
            Each ticket should have a Summary of no more than 10 words, a Description of at least \
            40 words, and a Resolution of up to 100 words. Write each ticket in a natural, \
            conversational tone and mark all of them as 'Resolved'. Randomly generate names for the Assignee and Reporter. Format the output as a CSV file, \
            with each column representing a field and each row representing a ticket."

  client = AzureOpenAI(
        api_key = api_key,
        api_version=api_version,
        azure_endpoint=azure_endpoint)
  
  # Sends the prompt and document to gpt-4, asking for a random 'temperature' between 0 and 1 to create some diversity in responses.
  completion = client.chat.completions.create(
    model = "gpt4",
    temperature = round(random.uniform(0,1), 1),
    messages=[{"role": "user", "content": prompt}]
  )
  
  msg = completion.choices[0].message.content
  # just the string part of the output is returned 
  return msg

print(generate_ticket_content())