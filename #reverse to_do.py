import pyperclip

input_text = """
Work block 1: 
✅  Meal prep
Work block 2: 
✅  Cleaning (paint)
✅  notion page for ref
✅  brainstorm cold email
✅  brainstorm post ideas
Daily Rituals
Morning 🔆
✅  Wakeup @ 7 am
✅  Walk
✅  Visualize goals
✅  Morning Journal
Evening 🌘
✅  Mouthwash after coffee
✅  Medicine (1/4)
✅  Water (3/3)
✅  Hair and skin care
✅  Plan next day on calendar
🔳  In bed and no phone after 10 pm
"""

modified_todo = []
each_line_in_array = input_text.splitlines()

for line in each_line_in_array:
    line = line.strip()
    if line == '':
        continue
    elif line.startswith("✅"):
        new_string = line.replace("✅", "- [x]")
        modified_todo.append(new_string)
    elif line.startswith("🔳"):
        new_string = line.replace("🔳", "- [ ]")
        modified_todo.append(new_string)
    else:
        # It's a header: add blank line before and make it bold
        if modified_todo and modified_todo[-1] != '':
            modified_todo.append('')
        bold_header = f"**{line}**"
        modified_todo.append(bold_header)

final_output = "\n".join(modified_todo)
pyperclip.copy(final_output)
