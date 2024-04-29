from openai import OpenAI
import os



# Set up your OpenAI API credentials
# my_api_key = ''
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ["OPENAI_TOKEN"],
)


MODEL = "gpt-3.5-turbo"
# Define the function to generate answers
def generate_answer(question):
# example with a system message
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant in a discord server answering question and being helpful."},
            {"role": "user", "content": question},
        ],
        temperature=0,
    )

    return response.choices[0].message.content