import json
import random

by_category = {}
filter_keys = ["question", "answer", "value"]

# ingest the raw data, filter for the items we want, and organize it by category
raw = json.loads(open("jeopardy.json", "r").read())
raw = raw[:200]

#### Demo: l, p, pp
# import pdb; pdb.set_trace()
breakpoint()

for item in raw:
    # Demo 2: n, c, q
    # import pdb; pdb.set_trace()
    category = item["category"]
    if category in by_category:
        by_category[category].append({key: item[key] for key in filter_keys})
    else:
        by_category[category] = [item]


def get_questions(category):
    # Returns all questions from the dataset that match the given category
    return by_category.get(str.upper(category), [])


def get_question(category):
    # Returns  random question (question text only) from the given category
    return random.choice(get_questions(category))


# Demo 3: s, r
# breakpoint()
category = "architects"
question = get_question(category)
print(f'Here is your question about "{category}": {question["question"]}')
