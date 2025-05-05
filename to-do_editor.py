import pyperclip
import datetime

input_text= """

"""


modified_todo = []

#adding today's date 
date = datetime.datetime.now()
date_format = date.strftime("**%d %B, %Y:**")

modified_todo.append(date_format)

each_line_in_array= input_text.splitlines()

for i in range(len(each_line_in_array)):
    if each_line_in_array[i].startswith("- [ ]"):
        new_string = each_line_in_array[i].replace("- [ ]", ":white_square_button:")
        modified_todo.append(new_string)
    elif each_line_in_array[i]== '':
        continue
    else:
        modified_todo.append(each_line_in_array[i])
        
        
modified_todo.append("Break ideas: Walk, clean, shower, read, dishwasher, water plants")
final_output = "\n".join(modified_todo)
pyperclip.copy(final_output)
        