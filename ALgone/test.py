import os
import openai

os.environ['OPENAI_API_KEY'] = "API_KEY"
openai.api_key = os.getenv("OPENAI_API_KEY")
text = """which product is the most sold?"""
SQL_PREFIX = """You are an agent designed to give SQL Query.
You are given a table and a question.
You must answer the question using SQL.
You must answer ONLY SQL Query.
If the answer is unavailable or unreliable, answer 'Not sure'
The table is as follows:
`Table: Products
product_id (integer, primary key)
product_name (varchar(255))
description (text)
price (decimal)
category_id (integer, foreign key)
Table: Staff
staff_id (integer, primary key)
first_name (varchar(255))
last_name (varchar(255))
email (varchar(255))`
The question is as follows:
"""
complete = SQL_PREFIX + text
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=complete,
    temperature=0,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)
output = response.choices[0].text.strip()
print(output)