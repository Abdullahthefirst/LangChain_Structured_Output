from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()
#schema
class Review(TypedDict):
    summary:str
    sentiment:str

review_text = ' '.join(open('review.txt').readlines())

model = ChatOpenAI(model='gpt-6-luna')
#making the model give structured output
structured_model = model.with_structured_output(Review)

result = structured_model.invoke(review_text)

print(result)
print(result['summary'])
print(result['sentiment'])