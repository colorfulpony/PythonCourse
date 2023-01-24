from pathlib import Path

root_dir = Path('')
files_path = Path('destination/files')

for path in root_dir.rglob("**/*.txt"):
    if path.is_file():
        if "14" in path.name:
            print(path.absolute())

