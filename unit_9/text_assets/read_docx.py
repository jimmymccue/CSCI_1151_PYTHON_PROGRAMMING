from pathlib import Path
import docx2txt

tarzan_file_path = Path.cwd().joinpath("text_assets", "Tarzan.txt")

try:
    contents = docx2txt.process(tarzan_file_path)
except FileNotFoundError as e:
    print(f'Exception thrown: {e=}')
else:
    words = contents.split()
    print(len(words))
    print(type(words))
    