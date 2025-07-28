import openai
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key=os.getenv("OPENAI_API_KEY")

def evaluate_questions(answer):
    prompt  =  """
You are an AI Engilsh tutor. I will provide question and answers pairs.
You need to carefully analyze those and provide marks accordingly.

I will provide only 10 questions and answers, mark of each question is 10. So calculate accordingly.

Here is questions and answers pairs:
{answer}

Output format:
{{
marks: marks,
true_questions_list: []
false_questions_list: []
}}

Instruction:
Carefully read and evaluate questions and their answers.
Give me marks out of 100.
I've provided output format so do not add anything else only provide that I have given you in format.
"""

    prompt = prompt.replace("{answer}", answer)
    print("======== Prompt ======")
    print(prompt)

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

# answer = """
# Question 1 : {"question": "What is the full form of COVID-19?", "difficulty": "easy"}
# Answer: COVID-19 stands for cori vali dish - 19

# Question 2 : {"question": "How has COVID-19 affected global economies?", "difficulty": "medium"}
# Answer: It caused massive job losses and business shutdowns. Many countries faced recession and economic slowdown.

# Question 3 : {"question": "What precautions can be taken to prevent the spread of COVID-19?", "difficulty": "easy"}
# Answer: Wear masks, wash hands regularly, and maintain distance. Also, avoid crowded places and get vaccinated.

# Question 4 : {"question": "What is the role of WHO during the COVID-19 pandemic?", "difficulty": "medium"}
# Answer: WHO provided global health guidance and updates. It helped countries with safety protocols and vaccine efforts.

# Question 5 : {"question": "What are the common symptoms associated with COVID-19?", "difficulty": "easy"}
# Answer: Fever, cough, tiredness, and loss of taste or smell. Some people may also have body aches and sore throat.

# Question 6 : {"question": "How has COVID-19 impacted the mental health of individuals worldwide?", "difficulty": "hard"}
# Answer:  It increased stress, anxiety, and feelings of isolation. Lockdowns and fear of illness affected many people's minds.

# Question 7 : {"question": "Which sector has been affected the most due to the COVID-19 pandemic?", "difficulty": "medium"}
# Answer: The healthcare and travel sectors were hit the hardest. Many airlines, hotels, and hospitals faced major challenges.

# Question 8 : {"question": "What are the long-term effects of COVID-19 on the human body?", "difficulty": "hard"}
# Answer:  Some people face tiredness, brain fog, and breathing issues. This condition is often called Long COVID.

# Question 9 : {"question": "How has COVID-19 changed the way businesses operate?", "difficulty": "medium"}
# Answer: Remote work and digital services became more common. Many companies shifted to online platforms and tools.

# Question 10 : {"question": "How has COVID-19 impacted the education system worldwide?", "difficulty": "hard"}
# Answer: Schools closed and moved to online learning. This created learning gaps and access issues for many students.
# """
# response = evaluate_questions(answer)
# print("\n ======= AI-Generated Response ======")
# print(response)