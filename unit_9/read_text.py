from pathlib import Path

# print(Path.cwd())
# print(Path.home())
# print(Path(__file__).name)
# print(Path(__file__).stem)
# print(Path(__file__).suffix)
# print(Path(__file__).anchor)

# tarzan_file_path = Path.cwd() / "text_assets" / "Tarzan.txt"
tarzan_file_path = Path.cwd().joinpath("text_assets", "Tarzan.txt")
# print(tarzan_fle_path)
try:
    # only surrounds the code that will break
    contents = tarzan_file_path.read_text('utf-8')
except FileNotFoundError as e:
    print(f'Exception: {e}')
except NameError as e:
    print(f'Name Error: {e}')
    contents = 'HI'
else:
    sentences = contents.splitlines()
finally:
    print(contents)
    # words = sentences[505].split(' ')
    # print(words)