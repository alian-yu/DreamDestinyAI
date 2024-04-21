import os
import sys
from urllib.parse import parse_qs


sys.path.insert(0, os.path.dirname(__file__))

from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

def application(environ, start_response):
    # Parse query parameters from the environ dictionary
    query_params = parse_qs(environ.get('QUERY_STRING', ''))
    action = query_params.get('action', [''])[0]
    print(action)
    if action == '':
        file_path = 'public/test.html'
        if os.path.isfile(file_path):
            # Set the response status and content type
            start_response('200 OK', [('Content-Type', 'text/html')])
            # Read the file content
            with open(file_path, 'rb') as file:
                response = file.read()
            return [response]  # Return the file content as bytes
        else:
            start_response('404 Not Found', [('Content-Type', 'text/plain')])
            return [b'404 Not Found']
    elif action == 'chat':
        #print(action)
        message = query_params.get('message', [''])[0]
        start_response('200 OK', [('Content-Type', 'text/plain')])
        version = 'Python %s\n' % sys.version.split()[0]
        response = '\n'.join(['It works!\n', version])

        '''completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {'role': "system", 'content': "You are a meal planner, skilled in generating the meal planning for users according to what foods the user have and how much, such as fruits, veggies, and dairy, and based on whether the user is a vegetarian or not. You will create diverse and nutritious meal plans for a specific time period, such as one or two weeks. This way, the user won't get bored eating the same thing every day, and know how many calories they are consuming at each meal. There should not be extra food ingredients beyond what the user have on hand"},
                {"role": "user", "content": "I am a vegetarian, I live a healthy life. These are the foods in my refrigerator: 1 cucumber, 2 zucchinis, 1 dozen eggs, 5 bananas, 5 apples, 1 bunch of asparagus, a bottle of milk, 1 bag of bread, 1 bottle of oats. list the meal plans for me for 3 days, 3 meals per day."}
            ]
        )
        
        
        response = "Role:" + completion.choices[0].message.role
        response = response + "Content:" + completion.choices[0].message.content
        '''
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {'role': "system", 'content': "You are a meal planner, skilled in generating the meal planning for users according to what foods the user have and how much, such as fruits, veggies, and dairy, and based on whether the user is a vegetarian or not. You will create diverse and nutritious meal plans for a specific time period, such as one or two weeks. This way, the user won't get bored eating the same thing every day, and know how many calories they are consuming at each meal. There should not be extra food ingredients beyond what the user have on hand"},
                {"role": "user", "content": message}
            ]
        )
        
        
        response = "Role:" + completion.choices[0].message.role
        response = response + "Content:" + completion.choices[0].message.content
        #print(completion.choices[0].message)
        print("???")

        return [response.encode()]
