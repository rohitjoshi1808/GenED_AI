
import openai
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key=os.getenv("OPENAI_API_KEY")

def generate_question(word):
    prompt  =  f"""

You are an AI Engilsh tutor.

Generate 10 creative, diverse and easy to hard questions using word: {word}

The Questions should be cover:
Diverse use case of {word}
Questions from differ usecase of that word in regular application
short and straight questions

Question should br plain and easy to understand

Question should be in JSON format like:
Question list of {word} :
Question 1 : .....
Question 2 : ......
...............
Question 10 : ....

"""

    
    # print(prompt)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=500
    )

    reply = response.choices[0].message['content']
    return reply

# word = input("Please Enter any word or English noun: " )

# response = generate_question(word)
# print("\n--- AI-Generated Response ---")
# print(response)