import json
import random

#### Demo: l, p, pp, !
# import pdb; pdb.set_trace()
raw = json.loads(open("jeopardy.json", "r").read())

by_category = {}
filter_keys = ['question', 'answer', 'value']

# ingest the raw data, filter for the items we want, and organize it by category
for item in raw[:200]:
  ### Demo 2: n, c, q
  # import pdb; pdb.set_trace()
  category = item['category']
  if category in by_category.keys():
    by_category[category].append({key: item[key] for key in filter_keys})
  else:
    by_category[category] = [item]

def get_questions(category):
  # Returns all questions from the dataset that match the given category
  return by_category.get(str.upper(category), [])


def get_question(category):
  # Returns a random question (question text only) from the given category
  return random.choice(get_questions("architects"))

## Demo 3: s, u, d
# import pdb; pdb.set_trace()

question = get_question("architects")
print(question["question"])



