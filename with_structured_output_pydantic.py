from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal, List
from  pydantic import BaseModel, Field
from pprint import pprint
import streamlit as st

load_dotenv()
#schema
class Review(BaseModel):
    key_themes: List[str] = Field(description="Give the list of key themes discussed")
    summary: str = Field(description="summary of main attention seeker review part in few lines")
    sentiment: Literal['positive', 'negative'] = Field(description="return sentiment of the review")
    pros: Optional[List[str]] = Field(default=None, description="Give list of higlighted pros in the review")
    cons: Optional[List[str]] = Field(default=None, description="Give list of higlighted cons in the review")


review_text = ' '.join(open('review.txt').readlines())

model = ChatOpenAI(model='gpt-6-luna')
#making the model give structured output
structured_model = model.with_structured_output(Review)

result = structured_model.invoke(review_text)

# print(result)
# print("Summary: ", result['summary'])
# print("Sentiment:", result['sentiment'])
# print("Key-Themes:",result['key_themes'])
# print("Pros:", result['pros'])
# print("Cons:", result['cons'])

# pprint(result)
print(result.summary) # The returned Pydantic Object is not subscriptable