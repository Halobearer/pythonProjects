from pathlib import Path

# path = pathlib.Path.cwd()
fake_path = Path("C:\Cohort14\private.img")
cwd_path = Path.cwd() / "damian"
print(cwd_path)

# parent gives you the parent for that particular file then parents is for all files till the root
# print("Parents -", path.parent)
# print(list(path.parents))
# print("Anchor -", path.anchor)
# print("Name -", path.name)
# print("Suffix -", path.suffix)
# print("Stem -", path.stem)

cwd_path.mkdir(exist_ok=True)
# The reason for the exist_ok is to prevent an error because running the code again will
# make it look ike you want to create another file

new_file_path = cwd_path / "private.txt"
new_file_path.touch()

print(fake_path.exists())
print(cwd_path.exists())
print("Dir -", cwd_path.is_dir())

