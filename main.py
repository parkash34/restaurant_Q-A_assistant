import os
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API KEY is missing in .env file")

app = FastAPI()

class Question(BaseModel):
    question : str

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0.2,
    max_tokens = 500,
    api_key = api_key
)

restaurant = {
    "name": "Bella Italia",
    "opening_hours": "12 PM to 11 PM",
    "location": "Astoria, New York",
    "phone": "123-456-7890",
    "menu": {
        "pizzas": ["Margherita", "Pepperoni", "Vegetarian"],
        "pastas": ["Carbonara", "Bolognese", "Vegan Arrabbiata"],
        "desserts": ["Tiramisu", "Gelato"]
    },
    "dietary_options": ["vegetarian", "vegan", "gluten_free"],
    "prices": {
        "pizzas": "$12-$18",
        "pastas": "$10-$16",
        "desserts": "$6-$10"
    }
}

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a restaurant assistant for {restaurant_name}
     Answer questions related to our opening hours, location, menu, and dietary options.
     Use the following data of {restaurant_name} restaurant.
     opening_hours : {opening_hours}
     location : {location}
     phone : {phone}
     menu : {menu}
     dietary options : {dietary_options}
     prices : {prices}
     
     Always respond in this exact JSON format:
    {{
        "answer": "your answer here",
        "category": "menu/hours/location/other",
        "can_help": true or false
    }}
    Do not add any text outside the JSON."""),
    ("user", "{question}")
])


chain = prompt | llm | JsonOutputParser()


@app.post("/ask")
def ask_ai(question : Question):
    if not question.question.strip():
        return "Question doesn't exist or you didn't type anything."
    
    result = chain.invoke({
        "restaurant_name" : restaurant["name"],
        "opening_hours" : restaurant["opening_hours"],
        "location" : restaurant["location"],
        "phone" : restaurant["phone"],
        "menu" : restaurant["menu"],
        "dietary_options" : restaurant["dietary_options"],
        "prices" : restaurant["prices"],
        "question": question.question
    })
    return result
