import json
import random

raw = json.loads(open("jeopardy.json", "r").read())

by_category = {}
filter_keys = ['question', 'answer', 'value']

# ingest the raw data, filter it, and organize it by category
for item in raw[:200]:
  category = item['category']
  if category in by_category.keys():
    by_category[category].append({key: item[key] for key in filter_keys})
  else:
    by_category[category] = [item]

# breakpoint()


def get_questions(category):
  return by_category.get(str.upper(category), [])


def get_question(category):
  return random.choice(get_questions("architects"))


breakpoint()
question = get_question("architects")
breakpoint()

# popularity = [0] * len(by_category.items())
# MAX = ["", 0]
# for key, val in by_category.items():
#   popularity[len(val)]+= 1
#   if popularity[len(val)] > MAX[1]:
#     MAX[0] = key
#     MAX[1] = popularity[len(val)]





