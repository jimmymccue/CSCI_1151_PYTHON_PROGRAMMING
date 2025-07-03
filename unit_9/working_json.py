from pathlib import Path
import json

file_path = Path.cwd() / 'file.json'

# contents = file_path.read_text(encoding='utf-8')
# file2 = json.loads(contents)
# print(file2)

# for key, value in file2.items():
#     print(f'key: {key}, value: {value}')

# simple_list = [1,2,3,4,5]

simple_dict = {
  'name' : 'Jimmy'
}

contents = json.dumps(simple_dict)
file_path.write_text(contents)