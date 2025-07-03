from pathlib import Path

tarzan_file_path = Path.cwd().joinpath("text_assets", "Tarzan.txt")

# diff_path_with_suffix = tarzan_file_path.with_suffix('.example')
# tarzan_file_path.replace(diff_path_with_suffix)

# destination = tarzan_file_path.with_suffix('.example')
# print(destination)
# destination.write_text(tarzan_file_path.read_text())

filename = Path('hello.txt')
filename.touch()

# print(filename.stat.__sizeof__())

print(text)

# if not filename.exists:
#     filename.touch()

# print(diff_path_with_suffix)