import util
import random

data = util.load_data()

"""
This module contains tasks to give you practice in navigating up and 
down the current stack.
"""

by_category = {}
filter_keys = ["question", "answer", "value"]


for item in data:
    category = item["category"]
    if category in by_category:
        by_category[category].append({key: item[key] for key in filter_keys})
    else:
        by_category[category] = [item]


def get_questions(category):
    # Returns all questions from the dataset that match the given category
    breakpoint()
    return by_category.get(str.upper(category), [])


def get_question(category):
    # Returns  random question (question text only) from the given category
    return random.choice(get_questions(category))


### Task 1a - stop the code right before `question` is assigned. What is the current context?
### Task 1b - step into the function using s(tep). What is the next line to be executed?
### Task 1c - rerun the example and this time go to the n(ext) line. What is the next line to be executed?

### Task 2 - Stop the code in the same place as before. S(tep) into the get_question function and
# enter n(ext) to get to line 30. S(tep) again. What function do we end up in?

### Task 3a - Stop the code in the same place as before. Print out w(here) you are. How many frames are in the stack?
### Task 3b - Rerun the example and step into the next function. Use the w(here) command again. How many frames are there now?
### Task 3c - Now put a breakpoint in `get_questions`. Navigate u(p) and d(own) in the frame. How many u(p) commands is it to the top of the stack?

category = "architects"
question = get_question(category)
print(f'Here is your question about "{category}": {question["question"]}')
