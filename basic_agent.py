from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from test import store_chat_in_supabase
from serper import get_data

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("user", "{input}"),
    ]
)

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",  
    google_api_key="AIzaSyBETOFSRj3wJjAA8L5BPjHV47j_Es7Xu0w"
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser


while True:
    user_input = input("Enter your query (type 'bye' to exit): ")
    if user_input.lower() == "bye":
        print("Goodbye!")
        break
   
    event_data = get_data(user_input)
    user_interest = "I like tech, AI, and innovation"
    prompt = f"""
The following is a list of events:

{event_data}

 suggest the order in which the user should visit these events. Rank them from most to least recommended, explaining briefly why each event is ranked in that order.
 The output should be in the following format:
 Event 1: [Event Name] - [Reason for ranking]
  - Details about the event
 Event 2: [Event Name] - [Reason for ranking]
  - Details about the event
"""


    response = chain.invoke({"input": prompt})
    store_chat_in_supabase(user_input, str(response))  
    print(response)

