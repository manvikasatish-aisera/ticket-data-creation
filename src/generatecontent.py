from vaultsecrets import *
from openai import AzureOpenAI
from numpy import random

def send_prompt_with_document(section, title):
  apikeyPath= "/qa/data/environment/common/openai"

  #gets credentials to login into openai
  api_key = get_openai_details(apikeyPath, "OPENAI_API_KEY_V2")
  api_version = get_openai_details(apikeyPath, "OPENAI_API_VERSION_V2")
  azure_endpoint = get_openai_details(apikeyPath, "OPENAI_API_ENDPOINT_V2")
    
  prompt = "Assume the role of a user of a generative AI product. Given the contents of a document and its title, generate a single question, phrase, or statement that is coherent english. The question, statement, or phrase should be short in length, and cover either main ideas, specific details, or implications, and can use slang, short forms of words, etc. Do not include the document title or role of the user in your response. Do not include any escape characters in your response. Each phrase must refer to the main entity in the title or the content text, and be unique and cover something different about the document everytime you generate a new one. Ignore images and HTML tags, and ensure you don't pull phrases straight from the document."
  client = AzureOpenAI(
        api_key = api_key,
        api_version=api_version,
        azure_endpoint=azure_endpoint)
  
  # Sends the prompt and document to gpt-4, asking for a random 'temperature' between 0 and 1 to create some diversity in responses.
  completion = client.chat.completions.create(
  model = "gpt4",
  temperature = round(random.uniform(0,1), 1),
  messages=[
    {"role": "system", "content": '[Document Title] \n"' + title + '"\n\n[Document Content]\n<<' + section + ">>\n###\n"},
    {"role": "user", "content": '[Prompt]\n"' + prompt + '"'}
  ]
  )
  msg = completion.choices[0].message.content
  #just the string part of the output is returned 
  return msg