
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a meal planner, skilled in generating the meal planning for users according to what foods the user have and how much, such as fruits, veggies, and dairy, and based on whether the user is a vegetarian or not. You will create diverse and nutritious meal plans for a specific time period, such as one or two weeks. This way, the user won't get bored eating the same thing every day, and know how many calories they are consuming at each meal. There should not be extra food ingredients beyond what the user have on hand"},
    {"role": "user", "content": "I am a vegetarian, I live a healthy life. These are the foods in my refrigerator: 1 cucumber, 2 zucchinis, 1 dozen eggs, 5 bananas, 5 apples, 1 bunch of asparagus, a bottle of milk, 1 bag of bread, 1 bottle of oats. list the meal plans for me for 3 days, 3 meals per day."}
  ]
)

print(completion.choices[0].message)
