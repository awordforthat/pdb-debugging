import util

data = util.load_data()

"""
This module contains tasks to give you practice with the very 
basics of interacting with code in the pdb shell: looking around
and printing things out.
"""

by_category = {}
filter_keys = ["question", "answer", "value"]

### Task 1a - stop the code execution here. What is the next line that will be executed?
### Task 1b - what is the value of `data`? Print it to the console.
### Task 1c - Now pretty-print the `data` object so we can actually read it!

### Task 2a - stop the code on the first line inside the for loop and list the context. What are the first and last lines that we get?
### Task 2b - without rerunning the code, list the context again. What lines do you get?
### Task 2c - contrast that with the behavior of (w)here. How are they different?

for item in data:
    category = item["category"]
    if category in by_category:

        by_category[category].append({key: item[key] for key in filter_keys})
    else:
        by_category[category] = [item]
