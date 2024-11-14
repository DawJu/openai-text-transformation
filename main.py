from openai import OpenAI
from file_reader import file_reader


file_path = 'text_file.txt'
prompt = file_reader(file_path)
print(prompt)

# client = OpenAI()

# completion = client.chat.completions.create(
#     model='',
#     messages=[
#         {'role': 'system', 'content': ''},
#         {
#             'role': 'user',
#             'content': prompt
#         }
#     ]
# )