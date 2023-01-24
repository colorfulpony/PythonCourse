from pathlib import Path
import zipfile

root_dir = Path('.')
files_path = Path('files')

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path, 'r') as zf:
        zf.extractall(path=files_path)

