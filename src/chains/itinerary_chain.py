from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY

llm= ChatGroq(
    groq_api_key=GROQ_API_KEY,  
    model_name="llama-3.3-70b-versatile",
    temperature=0.3
)

itinerary_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful travel assistant. Create a day trip itinerary for {city} based on user's interest: {interest}. Provide a brief , bulleted itinerary"),
        ("human", "Create a itinerary for my day trip")
    ]
)  

def generate_itinerary(city: str, interests: list[str]) -> str:
    """
    Create a str that generates a day trip itinerary based on user input.
    """
    response = llm.invoke(
        itinerary_prompt.format_messages(city=city, interest=','.join(interests))

    )
    return response.content



    



