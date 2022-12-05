from pathlib import Path

fake_path = Path("C:\my_folder\my_file.txt")
file_path = Path.cwd() / "my_folder"
# file_path.mkdir()  # to create the folder also after this you don't need the line cause line 6 can do both
file_path.mkdir(exist_ok=True)  # to prevent an error

new_file_path = file_path / "my_file.txt"
new_file_path.touch()
print(file_path)

print(file_path.exists())
print("Name -", new_file_path.name)  # to specify the folder name as output
print("Parent -", new_file_path.parent.name)  # to specify the parent folder for my_file.txt
