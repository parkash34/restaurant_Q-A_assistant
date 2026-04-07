# Bella Italia — Restaurant Q&A Assistant

A LangChain powered restaurant Q&A assistant built with FastAPI and Groq AI.
This project demonstrates core LangChain concepts including prompt templates,
chains and output parsers to build a structured restaurant assistant.

## Features

- LangChain prompt templates — reusable structured prompts
- Chain pipeline — prompt | llm | parser using | operator
- Structured JSON responses — category, answer and can_help fields
- Real restaurant data injection — no hallucination
- Input validation — empty questions rejected automatically
- Fast responses using Groq's LLaMA 3.3 70B model

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend web framework |
| LangChain | AI chain framework |
| Groq API | AI language model provider |
| LLaMA 3.3 70B | AI model |
| Pydantic | Data validation |
| python-dotenv | Environment variable management |

## Project Structure
```
project/
│
├── .venv/               
├── main.py            
├── .env               
└── requirements.txt   
```

## Setup

1. Clone the repository
```
git clone https://github.com/yourusername/bella-italia-qa
```

2. Create and activate virtual environment
```
python -m venv env
env\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Create `.env` file and add your Groq API key
```
API_KEY=your_groq_api_key_here
```

5. Run the server
```
uvicorn main:app --reload
```

## API Endpoint

### POST /ask

**Request:**
```json
{
    "question": "Do you have vegan options?"
}
```

**Response:**
```json
{
    "answer": "Yes we have vegan options including Vegan Arrabbiata pasta!",
    "category": "menu",
    "can_help": true
}
```

## LangChain Concepts Used
```
ChatPromptTemplate  →  structured reusable prompt with variables
ChatGroq            →  LangChain integration with Groq API
JsonOutputParser    →  converts AI response to Python dict
Chain               →  prompt | llm | parser pipeline
```
## Restaurant Information
```
Name:          Bella Italia
Location:      Astoria, New York
Opening Hours: 12 PM to 11 PM
Phone:         123-456-7890
```

## Menu

| Category | Items |
|---|---|
| Pizzas | Margherita, Pepperoni, Vegetarian |
| Pastas | Carbonara, Bolognese, Vegan Arrabbiata |
| Desserts | Tiramisu, Gelato |

## Dietary Options

- Vegetarian
- Vegan
- Gluten Free

## Environment Variables

API_KEY=your_groq_api_key_here

## Notes

- Never commit your .env file to GitHub
- Assistant only answers Bella Italia related questions
- Unrelated questions return can_help: false